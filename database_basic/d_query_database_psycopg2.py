# # Use `psycopg2` to get information out of SQL
#
# You would choose this approach over `sqlalchemy` if you don't need the result inside a dataframe object.

import psycopg2

MY_DB = "teaching_bucket"
UN = "postgres"
PW = "Bunnywithspt54"
HOST = "localhost"

# You can use psycopg2 to execute a query and operate on the results
db_uri = f"postgresql://{UN}:{PW}@{HOST}:5432/{MY_DB}"
connection = psycopg2.connect(db_uri)
cursor = connection.cursor()

# +
# Query the total number of stops and those that found a weapon
query_total_stops = " SELECT COUNT(stop_frisk_id) FROM nyc_stop_frisk_2018 "
query_weapon_stops = f" {query_total_stops} WHERE weapon_found_flag = 'Y' "

# Execute each query and extract the results
cursor.execute(query_total_stops)
total_result = cursor.fetchone()

cursor.execute(query_weapon_stops)
weapon_result = cursor.fetchone()
# -

# The .fetchone() result gives you a tuple, so you must slice into the first element
total = total_result[0]
weapons_found = weapon_result[0]

# Use basic python to get the percentage of stops that resulted in the officer finding a gun
percent_with_weapons = float(weapons_found) / float(total) * 100
percent_without_weapons = 100 - percent_with_weapons
percent_without_weapons = round(percent_without_weapons, 2)

# Use this information to write a message out to the user
message = f"In 2018 the NYPD stopped {total} people and found weapons in {weapons_found} cases."
message += f"\nIn other words, {percent_without_weapons}% of the stops did not result in an officer finding a weapon."

print(message)

# Close out your database connections
cursor.close()
connection.close()
