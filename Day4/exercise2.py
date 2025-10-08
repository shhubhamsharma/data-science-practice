# Exercise 2: Employee Salary Aggregation

import pandas as pd

data = {
    "Employee": ["John", "Jane", "Mike", "Sara", "Paul", "Anna"],
    "Department": ["HR", "IT", "IT", "HR", "Finance", "Finance"],
    "Salary": [50000, 60000, 65000, 52000, 70000, 72000]
}

df = pd.DataFrame(data)

# Calculate the average salary per department.
avg_salary_department = df.groupby("Department")["Salary"].mean()
print(avg_salary_department)

# Find total salary per department.

total_salary_department = df.groupby("Department")["Salary"].sum()
print(total_salary_department)


# Determine which department has the highest average salary.
highest_salary_department = df.groupby("Department")["Salary"].mean().idxmax()
print(highest_salary_department)
