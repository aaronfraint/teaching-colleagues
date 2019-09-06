# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Parse pedestrian volumes from an Excel-based Turning Movement Count
#
# We have a folder full of Excel count data and companion PDFs. We need to parse each one to pull out a Pedestrian-specific volume number that we can then use to scale point sizes on a GIS map.
#
# Things to note:
# - Data does not start on Row 1
# - There are typically 4 columns with Ped data, but there could be non-standard intersections with more or fewer legs
#
# ### Use jupyter to prototype a solution:

# +
import pandas as pd
import os
import csv


data_folder = r"C:\Egnyte\Shared\PROJECTS\2018\00-2018-205 Santa Clara CA Pedestrian Master Plan\Products\Counts\Count Reports 6-17-19"
test_file = os.path.join(data_folder, "1 LICK MILL BLVD & TASMAN DR.xls")
# -

# Read the file starting at line 10
df = pd.read_excel(test_file, sheet_name="Vehicles", header=9)

# +
#rename the Start Time column to start_time, and convert the times to hours, since that's all we need for the buckets
df.rename(columns = {'Start Time':'start_time'}, inplace = True)
df['start_time'] = pd.to_datetime(df['start_time']).dt.hour

print(df['start_time'])


# +
# Make variables that will hold the totals across all "Peds" columns
running_total = 0
morning_peak = 0
midday = 0
evening_peak = 0

# Get a list of all "Peds" column names
ped_cols = [x for x in df.columns if "Peds" in x]

# +
# For each column, get the sum and add it to the running total
for col in ped_cols:
    col_total = df[col].sum()

    running_total += col_total
        
print(running_total)

# +
# For each column, get the sum of hours within a given time bucket

MORNING_START = 7
MORNING_END = 9

for col in ped_cols:
    
    filtered_df = df.loc[(df['start_time'] >= MORNING_START) & (df['start_time'] <= MORNING_END)]
    
    col_total = filtered_df[col].sum()
                                   
    morning_peak += col_total
        
print(morning_peak)


# -

# ### Once you have a working solution, compartmentalize it within a function:

# +
# Now do all the above as a function

def get_ped_total(excel_count_file):

    # This dictionary defines a set of time bucket names and their start/end hours
    time_buckets = [
        ("am_peak", 7, 10),
        ("midday", 11, 14),
        ("pm_peak", 15, 18)
    ]
    
    # Read the file starting at line 10
    df = pd.read_excel(excel_count_file, sheet_name="Vehicles", header=9)
    
    #rename the Start Time column to start_time
    df.rename(columns = {'Start Time':'start_time'}, inplace = True)
    
    #convert the times to hours, since that's all we need for the buckets
    df['start_time'] = pd.to_datetime(df['start_time']).dt.hour

    # Make variables that will hold the totals (for different time buckets) across all "Peds" columns
    totals = {
        "daily": 0,
        "am_peak": 0,
        "midday": 0,
        "pm_peak": 0
    }
    
    # Get a list of all "Peds" column names
    ped_cols = [x for x in df.columns if "Peds" in x]

    # For each column, get the sum and add it to the daily total
    for col in ped_cols:

        # Get the daily total
        col_total = df[col].sum()

        totals["daily"] += col_total
        
        # parse out a few time buckets (i.e. AM peak, midday, PM peak)
        for bucket_name, start_hour, end_hour in time_buckets:
            
            # filtered the dataframe to this bucket's start/end hours
            filtered_df = df.loc[(df['start_time'] >= start_hour) & (df['start_time'] <= end_hour)]

            # Sum the filtered table and add to the appropriate total key
            bucket_total = filtered_df[col].sum()
            totals[bucket_name] += bucket_total
            
    return totals


# -

# ### Now we're ready to iterate over all Excel files and pull results out

# +
results = []
results.append( ["joinid", "location", "ped_vol"] )

for f in os.listdir(data_folder):
    if f[-4:] == ".xls":

        # Get info about location for summary table
        text_list = f.split(" ")
        location_id = text_list[0]
        place_name = " ".join(text_list[1:]).replace(".xls", "")

        xls_path = os.path.join(folder_path, f)
        totals = get_ped_total(xls_path)
        daily = totals["daily"]

        results.append( [location_id, place_name, daily] )
# -

# ### Write the results to CSV file using the ``csv`` module

# +
output = os.path.join(data_folder, "test_output.csv")

with open(output, "w", newline='') as csvfile:

    writer = csv.writer(csvfile)
    for row in results:
        writer.writerow(row)
