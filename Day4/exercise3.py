#3 Joining employee details
import pandas as pd

df1 = pd.DataFrame({
    "Employee": ["John", "Jane", "Mike", "Sara"],
    "Department": ["HR", "IT", "IT", "HR"]
})

df2 = pd.DataFrame({
    "Employee": ["John", "Jane", "Mike", "Paul"],
    "Salary": [50000, 60000, 65000, 70000]
})


inner_joined_df = pd.merge(df1,df2,how="inner",on="Employee")
print("Perform an inner join on Employee.")
print(inner_joined_df)

left_joined_df = pd.merge(df1,df2,how="left",on="Employee")
print("Perform an left join on Employee.")
print(left_joined_df)


outer_joined_df = pd.merge(df1,df2,how="outer",on="Employee")
print("Perform an outer join on Employee.")
print(outer_joined_df)



