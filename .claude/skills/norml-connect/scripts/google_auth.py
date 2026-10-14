"""Provider-managed Google credentials. Never emit credential material."""
import datetime as dt
import shutil
import subprocess

def load_credentials(account, quota_project=None, mode='gcloud', scopes=None):
    if not account or '@' not in account:
        raise ValueError('An explicit Google account is required')
    scopes = scopes or ['https://www.googleapis.com/auth/drive']
    if mode == 'adc':
        import google.auth
        creds, _ = google.auth.default(scopes=scopes, quota_project_id=quota_project)
        return creds
    if mode != 'gcloud':
        raise ValueError('Choose gcloud or adc explicitly')
    if not shutil.which('gcloud'):
        raise RuntimeError('Google Cloud CLI is missing; follow the connection recipe')
    from google.oauth2.credentials import Credentials
    from google.auth.exceptions import RefreshError
    def refresh(_request, scopes=None):
        try:
            result = subprocess.run(
                ['gcloud','auth','print-access-token','--account',account],
                check=True, capture_output=True, text=True, timeout=45)
        except (OSError, subprocess.SubprocessError):
            raise RefreshError('Google token broker failed; reconnect the selected account') from None
        token=result.stdout.strip()
        if not token:
            raise RefreshError('Google token broker returned no credential')
        expiry=dt.datetime.now(dt.timezone.utc).replace(tzinfo=None)+dt.timedelta(minutes=25)
        return token, expiry
    return Credentials(token=None, scopes=scopes, refresh_handler=refresh,
                       quota_project_id=quota_project, account=account)

def verify_drive_identity(drive, expected_account):
    user=drive.about().get(fields='user(emailAddress)').execute().get('user',{})
    if user.get('emailAddress','').casefold()!=expected_account.casefold():
        raise RuntimeError('Connected Google identity does not match the selected account')
    return True
