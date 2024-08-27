grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
avg_grades_1 = [sum(grades[0])/len(grades[0]),
    sum(grades[1]) /len(grades[1]),
    sum(grades[2]) /len(grades[2]),
    sum(grades[3]) /len(grades[3]),
    sum(grades[4]) /len(grades[4])]
journal = {students[0]: avg_grades_1[0], students[1]: avg_grades_1[1], students[2]: avg_grades_1[2], students[3]: avg_grades_1[3], students[4]: avg_grades_1[4]}
print(journal)