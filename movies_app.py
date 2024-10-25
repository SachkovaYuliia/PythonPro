import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect(db_file)
        print("Підключено до бази даних")
    except Error as e:
        print(e)
    return sqlite_connection


def create_tables(sqlite_connection):
    try:
        sqlite_connection.execute('''CREATE TABLE IF NOT EXISTS movies (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        title TEXT NOT NULL,
                                        release_year INTEGER NOT NULL,
                                        genre TEXT NOT NULL)''')

        sqlite_connection.execute('''CREATE TABLE IF NOT EXISTS actors (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        birth_year INTEGER)''')

        sqlite_connection.execute('''CREATE TABLE IF NOT EXISTS movie_cast (
                                        movie_id INTEGER,
                                        actor_id INTEGER,
                                        FOREIGN KEY (movie_id) REFERENCES movies (id),
                                        FOREIGN KEY (actor_id) REFERENCES actors (id))''')

        sqlite_connection.commit()
        print("Таблиці створено успішно.")
    except Error as e:
        print(e)


def add_movie(sqlite_connection, title, release_year, genre, actor_ids):
    """
    Додає новий фільм і зв'язує його з акторами.
    Перевіряє, чи жанр коректний.
    """
    allowed_genres = ["Драма", "Комедія", "Мелодрама", "Пригода", "Наукова фантастика", "Бойовик", "Трилер"]

    if genre not in allowed_genres:
        print(f"Жанр '{genre}' не підтримується. Будь ласка, виберіть жанр зі списку: {', '.join(allowed_genres)}.")
        return

    try:
        sqlite_connection.execute("INSERT INTO movies (title, release_year, genre) VALUES (?, ?, ?)",
                                  (title, release_year, genre))
        sqlite_connection.commit()

        movie_id = sqlite_connection.execute("SELECT id FROM movies WHERE title = ? AND release_year = ?",
                                             (title, release_year)).fetchone()[0]

        for actor_id in actor_ids:
            actor = sqlite_connection.execute("SELECT id FROM actors WHERE id = ?", (actor_id,)).fetchone()
            if actor:
                sqlite_connection.execute("INSERT INTO movie_cast (movie_id, actor_id) VALUES (?, ?)", 
                                          (movie_id, actor_id))
            else:
                print(f"Актор з id {actor_id} не знайдений, пропущено.")

        sqlite_connection.commit()
        print(f"Фільм '{title}' успішно додано з акторами.")
    except Error as e:
        print(f"Сталася помилка при додаванні фільму: {e}")


def add_actor(sqlite_connection, name, birth_year):
    sql = '''INSERT INTO actors(name, birth_year) VALUES (?, ?)'''
    try:
        with sqlite_connection:
            sqlite_connection.execute(sql, (name, birth_year))
        print(f"Актор '{name}' доданий до бази.")
    except Error as e:
        print(e)


def add_actor_to_movie(sqlite_connection, movie_id, actor_id):
    sql = '''INSERT INTO movie_cast(movie_id, actor_id) VALUES (?, ?)'''
    try:
        with sqlite_connection:
            sqlite_connection.execute(sql, (movie_id, actor_id))
        print(f"Актор з id {actor_id} доданий до фільму з id {movie_id}.")
    except Error as e:
        print(e)


def show_movies_with_actors(sqlite_connection):
    sql = '''SELECT movies.title, GROUP_CONCAT(actors.name, ', ') as actors
             FROM movies
             INNER JOIN movie_cast ON movies.id = movie_cast.movie_id
             INNER JOIN actors ON movie_cast.actor_id = actors.id
             GROUP BY movies.id'''
    try:
        cursor = sqlite_connection.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(f"Фільм: {row[0]}, Актори: {row[1]}")
    except Error as e:
        print(e)


def show_unique_genres(sqlite_connection):
    """
    Виводить список унікальних жанрів фільмів.
    """
    sql = '''SELECT DISTINCT genre FROM movies'''
    try:
        cursor = sqlite_connection.execute(sql)
        rows = cursor.fetchall()
        print("Унікальні жанри:")
        for row in rows:
            print(row[0])  
    except Error as e:
        print(e)


def show_movies_count_by_genre(sqlite_connection):
    sql = '''SELECT genre, COUNT(*) FROM movies GROUP BY genre'''
    try:
        cursor = sqlite_connection.execute(sql)
        rows = cursor.fetchall()
        print("Жанри та кількість фільмів:")
        for row in rows:
            print(f"{row[0]}: {row[1]}")
    except Error as e:
        print(e)


