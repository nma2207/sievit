from gmusicapi import Mobileclient
import ru_tracker_api
import  xlwt
from datetime import datetime

def main():
    api = Mobileclient()

    while api.login('nma2207@gmail.com', '*****************',  Mobileclient.FROM_MAC_ADDRESS) !=True:
        print('.',end='')
    print('True')
    # => True

    library = api.get_all_songs(1000)

    #API к торренту
    tracker = ru_tracker_api.API()

    #создали Эксель
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Sheet 1")

    i=0
    now = datetime.today().date()
    today = str(now.day) + "." + str(now.month) + "." + str(now.year)
    for song in library:
        search = tracker.request(song["singer"], song["name"])

        ws.write(i + 1, 0, song["singer"])
        ws.write(i + 1, 1, song["name"])
        ws.write(i + 1, 2, today)
        ws.write(i + 1, 3, song["date"])
        ws.write(i + 1, 4, song["cost"])
        ws.write(i + 1, 5, search["download_count"])
        ws.write(i + 1, 6, song["genre"])
        ws.write(i + 1, 7, search["duration"])
        ws.write(i + 1, 8, search["size"])
        # ws.write(i + 1, 9, lang)
        ws.write(i + 1, 10, song["rightholder"])
        ws.write(i + 1, 11, search["date"])
        ws.write(i + 1, 12, search["song_count"])
        i+=1


if __name__ == "__main__":
    main()