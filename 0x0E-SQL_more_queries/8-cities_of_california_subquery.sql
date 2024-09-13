-- A script that list the cities of California that can be found in the database hbtn_0d_usa

-- use table
-- USE hbtn_0d_usa;

-- List all cities of California, sorted by id in asc order
SELECT id, cities.name
FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
