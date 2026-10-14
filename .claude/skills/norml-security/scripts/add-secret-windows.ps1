[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)] [string]$Service,
    [Parameter(Mandatory=$true)] [string]$Account,
    [string]$Message = "Enter the secret in the masked Password field",
    [switch]$ReplaceExisting
)
$ErrorActionPreference = 'Stop'
if (-not (Get-Module -ListAvailable -Name CredentialManager)) {
    Write-Error 'CredentialManager is a required reviewed prerequisite; no module was installed.'
    exit 3
}
try {
    Import-Module CredentialManager -ErrorAction Stop
    if ((Get-StoredCredential -Target $Service) -and -not $ReplaceExisting) {
        Write-Error 'Existing target refused; authorize -ReplaceExisting only after checking consumers.'
        exit 3
    }
    $credential = Get-Credential -UserName $Account -Message $Message
    if (-not $credential -or -not $credential.GetNetworkCredential().Password) {
        Write-Error 'Canceled or empty secret.'
        exit 2
    }
    New-StoredCredential -Target $Service -Credential $credential -Persist LocalMachine | Out-Null
    $stored = Get-StoredCredential -Target $Service
    if (-not $stored -or $stored.GetNetworkCredential().Password -cne $credential.GetNetworkCredential().Password) {
        Write-Error 'Protected-store readback failed; consumer access remains unverified.'
        exit 4
    }
    $credential = $null
    $stored = $null
    Write-Output 'Stored and verified; provider access still requires a scoped resource check.'
} catch {
    Write-Error 'Credential operation failed; no secret or provider response is printed.'
    exit 3
}
