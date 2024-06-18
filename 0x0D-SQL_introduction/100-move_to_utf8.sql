-- Use the hbtn_0c_0 database
USE hbtn_0c_0;

-- Convert the entire database hbtn_0c_0 to UTF-8 (utf8mb4)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table first_table to UTF-8 (utf8mb4)
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

