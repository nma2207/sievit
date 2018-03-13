#encoding: utf-8
import xlwt
import random
from datetime import datetime
def main():
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Sheet 1")
    group_list = ['Bi-2', "AC/DC", "deadmau5", "Nogu svelo", "Nickelback", "Rammstein", "Evan Blum", "Buzova", "Leningrad", "Basta", "Marun", "Years & Years", "Loboda"]
    group_count = len(group_list)
    album_names = ["Ona ne bointsa", "Roskstar", "despasito", "MInimal", "Woyaj", "La-la", "girl", "boy", "Nossa", "Tall", "Abada", "Kedavra", "Strong", "Car", "Horizont", "Herz", "Azat"]
    album_count = len(album_names)

    genre_list = ["rock", "pop", "electro", "rap", "bluz", "jazz"]
    genre_count = len(genre_list)

    lang_list = ["ru", "en", "tt"]
    lang_count = len(lang_list)
    for i in range(1000):
        #0
        group = group_list[random.randint(0,group_count-1 )]
        #1
        album_name = album_names[random.randint(0,album_count-1 )]
        #2
        now = datetime.today().date()
        today = str(now.day)+"."+str(now.month)+"."+str(now.year)
        #3
        reliz_date = random.randint(1970, 2017)
        #4
        cost = random.randint(50,150)
        #5
        download_count = random.randint(500, 15000)
        #6
        genre = genre_list[random.randint(0,genre_count-1 )]
        #7
        duration = random.randint(40,60)
        #8
        size = random.randint(200,1500)
        #9
        lang = lang_list[random.randint(0,lang_count-1 )]
        #10 правообладатель, пусть группа булет
        rightholder = group
        #11
        torrent_reliz_time = random.randint(reliz_date, 2017)
        #12
        song_count = random.randint(10,15)


        ws.write(i+1,0, group)
        ws.write(i + 1, 1, album_name)
        ws.write(i + 1, 2, today)
        ws.write(i + 1, 3, reliz_date)
        ws.write(i + 1, 4, cost)
        ws.write(i + 1, 5, download_count)
        ws.write(i + 1, 6, genre)
        ws.write(i + 1, 7, duration)
        ws.write(i + 1, 8, size)
        #ws.write(i + 1, 9, lang)
        ws.write(i + 1, 10, rightholder)
        ws.write(i + 1, 11, torrent_reliz_time)
        ws.write(i + 1, 12, song_count)

    wb.save('xl_rec.xls')


if __name__ == "__main__":
    main()