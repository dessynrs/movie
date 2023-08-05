from modules.db import setup, save_movie, get_all_movie

con, cur = setup()

# ambil inputan dari user
title = input("Masukkan judul film: ")
year = int(input("Masukkan tahun film: "))
score = float(input("Masukkan nilai film: "))

save_movie(title, year, score)

get_all_movie()