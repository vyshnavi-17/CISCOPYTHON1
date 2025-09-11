class EmployeeException(Exception):
    pass

class EmployeeNotFound(EmployeeException):
    pass

class EmpoyeeAlreadyExistError(EmployeeException):
    pass

class DatabaseError(EmployeeException):
    pass
    