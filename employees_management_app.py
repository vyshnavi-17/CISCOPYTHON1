employeees = []
employee = ('Banu',22,50000,True)
employeees.append(employee)


employee = ('Mahesh',32,53000,True)
employeees.append(employee)

employee = ('Vaishnavi',25,50000,True)
employeees.append(employee)


print('after add all employess:',employeees)
employeees.append(employee)

print('after add all employees:',employeees)

I = 0
search = 'vaishavi'
index = -1
for emp in employeees:
    if emp[0] == search:
        index = I
        break
    I +=1
if index == -1:
    print('employe not found')
else:
    search_employee =  employeees[index]
    print(search_employee)
    salary = float(input('salary:'))
    employee = (search_employee[0],search_employee[1],salary,search_employee[3])
    employeees[index]=employee
print ('after search and update:',employeees)

employee = ('Dravid',50,200.75,True)
employeees.append(employee)
print('after add dravid :',employeees)
employeees.pop()
print('after delete dravud',employeees)

position = 1
employeees.pop(position)
print('after delete mahesh',employeees)
