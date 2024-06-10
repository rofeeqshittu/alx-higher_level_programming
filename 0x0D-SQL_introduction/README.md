---

# 0x0D. SQL - Introduction

## Description
This project is part of the "SE Foundations" curriculum and covers the basics of SQL using MySQL. The aim is to understand the fundamentals of databases, especially relational databases, and how to interact with them using SQL.

## Concepts Covered
- Databases
- Relational databases
- SQL (Structured Query Language)
- MySQL


## SQL Comments Example
```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

## MySQL Installation Instructions
### Install MySQL 8.0 on Ubuntu 20.04 LTS
```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
# Output should be something like:
# mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

### Connect to MySQL server
```bash
$ sudo mysql
# You should see the MySQL monitor prompt
mysql> quit
Bye
```

### Using “container-on-demand” to run MySQL
- Request an Ubuntu 20.04 container
- Connect via SSH or Web terminal
- Start MySQL before using it:
```bash
$ service mysql start
# Starting MySQL database server mysqld
```

## Tasks
### 0. List databases
- **File:** `0-list_databases.sql`
- **Description:** Write a script that lists all databases of your MySQL server.

### 1. Create a database
- **File:** `1-create_database_if_missing.sql`
- **Description:** Write a script that creates the database `hbtn_0c_0` in your MySQL server.

### 2. Delete a database
- **File:** `2-remove_database.sql`
- **Description:** Write a script that deletes the database `hbtn_0c_0` in your MySQL server.

### 3. List tables
- **File:** `3-list_tables.sql`
- **Description:** Write a script that lists all the tables of a database in your MySQL server. The database name will be passed as an argument.

### 4. First table
- **File:** `4-first_table.sql`
- **Description:** Write a script that creates a table called `first_table` in the current database in your MySQL server.

### 5. Full description
- **File:** `5-full_table.sql`
- **Description:** Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0`.

### 6. List all in table
- **File:** `6-list_values.sql`
- **Description:** Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0`.

### 7. First add
- **File:** `7-insert_value.sql`
- **Description:** Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`).

### 8. Count 89
- **File:** `8-count_89.sql`
- **Description:** Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0`.

### 9. Full creation
- **File:** `9-full_creation.sql`
- **Description:** Write a script that creates a table `second_table` in the database `hbtn_0c_0` and add multiple rows.

### 10. List by best
- **File:** `10-top_score.sql`
- **Description:** Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` ordered by score (top first).

### 11. Select the best
- **File:** `11-best_score.sql`
- **Description:** Write a script that lists all records with a score >= 10 in the table `second_table` of the database `hbtn_0c_0` ordered by score (top first).

### 12. Cheating is bad
- **File:** `12-no_cheating.sql`
- **Description:** Write a script that updates the score of `Bob` to 10 in the table `second_table`.

### 13. Score too low
- **File:** `13-change_class.sql`
- **Description:** Write a script that removes all records with a score <= 5 in the table `second_table`.

### 14. Average
- **File:** `14-average.sql`
- **Description:** Write a script that computes the score average of all records in the table `second_table`.

### 15. Number by score
- **File:** `15-groups.sql`
- **Description:** Write a script that lists the number of records with the same score in the table `second_table`.

### 16. Say my name
- **File:** `16-no_link.sql`
- **Description:** Write a script that lists all records of the table `second_table` without listing rows without a name value.

## Repository Structure
```markdown
.
├── 0-list_databases.sql
├── 1-create_database_if_missing.sql
├── 2-remove_database.sql
├── 3-list_tables.sql
├── 4-first_table.sql
├── 5-full_table.sql
├── 6-list_values.sql
├── 7-insert_value.sql
├── 8-count_89.sql
├── 9-full_creation.sql
├── 10-top_score.sql
├── 11-best_score.sql
├── 12-no_cheating.sql
├── 13-change_class.sql
├── 14-average.sql
├── 15-groups.sql
├── 16-no_link.sql
└── README.md
```

## License
© 2024 ALX, All rights reserved.

---
