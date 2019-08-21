# # Make a SQL database using `psycopg2`
#
# When you make a database in SQL, you have to execute the command from within a database that already exists.
# By default every PgSQL cluster has a database named `postgres`, so in the code below we connect to that database
# before issuing the command to create the new database named in the `MY_DB` variable.
#
# ### Notes:
# - If the database already exists, this will fail with a `DuplicateDatabase` error
# - This only creates a basic database, it does not enable PostGIS

import psycopg2

MY_DB = "teaching_bucket"
UN = "postgres"
PW = "Bunnywithspt54"
HOST = "localhost"

# Connect to the postgres database
db_uri = f"postgresql://{UN}:{PW}@{HOST}:5432/postgres"
connection = psycopg2.connect(db_uri)
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()

# Execute the CREATE command
query_to_make_db = f"CREATE DATABASE {MY_DB};"
cursor.execute(query_to_make_db)

# Commit and close the database connection
cursor.close()
connection.commit()
connection.close()
