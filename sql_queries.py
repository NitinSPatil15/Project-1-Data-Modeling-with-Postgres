# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
songplay_id varchar not null, 
start_time bigint, 
user_id int not null, 
level text, 
song_id varchar, 
artist_id varchar, 
session_id int, 
location text, 
user_agent varchar
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
user_id int primary key, 
first_name text not null, 
last_name text not null, 
gender char, 
level text
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
song_id varchar primary key, 
title text not null, 
artist_id varchar, 
year int, 
duration real
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
artist_id varchar primary key, 
artist_name text not null, 
artist_location text, 
artist_latitude real, 
artist_longitude real
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
start_time bigint not null, 
hour int, 
day int, 
week int, 
month int, 
year int, 
weekday int
)
""")
