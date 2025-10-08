# 🧩 Step 1 — Create a Student Table (SQL style)

import pandas as pd

data = [
    [1, "Amit", "Delhi Public School", 78, 85, 90],
    [2, "Priya", "Delhi Public School", 88, 79, 84],
    [3, "Ravi", "Modern School", 92, 89, 95],
    [4, "Sita", "Modern School", 85, 87, 90],
    [5, "John", "Cambridge", 90, 91, 89],
]

df = pd.DataFrame(data, columns=["ID", "Name", "SchoolName", "Math", "Science", "English"])
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

'''
| SQL Operation | Pandas Equivalent                    |
| ------------- | ------------------------------------ |
| `SELECT`      | `df[["col1", "col2"]]`               |
| `WHERE`       | `df[df["col"] > 80]`                 |
| `ORDER BY`    | `df.sort_values(by="col")`           |
| `GROUP BY`    | `df.groupby("col")["target"].mean()` |
| `JOIN`        | `pd.merge(df1, df2, on="key")`       |
| `LIMIT`       | `df.head(n)`                         |
'''
# Example 1: SELECT specific columns

print(df[["ID","Name"]])

# Example 2: WHERE condition (filter)

print(df[df["Math"]>75])

# Example 3 order by

print(df.sort_values(by="Average"))

# Group by
print(df.groupby("SchoolName")["Average"].mean())

# Example 5: SELECT with multiple conditions

print(df[(df["Science"]>34)&df["Math"]>70][["Name","ID","SchoolName"]])


# Real SQL in pandas
