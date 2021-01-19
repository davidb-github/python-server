import sqlite3
import json
from models import Employee, employee


EMPLOYEES = [
    {
        "name": "david",
        "location_id": 1,
        "animal_id": 1,
        "id": 1,
        "fte": True
    },
    {
        "name": "sam",
        "location_id": 1,
        "animal_id": 1,
        "id": 2,
        "fte": True
    },
    {
        "name": "daniel",
        "location_id": 2,
        "animal_id": 1,
        "id": 3,
        "fte": True
    }
]

# return all employees
# def get_all_employees():
#     return EMPLOYEES

# return all employees - sql
def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        """)

        # init an empty list to hold employee representations
        employees = []

        # convert rows of data into python list
        dataset = db_cursor.fetchall()

        #iterate list of data returned from db
        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])

            employees.append(employee.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)


# return employee by id
# def get_single_employee(id):
#     requested_employee = None

#     for employee in EMPLOYEES:
#         if employee["id"] == id:
#             requested_employee = employee
    
#     return requested_employee


# return employee by id
def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee AS e
        WHERE e.id = ?
        """, ( id, ))

        # load the single result into memory
        data = db_cursor.fetchone()

        #create an employee instance from the current row
        employee = Employee(data['id'], data['name'], data['address'], data['location_id'])

    return json.dumps(employee.__dict__)


# add new employee - accepts employee parameter
def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)

    return employee

# function to delete employee - accepts employee id as parameter
def delete_employee(id):
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

# update existing employee - accepts employee id and new_employee dict as input parameters
def update_employee(id, new_employee):
    # Iterate the EMPLOYEES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break