grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
avg_grades_1 = [sum(grades[0])/len(grades[0]),
    sum(grades[1]) /len(grades[1]),
    sum(grades[2]) /len(grades[2]),
    sum(grades[3]) /len(grades[3]),
    sum(grades[4]) /len(grades[4])]
journal = zip(students, avg_grades_1)
print(dict(journal))

#grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#students = sorted(list(students))
#avg_grades = [0,0,0,0,0]
#journal = {}
#a = 0
#l = 0
#for i in range(len(grades)):
#    a = 0
#    for j in range(len(grades[i])):
#        a += grades[i][j]
#        l = len(grades[i])
#    avg_grades[i] = a / l
#    journal[students[i]] = avg_grades[i]
#print(journal)