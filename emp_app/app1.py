import repo

# test create employeee and readall
employee = (101,'Banu',22,50000,True)
repo.create_employee(employee)
print(f'employee {employee[1]} created successfully')
print('after add: , repo.read_all_employees')

employee = (102,'Mahesh',22,50000,True)
repo.create_employee(employee)
print(f'employee {employee[1]} created successfully')
print('after add: , repo.read_all_employees')

employee = (103,'vaishnavi',22,50000,True)
repo.create_employee(employee)
print(f'employee {employee[1]} created successfully')
print('after add: , repo.read_all_employees')


# test read by id
employee  = repo.read_by_id(103)
if employee == None:
    print ('employee not found')
else:
     id,name,age,salary,is_active = employee
     salary += 20000
     new_employee = (id,name,age,salary,is_active)
     repo.update(103,new_employee)
     print('after update:',repo.read_all_employees())

#testdelete
repo.delete_employee(102)
print('after delete', repo.read_all_employees())

