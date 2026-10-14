# Human website passwords and browser autofill

Owner: this package for storage and migration boundaries; provider-supported setup
for installation/account verification.
This procedure does not install a migration helper or claim a direct bulk API.

## Choose the human store

Use the user's explicit choice. Otherwise ask once between Apple Passwords
with Apple's official iCloud Passwords Chrome extension and Google Password
Manager. Preserve existing working logins while the choice is pending.
One human store is the target; three independently maintained copies are not.
Protected automation entries remain at their configured owner. Never move them wholesale.

## Platform choices

| Platform | Automation secrets | Human website logins in Chrome |
|---|---|---|
| macOS | macOS Keychain | Apple Passwords + official iCloud Passwords extension, or Google Password Manager |
| Windows | Windows Credential Manager | Google Password Manager; Apple users may instead choose iCloud for Windows + the official iCloud Passwords extension after compatibility/setup verification |

Ask for a browser-password preference independently from the OS automation
store. Record the selected manager, Chrome profile and account/device storage
scope as reference-only local settings. Never assume the teammate uses Apple
because the example was developed on a Mac. Existing explicit choices persist.
Windows Credential Manager does not substitute for a saved Chrome website login.

### Google Password Manager on Windows or macOS

1. Resolve the intended Chrome profile and whether the user wants account-synced
   storage or device-only storage. Do not silently sign into another Google
   account or enable synchronization as part of copying a credential.
2. Open Chrome > Passwords and autofill > Google Password Manager > Add.
   Save the verified website, actual username and existing password through
   the approved secure transfer path. Alternatively use Chrome's Save prompt
   after an authorized sign-in. Do not expose password previews to the agent.
3. Bulk import uses Google Password Manager > Settings > Import passwords.
   Google's supported CSV needs `url`, `username` and `password` columns.
   The plaintext-file exception below applies to both platforms. Prepare the
   exact subset and private temporary location first; ask only for the missing
   exception. Existing authorization persists, so do not ask again for the same
   reviewed transfer or cleanup.
4. Verify Chrome suggests the right domain/account and sign-in succeeds. On
   Windows, the user completes Windows Hello or other native authentication
   when required. Keep automation credentials in Credential Manager.

Use provider-supported setup and verify the intended transport. This is a
supported UI/import procedure, not a shipped universal migration script. Never
write Chrome's Login Data database, decrypt its store, or export all Windows
credentials to obtain one website password. Use only selected references; no
plaintext values in PowerShell output, history, tool arguments or logs.

## Inventory before transfer

1. Read the user’s selected reference-only project/service metadata. Record candidate website, actual login username, source reference,
   intended manager and status there only, with normal restricted permissions.
2. Confirm each candidate is a reusable human website password. Names containing
   `admin`, `owner` or `password` are hints, not proof. Exclude API/app passwords,
   SQL connection URLs, encryption/JWT keys, invite links and recovery codes.
3. Resolve the exact login domain and username from evidence. A Keychain
   account label may be a storage label, not the web username.
   Do not invent a website from a service slug or copy to sibling subdomains.
4. Report coverage accurately: a pointer inventory does not enumerate all old
   Keychain, Safari or Chrome records. Do not dump Keychain contents or decrypt
   browser password databases to fill gaps.
5. Resolve an existing destination entry by domain + username. Never overwrite,
   delete, rotate or merge a conflicting password merely to make migration pass.

## Transfer through supported surfaces

- Apple Passwords: use its website-entry UI with website, username and existing
  password. Chrome consumes it through the official Apple extension; verify the
  extension's publisher and current OS requirements before installing.
- Google Password Manager: use its supported Add entry or Chrome save-password
  flow with the exact website and username.
- Agent setup owns supported provisioning. The human handles unavoidable native
  unlock, Touch ID, provider sign-in and extension consent. Existing browser/UI
  authorization rules still apply; opening an official consent page is not
  permission to control unrelated tabs.
- Secret values must bypass model-visible arguments, output, screenshots and
  logs. A reviewed local transfer may read a specific approved source into
  memory and hand it directly to an authorized destination. No broad Keychain
  dump, raw Chrome database writes, credential-store decryption or silent
  `security add-internet-password` substitution for a verified Passwords entry.
- A generic Keychain entry has no verified automatic bulk conversion in this
  procedure. Preserve the source until the destination's actual autofill works.
- Apple and Google document CSV import, but CSV contains plaintext secrets.
  This procedure does **not** authorize exporting or generating password CSVs,
  even in `/tmp`, Downloads or an ignored folder. When CSV is the only supported
  bulk route, explain this exact limitation and obtain an explicit narrow
  exception with a defined subset, private non-synced handling and cleanup plan.
  Never read a password CSV into the model. Do not ask for secrets in chat.
- Avoid clipboard transfer by default. If the user chooses it, account for
  clipboard-history capture; clearing the current clipboard alone does not
  clear a history manager. Never leave an unattended password on the clipboard.

## Verify and finish

1. Confirm the selected manager has the exact domain and username, without
   revealing the saved password. Separate installed, unlocked, saved and verified.
2. Test Chrome autofill on one intended login page and verify the resulting
   account after sign-in. A stored generic Keychain secret is not this test.
3. Repeat verification for migrated entries as appropriate. Record counts and
   per-entry pending/conflict status only in local reference metadata; do not
   label a whole migration verified from one successful sample.
4. Keep working source entries while any consumer still depends on them. A later
   removal or password rotation is separate work. Document any remaining copies
   and their rotation dependency; there is no assumed two-way synchronization.
5. New deployments include this human-access check alongside a separate verified
   automation credential. If blocked, identify the exact missing native consent,
   domain, username, supported transfer path or verification step.

## Convenient daily access

With Apple selected, Chrome uses the official extension to fill matching website
logins. Passwords also offers Settings > Show Passwords in Menu Bar for manual
lookup. With Google selected, use Chrome's Google Password Manager for lookup
and its built-in matching-login suggestions. App hotkeys are optional personal
setup; never claim a shortcut is configured unless verified.

## Primary sources

Reviewed Oct 4, 2026; check current compatibility before setup.

- [Apple's official iCloud Passwords extension](https://chromewebstore.google.com/detail/icloud-passwords/pejdijmoenmkgeppbflobdenhhabjlaj?hl=en)
- [Create an Apple Passwords website entry](https://support.apple.com/guide/passwords/mchla6acb8cb/mac)
- [Apple Passwords CSV import](https://support.apple.com/guide/passwords/mchl2f1a184c/mac)
- [Apple Passwords menu bar access](https://support.apple.com/guide/passwords/menu-bar-mchldd5eb88d/mac)
- [Google Password Manager CSV import](https://support.google.com/chrome/answer/13068232?co=GENIE.Platform%3DDesktop&hl=en)

- [Google: manage and add website passwords](https://support.google.com/chrome/answer/95606?co=GENIE.Platform%3DDesktop&hl=en)
- [Microsoft: Windows Credential Manager](https://support.microsoft.com/en-us/windows/security/credential-manager-in-windows)
