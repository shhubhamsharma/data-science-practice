
# Day 3: Data Cleaning & Filtering Exercises (Python)

import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Alice", None],
    "City": ["Delhi", "Mumbai", "Delhi", np.nan, "Pune", "Bangalore", "Delhi", "Mumbai"],
    "Score": [65, 80, np.nan, 90, 75, 85, 65, 92],
    "Age": [25, 30, 35, 40, np.nan, 29, 25, 33],
    "Gender": ["F", "M", "M", "M", "F", "M", "F", "F"]
}
df = pd.DataFrame(data)
print(df)

# Select all rows where City is "Delhi".
df_city_delhi =  df[df["City"].isin(["Delhi"])]
print("Q1:\n")
print(df_city_delhi)
# Filter rows where Score > 70 and Age < 35.
df_age_score =  df[(df["Score"]>70) & (df["Age"]<35)]
print("Q2:\n")
print(df_age_score)
# Find all rows where Name starts with the letter "A".
df_dropna= df.dropna()
print("Drop Na \n")
print(df_dropna)
df_name= df_dropna[df_dropna["Name"].str.startswith("A")]
print('Q3\n',df_name)


'''
Handling Missing Values
🎯 Tasks

Find all rows that have any missing value.

Drop all rows where City is missing.

Replace missing Score values with the average score.

Replace missing Age values with the median age.

Replace missing Name values with "Unknown".

💡 Hint: Use isna(), dropna(), and fillna().
'''

print("Find all rows that have any missing value.")
df_missing_value_row= df.isna()

print(df[df.isna().any(axis=1)])

print("Drop all rows where City is missing.")
# df=df[df["City"].isin(df["City"].dropna())]
df = df.dropna(subset=["City"])
print(df)

print("Replace missing Score values with the average score.")

df =df.fillna({"Score":df["Score"].mean()})
print(df)


print("Replace missing Age values with the median age.")
df =df.fillna({"Age":df["Age"].median()})
print(df)

print("Replace missing Name values with Unknown.")
df =df.fillna({"Name":"Unknown"})
print(df)



'''
EXERCISE 3 — Replacing & Mapping
🎯 Tasks

Replace "Delhi" with "New Delhi" in the City column.

Replace "M" → "Male", "F" → "Female" in the Gender column.

Create a new column called "Category":

"High" if Score > 80

"Medium" if 60 <= Score <= 80

"Low" if Score < 60

💡 Hint: Use replace() or map(), and for the new column use apply() or np.select().
'''
print("Replace Delhi with New Delhi in the City column.")
df["City"]=df["City"].replace("Delhi","New Delhi")
print(df)

df=df.replace({"Gender":{"M":"Male","F":"Female"}})
print(df)

df['Category'] ="Low"
df.loc[df["Score"]>60,'Category']="Medium"
df.loc[df["Score"]>80,'Category']="High"

print("add column")
print(df)

'''
EXERCISE 4 — Removing Duplicates & Outliers
🎯 Tasks

Find how many duplicate rows exist.

Remove all duplicates.

Suppose any Score > 100 is invalid — replace those with NaN.

Remove rows where Age < 20 or Age > 60 (outlier filtering).

💡 Hint: Use duplicated(), drop_duplicates(), and between().
'''
print("Find how many duplicate rows exist.")
print("Number of duplicate rows:", df.duplicated().sum())

print(df[df.duplicated()])

print("Remove duplicate")

df= df.drop_duplicates()
print(df)

print("Remove those Age <20>60")
df=df[df["Age"].between(20,60)]
print(df)

'''
EXERCISE 5 — Complex Filtering
🎯 Tasks

Select all females in "New Delhi" with Score >= 70.

Find people with the same Name appearing more than once.

Sort the DataFrame by City (ascending) and Score (descending).

Get the top 3 scores per City.

💡 Hint:

Use groupby("City").head(3)

For duplicates: df["Name"].value_counts() > 1
'''

print("Select all females in \"New Delhi\" with Score >= 70.")
df_fil=df[(df["Gender"]=="Female") & (df["City"]=="New Delhi") & (df["Score"]>70)]
print(df_fil)

df_dup=df[df["Name"].duplicated(keep=False)]
print(df_dup)
df=df.sort_values("City")
print(df)
df_grouped=df.groupby("City").head(3)
print(df_grouped)

print("SAVING Cleaned")
print(df.to_csv("./cleaned_data.csv",index=False))

df_copied= pd.read_csv('./cleaned_data.csv')
print(df_copied)