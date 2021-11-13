from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = "13d_LAJPlxMa_DubPTuirkIV4DERBMXbrWQsmSh8ReK4"
FISH_SHEET_RANGE = "Fish!2:81"
BUGS_SHEET_RANGE = "Insects!2:81"
SEA_SHEET_RANGE = "Sea Creatures!2:41"
FOSSILS_SHEET_RANGE = "Fossils!2:74"
ART_SHEET_RANGE = "Art!2:71"
GYROIDS_SHEET_RANGE = "Gyroids!2:190"
SONGS_SHEET_RANGE = "Music!2:111"


def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES)
            creds = flow.run_local_server(port=64049)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    # --- update fish ---
    fish_sheet = (
        sheet.values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            valueRenderOption="FORMULA",
            range=FISH_SHEET_RANGE,
        )
        .execute()
    )
    fish_values = fish_sheet.get("values", [])

    if not fish_values:
        print("No fish data found.")
    else:
        for row in fish_values:
            print(row[1])

    # --- update bugs ---
    bugs_sheet = (
        sheet.values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            valueRenderOption="FORMULA",
            range=BUGS_SHEET_RANGE,
        )
        .execute()
    )
    bugs_values = bugs_sheet.get("values", [])

    if not bugs_values:
        print("No bugs data found.")
    else:
        for row in bugs_values:
            print(row[1])

    # --- update sea creatures ---
    sea_sheet = (
        sheet.values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            valueRenderOption="FORMULA",
            range=SEA_SHEET_RANGE,
        )
        .execute()
    )
    sea_values = sea_sheet.get("values", [])

    if not sea_values:
        print("No sea creature data found.")
    else:
        for row in sea_values:
            print(row[1])

    # --- update fossils ---
    fossils_sheet = (
        sheet.values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            valueRenderOption="FORMULA",
            range=FOSSILS_SHEET_RANGE,
        )
        .execute()
    )
    fossils_values = fossils_sheet.get("values", [])

    if not fossils_values:
        print("No fossils data found.")
    else:
        for row in fossils_values:
            print(row[0])

    # --- update art ---
    art_sheet = (
        sheet.values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            valueRenderOption="FORMULA",
            range=ART_SHEET_RANGE,
        )
        .execute()
    )
    art_values = art_sheet.get("values", [])

    if not art_values:
        print("No art data found.")
    else:
        for row in art_values:
            print(row[0])

    # --- update gyroids ---
    gyroids_sheet = (
        sheet.values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            valueRenderOption="FORMULA",
            range=GYROIDS_SHEET_RANGE,
        )
        .execute()
    )
    gyroids_values = gyroids_sheet.get("values", [])

    if not gyroids_values:
        print("No gyroids data found.")
    else:
        for row in gyroids_values:
            print(row[0])

    # --- update gyroids ---
    songs_sheet = (
        sheet.values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            valueRenderOption="FORMULA",
            range=SONGS_SHEET_RANGE,
        )
        .execute()
    )
    songs_values = songs_sheet.get("values", [])

    if not songs_values:
        print("No songs data found.")
    else:
        for row in songs_values:
            print(row[0])


if __name__ == "__main__":
    main()
