import pandas as pd

'''
From the given dataset, print the youngest student.

Find the average score of students from Delhi.

Sort students by Age (ascending) and print the top 3.
'''

data= {
    "Name": ["Alice", "Bob", "Charlie","David"],
    "Age": [25, 30, 35,40],
    "City": ["Delhi", "Mumbai", "Bangalore","Delhi"],
    "Score": [60, 80, 30,   90]
}

df= pd.DataFrame(data);
print(df)

youngestStudent= df[df["Age"]==df["Age"].min()]
youngestStudentSorted= df.sort_values(by="Age",ascending=True).head(1)

print("youngestStudent:\n",youngestStudent)
print("youngestStudentSorted:\n",youngestStudentSorted)

'''
youngestStudent = df.loc[df["Age"].idxmin()]
print("Youngest Student:\n", youngestStudent)
'''
#2 
avgStudentScoreFromDelhi= df[df["City"]=="Delhi"].groupby(by="City")["Score"].mean()

print("avgStudentScoreFromDelhi:",avgStudentScoreFromDelhi)

#3 
print(df.sort_values(by="Age").head(3))

'''
What is df.loc?
loc is location based indexing, used to select rows and columns by labels

'''
print("##########")
print(df.loc[0])
#Filter rows
print(df.loc[df['City']=="Delhi"])
print("##########")

print(df.loc[df["Age"].idxmin()])


#### Exercise for Day2###
#1. Select only the Name and Score of all students from Delhi using .loc.

all_student_name_score = df.loc[df["City"]=="Delhi",['Name','Score']]
print("1. Select only the Name and Score of all students from Delhi using .loc.")
print(all_student_name_score)

print("Find the oldest student using .loc and .idxmax().")
oldest_student = df.loc[df['Age'].idxmax()]
oldest_student_df = df.loc[[df['Age'].idxmax()]] # Data frame 

print(oldest_student);
print(oldest_student_df);

print("Select the rows for the 1st and 3rd student (Alice and Charlie) with only Name and Age.")
first_3rd_row= df.loc[[0,2],["Name","Age"]]
print(first_3rd_row)


print("Increase the score of all students from Delhi by 5 using .loc. Print the updated DataFrame.")

df.loc[df["City"]=="Delhi","Score"]+=5
print(df)

print("Get the Name of the student with the lowest score using .loc.")
student_with_lowest_score=df.loc[[df["Score"].idxmin()]]
print(student_with_lowest_score)
