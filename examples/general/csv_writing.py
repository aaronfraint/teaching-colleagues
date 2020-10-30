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

# # Using the ``csv`` module to write to disk

import csv

# +
# Let's define a list of lists, which we will then write to disk
# Notice the header list at the beginning, and the subsequent data lists below

data = [
    ["id", "location", "square_feet"],
    [1, "Alta Sacramento", 1000],
    [2, "Alta Oakland", 5000],
    [3, "Alta Seattle", 3500]
]

# +
# Write the result to a .csv file

output_csv = r"files\outputs\test_writing_csv.csv"

with open(output_csv, "w", newline='') as csvfile:

    writer = csv.writer(csvfile)
    for row in data:
        writer.writerow(row)
# -

# ## Use your file browser to find and open ``test_writing_csv.csv``
#
# #### Confirm that it matches the ``data`` variable defined in this script
