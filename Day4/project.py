
'''
Analyze performance data of students from multiple schools, merge extra info (like city), and get useful insights such as:

Average performance by school and subject

Top students overall

School-wise ranking
'''

# Step 1 create data sets
import pandas as pd

# Student performance across subjects
students_df = pd.DataFrame({
    "StudentID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"],
    "SchoolID": [1, 1, 2, 2, 3, 3, 1, 2],
    "Math": [88, 75, 92, 68, 70, 80, 95, 85],
    "Science": [90, 72, 88, 70, 75, 85, 98, 80],
    "English": [85, 78, 82, 74, 88, 79, 91, 83]
})

# School details
schools_df = pd.DataFrame({
    "SchoolID": [1, 2, 3],
    "SchoolName": ["Greenwood High", "Riverdale Public", "Sunrise Academy"],
    "City": ["Delhi", "Mumbai", "Pune"]
})

# Step 2 Merge Datasets
df=pd.merge(students_df,schools_df,how="left",on="SchoolID")
print("Merged DataFrame:\n", df)


# Step 3 — Calculate Averages
# Add overall average per student
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# Average score per school
school_avg = df.groupby("SchoolName")[["Math", "Science", "English", "Average"]].mean().round(2)

print("\nAverage Scores per School:\n", school_avg)

# Step 4 — Find Top Performers

top_student= df.sort_values(by="Average",ascending=False).head(3)
print(top_student)

print("Step 5 — Find Subject Toppers")

subject_toppers={}

for subject in ["Math","Science","English"]:
    topper = df.sort_values(by=subject, ascending=False).head(1)[["Name", "SchoolName", subject]]
    # topper=df.loc[df[subject].idxmax(),["Name","SchoolName",subject]]
    subject_toppers[subject]= topper
print(subject_toppers)


# Count of students per school
student_count = df.groupby("SchoolName")["StudentID"].count()

# Combine into one report
summary = pd.concat([school_avg, student_count.rename("TotalStudents")], axis=1)
print("\nSchool Summary Report:\n", summary)
summary.to_csv("school_performance_summary.csv")
print("\nData exported successfully ")
