---

# SQL - More Queries

This repository contains a series of SQL scripts aimed at exploring more advanced querying techniques in MySQL. These exercises are part of the software engineering curriculum designed to deepen understanding of SQL and database management.

## Table of Contents

- [Tasks](#tasks)
- [Author](#author)


## Tasks

### 0. My privileges!
Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).

### 1. Root user
Write a script that creates the MySQL server user `user_0d_1` with all privileges and password `user_0d_1_pwd`.

### 2. Read user
Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2` with SELECT privilege on this database and password `user_0d_2_pwd`.

### 3. Always a name
Write a script that creates the table `force_name` with `id` as INT and `name` as VARCHAR(256) and cannot be null.

### 4. ID can't be null
Write a script that creates the table `id_not_null` with `id` as INT default 1 and `name` as VARCHAR(256).

### 5. Unique ID
Write a script that creates the table `unique_id` with `id` as INT default 1 and must be unique and `name` as VARCHAR(256).

### 6. States table
Write a script that creates the database `hbtn_0d_usa` and the table `states` with `id` as INT unique, auto generated, and primary key, and `name` as VARCHAR(256) not null.

### 7. Cities table
Write a script that creates the table `cities` with `id` as INT unique, auto generated, and primary key, `state_id` as INT not null and a FOREIGN KEY referencing `states(id)`, and `name` as VARCHAR(256) not null.

### 8. Cities of California
Write a script that lists all the cities of California in the database `hbtn_0d_usa` without using JOIN keyword.

### 9. Cities by States
Write a script that lists all cities in the database `hbtn_0d_usa` showing `cities.id`, `cities.name`, and `states.name`.

### 10. Genre ID by show
Write a script that lists all shows in `hbtn_0d_tvshows` that have at least one genre linked, showing `tv_shows.title` and `tv_show_genres.genre_id`.

### 11. Genre ID for all shows
Write a script that lists all shows in `hbtn_0d_tvshows` showing `tv_shows.title` and `tv_show_genres.genre_id`, including shows without a genre.

### 12. No genre
Write a script that lists all shows in `hbtn_0d_tvshows` without any genre linked.

For more detailed information, refer to the task descriptions provided within each SQL script file.

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/alx-higher_level_programming.git
    ```
2. Navigate to the project directory:
    ```sh
    cd alx-higher_level_programming/0x0E-SQL_more_queries
    ```
3. Run the SQL scripts using MySQL:
    ```sh
    cat [script_name].sql | mysql -hlocalhost -uroot -p
    ```

## Author

[Rofeeq Shittu](https://github.com/rofeeqshittu)

---
