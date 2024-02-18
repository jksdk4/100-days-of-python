import pandas

student_dict = {
    "student": ["Angela", "Luis", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)
print(student_df)

for (idx, row) in student_df.iterrows():
    if row.student == 'Angela':
        print(f"Index {idx} - {row.score}")
