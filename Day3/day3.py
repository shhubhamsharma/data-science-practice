'''
isin() filtering multiple values
replace() modifying specific values
dropna() & fillna() handling missing data
duplicated() & drop_diplicates()
'''

import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Alice"],
    "City": ["Delhi", "Mumbai", "Delhi", np.nan, "Pune", "Bangalore", "Delhi"],
    "Score": [65, 80, np.nan, 90, 75, 85, 65],
    "Age": [25, 30, 35, 40, np.nan, 29, 25]
}

df = pd.DataFrame(data)
print("Original Dataframe:")
print(df)

# Filter using .isin() students from Delhi or Mumbai
filtered_df=df[df["City"].isin(["Delhi","Mumbai"])]
print(filtered_df)


# Replace Values 
df["City"]=df["City"].replace("Delhi","New Delhi")
print("Replace Values \n")
print(df)

#Handling Missing Data
df_dropna= df.dropna()
print("Drop Na \n")
print(df_dropna)
print("Replace mising values \n")
df_replace_value=df.fillna({"City":"Unknown","Score":df["Score"].mean(),"Age":df["Age"].median()})
print(df_replace_value)

#Detect & Remove duplicates
print("Duplicated rows\n",df[df.duplicated()])
df_no_dupes =df.drop_duplicates()
print("df_no_dupes")
print(df_no_dupes)