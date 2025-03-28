# Задача 1. Анализ данных о фильмах

import csv

with open('movies.csv', mode='r', encoding='utf-8', newline = '') as file:
    reader = csv.reader(file)
    header = next(reader)
    movies = [row for row in reader]

total_movies = len(movies)
print('Общее количество фильмов в файле: ', total_movies)

total_box_office_after_2010 = sum(int(movie[4]) for movie in movies if int(movie[1]) > 2010)
print('Суммарные сборы за фильмы, выпущенные после 2010 года: ', total_box_office_after_2010)

highest_grossing_movie = max(movies, key=lambda movie: int(movie[4]))
highest_grossing_name = highest_grossing_movie[0]
highest_grossing_year = highest_grossing_movie[1]
highest_grossing_director = highest_grossing_movie[3]
print('Фильм с самыми высокими сборами: ', highest_grossing_name, highest_grossing_year, highest_grossing_director)

