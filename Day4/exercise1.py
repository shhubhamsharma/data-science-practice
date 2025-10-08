import pandas as pd

data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Class": ["A", "B", "A", "B", "A", "B"],
    "Score": [85, 90, 78, 88, 92, 75]
}

df = pd.DataFrame(data)


# Exercise 1: Average Scores by Class
avg_score = df.groupby("Class")["Score"].mean()
print(avg_score)

# Count the number of students 
student_count = df.groupby("Class")["Class"].count()
print(student_count)

print("Find the maximum and minimum score per class using agg().")
min_max_score = df.groupby("Class").agg(["min","max"])
print(min_max_score)