-- prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
SELECT table_name, column_name, column_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
