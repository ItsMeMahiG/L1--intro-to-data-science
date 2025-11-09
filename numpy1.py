import numpy as np
data_type=[('name','S15'),('class',int),('height', float)]
students_details = [('mahi',7,5.1),('vruddhi',8,5.4),('johan',7,4.9),('myna',7,5)]
students=np.array(students_details,dtype=data_type)
print("original array :")
print(students)
print("sort by height")
print(np.sort(students, order='height'))