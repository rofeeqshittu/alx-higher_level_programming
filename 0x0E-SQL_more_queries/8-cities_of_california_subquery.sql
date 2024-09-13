-- A script that list the cities of California that can be found in the database hbtn_0d_usa

-- use table
-- USE hbtn_0d_usa;

-- List all cities of California, sorted by id in asc order
SELECT cities.name
FROM cities
WHERE name=California
ORDER BY cities.id ASC;
