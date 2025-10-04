import pandas as pd

data= {
    "Name": ["Alice", "Bob", "Charlie","David"],
    "Age": [25, 30, 35,40],
    "City": ["Delhi", "Mumbai", "Bangalore","Delhi"],
    "Score": [60, 80, 30,   90]
}

df= pd.DataFrame(data);
print(df)

#Basic info of Dataframe
print("Info\n",df.info())
print("Describe\n",df.describe())

#Select column
print("Only Name:\n",df["Name"])
print("Only Name and City:\n",df[["Name","City"]])

#Filter Data

print("Student Older than 30:\n",df[df["Age"]>30])
print("Student From Delhi and Age>20\n",df[(df["City"]=="Delhi") & (df["Age"]>40)])

#sort data
print("Sort by Age:\n",df.sort_values(by="Age",ascending=True))

# group by
print("Group by City:\n",df.groupby("City")["Score"].mean())

