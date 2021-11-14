from __future__ import print_function
import os.path
from django.core.management.base import BaseCommand
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from wildlife.models import Critter

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


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
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
        fish_created_count = 0
        fish_updated_count = 0

        if not fish_values:
            print("No fish data found.")
        else:
            for row in fish_values:
                obj, created = Critter.objects.update_or_create(
                    name=row[1],
                    critter_type=Critter.FISH,
                    icon_uri=row[2].split('"')[1],
                    image_uri=row[3].split('"')[1],
                    bells_sell=int(row[5]),
                    source=row[6],
                    shadow_size=row[7],
                    difficulty=row[8],
                    vision=row[9],
                    catches_to_unlock=int(row[10]),
                    spawn_rates=row[11],
                    nh_jan=row[12],
                    nh_feb=row[13],
                    nh_mar=row[14],
                    nh_apr=row[15],
                    nh_may=row[16],
                    nh_jun=row[17],
                    nh_jul=row[18],
                    nh_aug=row[19],
                    nh_sep=row[20],
                    nh_oct=row[21],
                    nh_nov=row[22],
                    nh_dec=row[23],
                    sh_jan=row[24],
                    sh_feb=row[25],
                    sh_mar=row[26],
                    sh_apr=row[27],
                    sh_may=row[28],
                    sh_jun=row[29],
                    sh_jul=row[30],
                    sh_aug=row[31],
                    sh_sep=row[32],
                    sh_oct=row[33],
                    sh_nov=row[34],
                    sh_dec=row[35],
                    description=row[38],
                    ueid=row[49]
                )
                if(created):
                    fish_created_count += 1
                else:
                    fish_updated_count += 1
                obj.save()
            print("Fish: {} created and  {} updated".format(
                fish_created_count, fish_updated_count))

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
        bugs_created_count = 0
        bugs_updated_count = 0

        if not bugs_values:
            print("No bugs data found.")
        else:
            for row in bugs_values:
                obj, created = Critter.objects.update_or_create(
                    name=row[1],
                    critter_type=Critter.BUG,
                    icon_uri=row[2].split('"')[1],
                    image_uri=row[3].split('"')[1],
                    bells_sell=int(row[5]),
                    source=row[6],
                    weather=row[7],
                    catches_to_unlock=int(row[8]),
                    spawn_rates=row[9],
                    nh_jan=row[10],
                    nh_feb=row[11],
                    nh_mar=row[12],
                    nh_apr=row[13],
                    nh_may=row[14],
                    nh_jun=row[15],
                    nh_jul=row[16],
                    nh_aug=row[17],
                    nh_sep=row[18],
                    nh_oct=row[19],
                    nh_nov=row[20],
                    nh_dec=row[21],
                    sh_jan=row[22],
                    sh_feb=row[23],
                    sh_mar=row[24],
                    sh_apr=row[25],
                    sh_may=row[26],
                    sh_jun=row[27],
                    sh_jul=row[28],
                    sh_aug=row[29],
                    sh_sep=row[30],
                    sh_oct=row[31],
                    sh_nov=row[32],
                    sh_dec=row[33],
                    description=row[36],
                    ueid=row[46]
                )
                if(created):
                    bugs_created_count += 1
                else:
                    bugs_updated_count += 1
                obj.save()
            print("Bugs: {} created and  {} updated".format(
                bugs_created_count, bugs_updated_count))

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
        sea_created_count = 0
        sea_updated_count = 0

        if not sea_values:
            print("No sea creature data found.")
        else:
            for row in sea_values:
                obj, created = Critter.objects.update_or_create(
                    name=row[1],
                    critter_type=Critter.SEA,
                    icon_uri=row[2].split('"')[1],
                    image_uri=row[3].split('"')[1],
                    bells_sell=int(row[5]),
                    shadow_size=row[6],
                    difficulty=row[7],
                    catches_to_unlock=int(row[8]),
                    spawn_rates=row[9],
                    nh_jan=row[10],
                    nh_feb=row[11],
                    nh_mar=row[12],
                    nh_apr=row[13],
                    nh_may=row[14],
                    nh_jun=row[15],
                    nh_jul=row[16],
                    nh_aug=row[17],
                    nh_sep=row[18],
                    nh_oct=row[19],
                    nh_nov=row[20],
                    nh_dec=row[21],
                    sh_jan=row[22],
                    sh_feb=row[23],
                    sh_mar=row[24],
                    sh_apr=row[25],
                    sh_may=row[26],
                    sh_jun=row[27],
                    sh_jul=row[28],
                    sh_aug=row[29],
                    sh_sep=row[30],
                    sh_oct=row[31],
                    sh_nov=row[32],
                    sh_dec=row[33],
                    description=row[36],
                    ueid=row[49]
                )
                if(created):
                    sea_created_count += 1
                else:
                    sea_updated_count += 1
                obj.save()
            print("Sea creatures: {} created and  {} updated".format(
                sea_created_count, sea_updated_count))

        # # --- update fossils ---
        # fossils_sheet = (
        #     sheet.values()
        #     .get(
        #         spreadsheetId=SPREADSHEET_ID,
        #         valueRenderOption="FORMULA",
        #         range=FOSSILS_SHEET_RANGE,
        #     )
        #     .execute()
        # )
        # fossils_values = fossils_sheet.get("values", [])

        # if not fossils_values:
        #     print("No fossils data found.")
        # else:
        #     for row in fossils_values:
        #         print(row[0])

        # # --- update art ---
        # art_sheet = (
        #     sheet.values()
        #     .get(
        #         spreadsheetId=SPREADSHEET_ID,
        #         valueRenderOption="FORMULA",
        #         range=ART_SHEET_RANGE,
        #     )
        #     .execute()
        # )
        # art_values = art_sheet.get("values", [])

        # if not art_values:
        #     print("No art data found.")
        # else:
        #     for row in art_values:
        #         print(row[0])

        # # --- update gyroids ---
        # gyroids_sheet = (
        #     sheet.values()
        #     .get(
        #         spreadsheetId=SPREADSHEET_ID,
        #         valueRenderOption="FORMULA",
        #         range=GYROIDS_SHEET_RANGE,
        #     )
        #     .execute()
        # )
        # gyroids_values = gyroids_sheet.get("values", [])

        # if not gyroids_values:
        #     print("No gyroids data found.")
        # else:
        #     for row in gyroids_values:
        #         print(row[0])

        # # --- update gyroids ---
        # songs_sheet = (
        #     sheet.values()
        #     .get(
        #         spreadsheetId=SPREADSHEET_ID,
        #         valueRenderOption="FORMULA",
        #         range=SONGS_SHEET_RANGE,
        #     )
        #     .execute()
        # )
        # songs_values = songs_sheet.get("values", [])

        # if not songs_values:
        #     print("No songs data found.")
        # else:
        #     for row in songs_values:
        #         print(row[0])
