# Combined Aggregation & Join
import pandas as pd

df_scores = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "David"],
    "Class": ["A", "B", "A", "B"],
    "Math": [80, 70, 85, 90],
    "Science": [75, 80, 78, 85]
})

df_extra = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "David"],
    "Age": [14, 15, 14, 15]
})


# Calculate average score per student across Math and Science.

print("Calculate average score per student across Math and Science.")
df_scores["Average"]= df_scores[["Math","Science"]].mean(axis=1)
print(df_scores)

# Merge df_scores with df_extra to include the Age column.

print("Merge df_scores with df_extra to include the Age column.")
df_joined= pd.merge(df_scores,df_extra,how="left",on="Student")
print(df_joined)

print("Average Math score per class:\n")

df_avg_math=df_scores.groupby("Class")["Math"].mean()
print(df_avg_math)