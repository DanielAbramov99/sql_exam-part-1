# א:
# SELECT sum(revenue) as total_grossed,year FROM movies
# GROUP by year;

# ב:
# SELECT count(movie_name) as movies_amount, language FROM movies
# GROUP by language;

# ג:
# SELECT avg(revenue) as average_grossed, genre FROM movies
# GROUP by genre;

# ד:
# SELECT avg(revenue) as average_grossed, genre,language FROM movies
# GROUP by genre,language;

# ה:
# SELECT language,count(movie_name) AS movie_amount FROM movies
# GROUP by language
# HAVING movie_amount >= 3;

# ו:
# SELECT country, count(movie_name) AS movie_amount FROM movies
# GROUP by country
# ORDER by movie_amount DESC
# LIMIT 1;

# ז:
# select count(movie_name) AS movie_amount, genre FROM movies
# GROUP by genre
# ORDER by movie_amount DESC;

# ט:
# SELECT year, sum(revenue) as total_grossed FROM movies
# GROUP by year
# having total_grossed > 1000;

# י:
# SELECT language, count(movie_name) AS movie_amount FROM movies
# GROUP by language
# ORDER by movie_amount ASC
# LIMIT 1;

# יא:
# SELECT genre, count(movie_name) AS movie_amount FROM movies
# GROUP by genre
# HAVING movie_amount > 2;
