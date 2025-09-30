# What is a DataFrame?

# A DataFrame is:
# 2-dimensional (rows × columns) data structure
# Labeled (rows have index, columns have names)
# Heterogeneous (columns can have different data types → string, int, float, datetime, etc.)
# Similar to a SQL table or Excel sheet
# Provided by the pandas library in Python


'''
Why is DataFrame Important?
#################################################################
Almost all data analysis & machine learning pipelines start with DataFrames.
It’s the bridge between raw data (CSV, DB, JSON, Excel) and advanced ML libraries 
(like scikit-learn, PyTorch, TensorFlow).

A DataFrame = a smart Excel sheet inside Python with tools for filtering, 
grouping, aggregating, and cleaning data.
'''

import pandas as pd
# Create a DataFrame from a dictionary
# The dictionary contains sample data
# Each key represents a column in the DataFrame
# Each value is a list of entries for that column
# The DataFrame will have three columns: Name, Age, and City
# Each column will have three entries
# Finally, print the DataFrame and calculate the average age

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Delhi", "Mumbai", "Bangalore"],
    "Salary": [70000, 80000, 90000]
}

df = pd.DataFrame(data) 
'''
Add code to print the DataFrame and calculate the average age.

'''
print(df)

print("\nAverage Age:", df["Age"].mean())

# explain the code
'''
1. We import the pandas library and alias it as pd.
2. We create a dictionary named data with three keys: "Name", "Age", and "City". Each key has a list of values.
3. We create a DataFrame named df using pd.DataFrame(data), which converts the dictionary into a tabular format.
4. We print the DataFrame to the console.
5. We calculate the average age by accessing the "Age" column of the DataFrame and using the mean()
    method, then print the result.
'''


# ============================
# PANDAS DATAFRAME CHEAT SHEET
# ============================

# 1. Creating a DataFrame:
# ------------------------
# From dictionary
# df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})

# # From list of dicts
# df = pd.DataFrame([{"Name":"Alice","Age":25}, {"Name":"Bob","Age":30}])

# # From 2D list
# df = pd.DataFrame([["Alice",25],["Bob",30]], columns=["Name","Age"])

# From CSV
# df = pd.read_csv("data.csv")

# 2. Viewing Data:
# ----------------
df.head()       # First 5 rows
df.tail(3)      # Last 3 rows
df.shape        # (rows, columns)
df.info()       # Data types and non-null info
df.describe()   # Stats of numeric columns

# 3. Selecting Data:
# ------------------
df["Name"]          # Single column (Series)
df[["Name","Age"]]  # Multiple columns (DataFrame)
df.iloc[0]          # Row by index
df.loc[1]           # Row by label (index)

# 4. Filtering Data:
# ------------------
df[df["Age"] > 28]          # Age > 28
df[df["City"] == "Delhi"]   # City = Delhi

# 5. Adding / Modifying Columns:
# ------------------------------
df["Age+5"] = df["Age"] + 5

# 6. Sorting:
# -----------
df.sort_values("Age")                  # ascending
df.sort_values("Age", ascending=False) # descending

# 7. Group By:
#------------
df.groupby("City")["Age"].mean()

#8. Common Functions:
#-------------------
df["Age"].mean()
df["Age"].sum()
df["Age"].max()
df["Age"].min()
df["Name"].unique()
df["Name"].value_counts()

#9. Misc:
#--------
df.drop("Salary", axis=1)    # drop column
df.rename(columns={"Name":"Full Name"}, inplace=True)
df.isnull().sum()                # count missing values
df.fillna(0, inplace=True)       # fill missing values

# multi dimensional array
import pandas as pd
import numpy as np

# Example: Sales data for multiple months and regions
arrays = [
    ["Jan", "Jan", "Feb", "Feb"],
    ["North", "South", "North", "South"]
]
index = pd.MultiIndex.from_arrays(arrays, names=("Month", "Region"))

df1 = pd.DataFrame({
    "Sales": [200, 150, 220, 180],
    "Profit": [50, 30, 60, 40]
}, index=index)

print(df1)

