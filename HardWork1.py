grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(students)
import statistics as sts

i_mean = []

for i in grades:
    i = (round(sts.mean(i), 2))
    i_mean.append(i)

print(i_mean[1])

GradesOfStudents = zip(students_sort, i_mean)
print(dict(GradesOfStudents))