def show_avg_birth_year_by_genre(sqlite_connection, genre):
    sql = '''SELECT AVG(actors.birth_year)
             FROM movies
             JOIN movie_cast ON movies.id = movie_cast.movie_id
             JOIN actors ON movie_cast.actor_id = actors.id
             WHERE movies.genre = ?'''
    try:
        cursor = sqlite_connection.execute(sql, (genre,))
        result = cursor.fetchone()[0]
        print(f"Середній рік народження акторів у жанрі {genre}: {result}")
    except Error as e:
        print(e)


def search_movie(sqlite_connection, keyword):
    sql = '''SELECT id, title, release_year FROM movies WHERE title LIKE ?'''
    try:
        cursor = sqlite_connection.execute(sql, ('%' + keyword + '%',))
        rows = cursor.fetchall()
        if rows:
            print("Знайдені фільми:")
            for row in rows:
                print(f"{row[0]}. {row[1]} ({row[2]})")
        else:
            print("Фільми не знайдено.")
    except Error as e:
        print(e)


def show_movies_paginated(sqlite_connection, page_size, page_number):
    offset = (page_number - 1) * page_size
    sql = '''SELECT title FROM movies LIMIT ? OFFSET ?'''
    try:
        cursor = sqlite_connection.execute(sql, (page_size, offset))
        rows = cursor.fetchall()
        print(f"Сторінка {page_number} з {page_size} фільмів:")
        for row in rows:
            print(row[0])
    except Error as e:
        print(e)


def show_all_actors_and_movies(sqlite_connection):
    sql = '''SELECT actors.name, movies.title
             FROM actors
             JOIN movie_cast ON actors.id = movie_cast.actor_id
             JOIN movies ON movie_cast.movie_id = movies.id'''
    try:
        cursor = sqlite_connection.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(f"Актор: {row[0]}, Фільм: {row[1]}")
    except Error as e:
        print(e)


def movie_age(release_year):
    return 2024 - release_year  


def show_movies_with_age(sqlite_connection):
    sql = '''SELECT title, release_year FROM movies'''
    try:
        cursor = sqlite_connection.execute(sql)
        rows = cursor.fetchall()
        print("Фільми з віком:")
        for row in rows:
            print(f"{row[0]} ({row[1]}): {movie_age(row[1])} років")
    except Error as e:
        print(e)


def main():
    database = "kinobaza.db"
    sqlite_connection = create_connection(database)
    if sqlite_connection is not None:
        create_tables(sqlite_connection)

        while True:
            print("""
1. Додати фільм
2. Додати актора
3. Показати всі фільми з акторами
4. Показати унікальні жанри
5. Показати кількість фільмів за жанром
6. Показати середній рік народження акторів у фільмах певного жанру
7. Пошук фільму за назвою
8. Показати фільми (з пагінацією)
9. Показати імена всіх акторів та назви всіх фільмів
10. Показати фільми з віком
11. виправлення
0. Вихід
            """)
            choice = input("Виберіть дію: ")

            if choice == '1':
                title = input("Назва фільму: ")
                release_year = int(input("Рік випуску: "))
                genre = input("Жанр: ")
                
                actor_ids = input("Введіть id акторів, розділені комою: ").split(',')
                actor_ids = [int(actor_id.strip()) for actor_id in actor_ids]  
                
                add_movie(sqlite_connection, title, release_year, genre, actor_ids)

            elif choice == '2':
                name = input("Ім'я актора: ")
                birth_year = int(input("Рік народження: "))
                add_actor(sqlite_connection, name, birth_year)

            elif choice == '3':
                show_movies_with_actors(sqlite_connection)

            elif choice == '4':
                show_unique_genres(sqlite_connection)

            elif choice == '5':
                show_movies_count_by_genre(sqlite_connection)

            elif choice == '6':
                genre = input("Введіть жанр: ")
                show_avg_birth_year_by_genre(sqlite_connection, genre)

            elif choice == '7':
                keyword = input("Введіть ключове слово для пошуку: ")
                search_movie(sqlite_connection, keyword)

            elif choice == '8':
                page_size = int(input("Кількість фільмів на сторінку: "))
                page_number = int(input("Номер сторінки: "))
                show_movies_paginated(sqlite_connection, page_size, page_number)

            elif choice == '9':
                show_all_actors_and_movies(sqlite_connection)

            elif choice == '10':
                show_movies_with_age(sqlite_connection)

            elif choice == '0':
                print("Вихід...")
                break
            else:
                print("Невірна команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
