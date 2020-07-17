# import keyboard
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pytchat import LiveChat
livechat = LiveChat(video_id = "hMvmbGy3qq8")

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Spreadsheetapi-03009ddbdc6b.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Rekap Soal Webinar").sheet1

data = sheet.get_all_records()

print(data)
print(livechat.is_alive())

count = len(data)
while livechat.is_alive():
    chatdata = livechat.get()
        # print("live")
    for c in chatdata.items:
        print(f"{c.datetime} [{c.author.name}]- {c.message}")

        value = c.message
        if value.count("#") >= 3:
            values = value.split("#")
            sheet.insert_row(values, count + 2)
            print("berhasil ditambah")
            print("count " + str(count))
            count += 1   
        


