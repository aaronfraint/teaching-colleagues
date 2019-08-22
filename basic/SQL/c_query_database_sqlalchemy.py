# # Use `sqlalchemy` to pull data out of SQL into a `pandas` dataframe
#
# You would use this approach over `psycopg2` if you want the query result returned in a `pandas.DataFrame`

import pandas as pd
import sqlalchemy

MY_DB = "teaching_bucket"
UN = "postgres"
PW = "Bunnywithspt54"
HOST = "localhost"
DATA_TABLE = "nyc_stop_frisk_2018"

# Make a database connection with SQLAlchemy
db_uri = f"postgresql://{UN}:{PW}@{HOST}:5432/{MY_DB}"
connection = sqlalchemy.create_engine(db_uri)

# Pull the entire table from SQL into a pandas dataframe
query = f" SELECT * FROM {DATA_TABLE} """
df = pd.read_sql(query, connection)

# Use pandas to do something with the table
summary = df.describe().T
print(summary)

# Close out the SQL connection
connection.dispose()
