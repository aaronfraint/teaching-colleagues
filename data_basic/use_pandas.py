# # Use the `pandas` module to access data from a variety of sources
#
# In this example we're fetching a `.xlsx` file from the web, but you can also load `.csv` and other file types from disk.

import pandas as pd

# ## Define a URL or filepath and use `pd.read_csv()` or `pd.read_excel()`

url = 'https://www1.nyc.gov/assets/nypd/downloads/excel/analysis_and_planning/stop-question-frisk/sqf-2018.xlsx'
df = pd.read_excel(url)

# ## Once you've created a dataframe you can use any `pandas` operation on it

# Take the first 5 rows of the table and then "T"ranspose it 90 degrees for a preview of the rows/cols in the table
df.head().T
