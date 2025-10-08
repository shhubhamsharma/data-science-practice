from pandasql import sqldf
import pandas as pd

data = [
    [1, "Amit", "Delhi Public School", 78, 85, 90],
    [2, "Priya", "Delhi Public School", 88, 79, 84],
    [3, "Ravi", "Modern School", 92, 89, 95],
    [4, "Sita", "Modern School", 85, 87, 90],
    [5, "John", "Cambridge", 90, 91, 89],
    [6, "tavi", "Modern School", 82, 99, 95],

]
column =["Math", "Science", "English"]
df = pd.DataFrame(data, columns=["ID", "Name", "SchoolName", "Math", "Science", "English"])
df["Average"] = df[column].mean(axis=1)

pysqldf = lambda q: sqldf(q, globals())

query = """
SELECT Name, SchoolName, Average
FROM df
WHERE Average > 85
ORDER BY Average DESC
"""
pysqldf(query)

#  Task 1: Students who scored above 90 in at least one subject/
student_above90 = df[(df["Math"]>90) | (df["Science"]>90) |(df["English"]>90)]
print(student_above90)

print("Task 2: Average marks per subject per school")


average_marks=df.groupby("SchoolName")[["Math","Science","English"]].mean()
print(average_marks)

# Task 3: Top 2 students per school by average marks
average_marks_top2=df.sort_values(["SchoolName", "Average"],ascending=False).groupby("SchoolName").head(2)
print(average_marks_top2)
