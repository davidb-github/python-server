EMPLOYEES = [
    {
        "name": "david",
        "locationId": 1,
        "animalId": 1,
        "id": 1
    },
    {
        "name": "sam",
        "locationId": 1,
        "animalId": 1,
        "id": 2
    },
    {
        "name": "daniel",
        "locationId": 2,
        "animalId": 1,
        "id": 3
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