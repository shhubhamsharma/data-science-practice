# Day 4: Data Aggregation & Joins in Pandas
# Aggregation with groupby

# You can group your data by one or more 
# columns and apply summary 
# functions like mean(), sum(), count(), etc.

import pandas as pd

data = {
    "Department": ["HR", "IT", "IT", "HR", "Finance", "Finance", "IT"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"],
    "Salary": [50000, 60000, 65000, 52000, 70000, 72000, 68000]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Group by Department and calculate average salary
avg_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:\n", avg_salary)

# Count employees in each department
employee_count = df.groupby("Department")["Employee"].count()
print("\nEmployee Count by Department:\n", employee_count)



# 2️⃣ Multiple Aggregations

# You can apply multiple aggregation functions at once:
agg_salary = df.groupby("Department")["Salary"].agg(["mean", "max", "min"])
print("\nAggregated Salary Stats:\n", agg_salary)


# 3️⃣ Joins / Merges in Pandas

# In data science, datasets often come separately 
# and need to be combined. Pandas provides:

# merge() → SQL-like joins

# concat() → stacking data vertically or horizontally

df1 = pd.DataFrame({
    "Employee": ["Alice", "Bob", "Charlie", "David"],
    "Department": ["HR", "IT", "IT", "HR"]
})

df2 = pd.DataFrame({
    "Employee": ["Alice", "Bob", "Charlie", "Eve"],
    "Salary": [50000, 60000, 65000, 70000]
})

# Inner join (only common employees)
inner_join = pd.merge(df1, df2, on="Employee", how="inner")
print("\nInner Join:\n", inner_join)

# Left join (all from df1, matching from df2)
left_join = pd.merge(df1, df2, on="Employee", how="left")
print("\nLeft Join:\n", left_join)

'''
| Type  | Description                                           |
| ----- | ----------------------------------------------------- |
| inner | Only rows with matching keys in both dataframes       |
| left  | All rows from left dataframe, matched rows from right |
| right | All rows from right dataframe, matched rows from left |
| outer | All rows from both dataframes, fill missing with NaN  |

'''