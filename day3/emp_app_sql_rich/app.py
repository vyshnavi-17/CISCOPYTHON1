import repo_sql as repo

def menu():
    message = '''
Options are:
1 - Create Employee
2 - List All Employees
3 - Read Employee By Id
4 - Update Employee
5 - Delete Employee
6 - Exit 
Your Option: '''
    
    try:
        choice = int(input(message))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")
        return None
    
    if choice == 1:
        try:
            id = int(input('ID: '))
            name = input('Name: ')
            age = int(input('Age: '))
            salary = float(input('Salary: '))
            is_active = input('Active (y/n): ').strip().lower().startswith('y')

            employee = {'id': id, 'name': name, 'age': age, 
                        'salary': salary, 'is_active': is_active}

            repo.create_employee(employee)
            print('Employee Created Successfully.')
        except ValueError:
            print("Invalid input for ID, Age or Salary. Please try again.")

    elif choice == 2:
        print('List of Employees:')
        employees = repo.read_all_employee()
        if not employees:
            print("No employees found.")
        else:
            for employee in employees:
                print(employee)

    elif choice == 3:
        try:
            id = int(input('ID: '))
            employee = repo.read_by_id(id)
            if employee is None:
                print('Employee not found.')
            else:
                print(employee)
        except ValueError:
            print("Invalid ID input.")

    elif choice == 4:
        try:
            id = int(input('ID: '))
            employee = repo.read_by_id(id)
            if employee is None:
                print('Employee Not Found')
            else:
                print(employee)
                salary = float(input('New Salary: '))
                new_employee = {
                    'id': employee['id'],
                    'name': employee['name'],
                    'age': employee['age'],
                    'salary': salary,
                    'is_active': employee['is_active']
                }
                repo.update(id, new_employee)
                print('Employee updated successfully.')
        except ValueError:
            print("Invalid input.")

    elif choice == 5:
        try:
            id = int(input('ID: '))
            employee = repo.read_by_id(id)
            if employee is None:
                print('Employee Not Found')
            else:
                repo.delete_employee(id)
                print('Employee Deleted Successfully.')
        except ValueError:
            print("Invalid input.")

    elif choice == 6:
        print('Thank you for using Application.')

    else:
        print("Please select a valid option (1-6).")

    return choice

def menus():
    choice = None
    while choice != 6:
        choice = menu()

if __name__ == "__main__":
    menus()