# א:
# SELECT tourists. *, tours.* FROM tourists
# CROSS JOIN tours;

# ב:
# SELECT *  FROM tourists
# WHERE tour_id is NULL;
# DELETE FROM tourists
# WHERE tour_id IS NULL;


# ג:
# SELECT tours.*
# FROM tours
# LEFT OUTER JOIN tourists ON tours.id = tourists.tour_id
# WHERE tourists.tour_id IS NULL;
# UPDATE tours
# SET start_date = DATE(start_date, '+1 year'), end_date = DATE(end_date, '+1 year')
# WHERE id IN (
#     SELECT tours.id
#     FROM tours
#     LEFT OUTER JOIN tourists ON tours.id = tourists.tour_id
#     WHERE tourists.tour_id IS NULL
# );

# ד:
# SELECT  count(*) as tours_amount
# FROM tours
# LEFT OUTER JOIN tourists ON tours.id = tourists.tour_id
# WHERE tourists.tour_id IS NULL;

# ה:
# SELECT * FROM tourists
# FULL JOIN tours ON tourists.tour_id = tours.id;

# ו:
# SELECT * FROM tourists
# INNER JOIN countries ON tourists.country_id = countries.id;

# ז:
# SELECT * FROM tourists
# FULL JOIN tours ON tourists.tour_id = tours.id
# WHERE tourists.tour_id NOT NULL;

# ח:
# SELECT tourists.*, tours.*
# FROM tourists
# LEFT JOIN tours ON tourists.tour_id = tours.id
# UNION
# SELECT tourists.*, tours.*
# FROM tourists
# RIGHT JOIN tours ON tourists.tour_id = tours.id;
