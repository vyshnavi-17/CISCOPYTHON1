from db_setup import session,Employee

#CRUD (Create, Read All | Read One, Update, Delete)
#Employee App - SQL DB  - dict element

def create_employee(employee):
    employee_model=Employee(
        id=employee['id'],
        name=employee['name'],
        age=employee['age'],
        salary=employee['salary'],
        is_active=employee['is_active']
    )
    session.add(employee_model) # Insert statement to db 
    session.commit()

def read_all_employee():
    employees=session.query(Employee).all()
    dict_employee=[]
    for employee in employees:
        employee_dict={'id':employee.id,
                       'name':employee.name,
                       'age':employee.age,
                       'salary':employee.salary,
                       'is_active':employee.is_active}
        dict_employee.append(employee_dict)
    return dict_employee



def read_model_by_id(id):
    employee=session.query(Employee).filter_by(id=id).first()    
    return employee


def read_by_id(id):
    employee=read_model_by_id(id)
    if not employee:
        return None
        
    
    employee_dict={'id':employee.id,
                       'name':employee.name,
                       'age':employee.age,
                       'salary':employee.salary,
                       'is_active':employee.is_active}
    return employee_dict
    

def update(id, new_employee):#new_employee is update at id
    employee=read_all_employee(id)
    if not employee:
        return None
    employee.salary=new_employee['salary']
    session.commit()
    
def delete_employee(id):
  employee=read_all_employee(id)
  if not employee:
      return None
  session.delete(employee)
  session.commit()