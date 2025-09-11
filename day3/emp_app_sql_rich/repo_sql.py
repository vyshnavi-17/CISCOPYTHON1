from db_setup import session, Employee
from log import logging
from sqlalchemy.exc import SQLAlchemyError,IntegrityError 
# CRUD (Create, Read All | Read One, Update, Delete)
# Employee App - SQL DB  - dict element

def create_employee(employee):
    employee_model = Employee(
        id=employee['id'],
        name=employee['name'],
        age=employee['age'],
        salary=employee['salary'],
        is_active=employee['is_active']
    )
    session.add(employee_model)  # Insert statement to db 
    session.commit()
    logging.info('Employee Created Successfully')


def read_all_employee():
    employees = session.query(Employee).all()
    dict_employee = []
    for employee in employees:
        employee_dict = {
            'id': employee.id,
            'name': employee.name,
            'age': employee.age,
            'salary': employee.salary,
            'is_active': employee.is_active
        }
        dict_employee.append(employee_dict)
    logging.info('Read All Employee')
    return dict_employee


def read_model_by_id(id):
    employee = session.query(Employee).filter_by(id=id).first()   
    logging.info('Employee ID queried') 
    return employee


def read_by_id(id):
    employee = read_model_by_id(id)
    if not employee:
        return None
        
    employee_dict = {
        'id': employee.id,
        'name': employee.name,
        'age': employee.age,
        'salary': employee.salary,
        'is_active': employee.is_active
    }
    logging.info('Read Employee By ID Success')
    return employee_dict
    

def update(id, new_employee):  # new_employee is updated data for employee with id
    employee = read_model_by_id(id)  # FIXED: Use read_model_by_id to get model instance
    if not employee:
        logging.info('Employee Not Found')
        return None
    
    # Update fields - example updates salary only (you can expand as needed)
    employee.salary = new_employee['salary']
    session.commit()
    logging.info('Employee Salary Updated')
    

def delete_employee(id):
    employee = read_model_by_id(id)  # FIXED: Use read_model_by_id to get model instance
    if not employee:
        logging.info('Employee Not Found')
        return None
    
    session.delete(employee)
    session.commit()
    logging.info('Employee Deleted Successfully')