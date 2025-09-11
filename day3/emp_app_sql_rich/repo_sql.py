from db_setup import session, Employee
from log import logging
from sqlalchemy.exc import SQLAlchemyError,IntegrityError
from exc import EmployeeNotFound,EmpoyeeAlreadyExistError,DatabaseError

# CRUD (Create, Read All | Read One, Update, Delete)
# Employee App - SQL DB  - dict element

def create_employee(employee):
    try:
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
        
    except IntegrityError as ex:
        session.rollback()
        logging.error('Duplicate Employee ID:%s',ex)
        raise EmpoyeeAlreadyExistError(f"Employee ID={employee['id']} already exist")
        
    
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error('Database Error in creating Employee',ex)
        raise DatabaseError('Error while creating Database')
    


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
    

def update(id, new_employee):  
    employee = read_model_by_id(id)  
    if not employee:
        logging.info('Employee Not Found')
        return None

    employee.salary = new_employee['salary']
    session.commit()
    logging.info('Employee Salary Updated')
    

def delete_employee(id):
    employee = read_model_by_id(id)  
    if not employee:
        logging.info('Employee Not Found')
        return None
    
    session.delete(employee)
    session.commit()
    logging.info('Employee Deleted Successfully')