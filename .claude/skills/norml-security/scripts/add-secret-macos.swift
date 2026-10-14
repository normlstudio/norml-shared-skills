import AppKit
import Security
import Foundation

func fail(_ message: String, _ code: Int32) -> Never {
    fputs(message + "\n", stderr)
    exit(code)
}
let args = Array(CommandLine.arguments.dropFirst())
guard args.count == 2 || (args.count == 3 && args[2] == "--replace") else {
    fail("Usage: swift add-secret-macos.swift SERVICE ACCOUNT [--replace]", 1)
}
guard !args[0].isEmpty && !args[1].isEmpty else { fail("Non-secret identifiers are required.", 1) }
let query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrService as String: args[0],
    kSecAttrAccount as String: args[1]
]
let existing = SecItemCopyMatching(query as CFDictionary, nil)
if existing == errSecSuccess && args.count != 3 {
    fail("Existing entry refused; authorize --replace after checking consumers.", 3)
}
if existing != errSecSuccess && existing != errSecItemNotFound { fail("Keychain lookup failed.", 3) }
let application = NSApplication.shared
application.setActivationPolicy(.accessory)
application.activate(ignoringOtherApps: true)
let alert = NSAlert()
alert.messageText = "Store a protected credential"
alert.informativeText = "Service: " + args[0] + "\nAccount: " + args[1] + "\nThe value remains in this process and Keychain."
alert.addButton(withTitle: "Save")
alert.addButton(withTitle: "Cancel")
let field = NSSecureTextField(frame: NSRect(x: 0, y: 0, width: 360, height: 24))
alert.accessoryView = field
alert.window.initialFirstResponder = field
guard alert.runModal() == .alertFirstButtonReturn else { fail("Canceled.", 2) }
let value = Data(field.stringValue.utf8)
field.stringValue = ""
guard !value.isEmpty else { fail("Empty value refused.", 2) }
let status: OSStatus
if existing == errSecSuccess {
    status = SecItemUpdate(query as CFDictionary, [kSecValueData as String: value] as CFDictionary)
} else {
    var item = query
    item[kSecValueData as String] = value
    status = SecItemAdd(item as CFDictionary, nil)
}
guard status == errSecSuccess else { fail("Protected credential write failed.", 3) }
var check = query
check[kSecReturnData as String] = true
var stored: CFTypeRef?
guard SecItemCopyMatching(check as CFDictionary, &stored) == errSecSuccess,
      let bytes = stored as? Data, bytes == value else { fail("Readback verification failed.", 4) }
print("Stored and verified; provider resource access remains unverified.")
