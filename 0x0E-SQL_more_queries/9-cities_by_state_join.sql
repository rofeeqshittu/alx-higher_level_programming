-- Lists all cities contained in the database hbtn_0d_usa

USE hbtn_0d_1;

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.states_id = states.id;
ORDER BY cities.id ASC;
