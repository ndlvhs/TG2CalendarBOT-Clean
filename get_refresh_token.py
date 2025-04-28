from google_auth_oauthlib.flow import InstalledAppFlow

def main():
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json',   # укажи свой путь к файлу client_secrets.json
        scopes=["https://www.googleapis.com/auth/calendar"]
    )

    creds = flow.run_local_server(port=8080)

    print("\nAccess Token:", creds.token)
    print("Refresh Token:", creds.refresh_token)

if __name__ == '__main__':
    main()