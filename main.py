
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
avg_grades = [0,0,0,0,0]
journal = {}
a = 0
l = 0
for i in range(len(grades)):
    a = 0
    for j in range(len(grades[i])):
        a += grades[i][j]
        l = len(grades[i])
    avg_grades[i] = a / l
    journal[students[i]] = avg_grades[i]
print(journal)

