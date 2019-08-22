# # Save a `pandas` dataframe to SQL with `sqlalchemy`
#
# We will: 
# - make a dataframe from a hosted Excel file
# - set all column names to lowercase
# - write to the database

import pandas as pd
import sqlalchemy

MY_DB = "teaching_bucket"
UN = "postgres"
PW = "Bunnywithspt54"
HOST = "localhost"

# Make a pandas dataframe from a file
url = 'https://www1.nyc.gov/assets/nypd/downloads/excel/analysis_and_planning/stop-question-frisk/sqf-2018.xlsx'
df = pd.read_excel(url)

# Make a database connection with SQLAlchemy
db_uri = f"postgresql://{UN}:{PW}@{HOST}:5432/{MY_DB}"
connection = sqlalchemy.create_engine(db_uri)

# Clean up the dataframe before writing to SQL
# For example, SQL column names may not use capital letter
df.columns = [x.lower() for x in df.columns]

# Write the dataframe to the database and then dispose the connection
df.to_sql("nyc_stop_frisk_2018", connection, if_exists="replace")
connection.dispose()
