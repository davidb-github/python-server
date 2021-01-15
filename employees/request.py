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
def get_all_employees():
    return EMPLOYEES

# return employee by id
def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    
    return requested_employee

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