'''
1. Create Your Own DataFrame
Make a DataFrame called students with columns:
"Name" → at least 4 names
"Marks" → random numbers between 50–100
"Subject" → like "Math", "Science", etc.
Print the DataFrame.

2. Do Some Analysis
Using your students DataFrame:
Print only the "Name" column.
Find the average of Marks.
Get the maximum Marks and the student who scored it.

3. Filtering Practice
Print all rows where:
Marks are greater than 70
Subject is "Math"
'''
import pandas as pd
data={
    "Name":["s1","s2","s3","s4"],
    "Marks":[60,70,71,73],
    "Subjects":["Math","Science","Math","SCience"]
}
students= pd.DataFrame(data);

print(students)

meanVal= students["Marks"].mean() # Finding average of Marks
print("Avg Marks:",meanVal)

student=students.sort_values("Marks",ascending=False).head(1) # Finding max marks and student
print("Max student marks:",student)

studentMarkG70= students[students["Marks"]>70] # Filtering Practice
print("Students with Mark >70:",studentMarkG70)

maxMarksOfMath= studentMarkG70[studentMarkG70["Subjects"]=="Math"] # Filtering Practice using chaining
print("Students with Mark >70 in Math:",maxMarksOfMath)
