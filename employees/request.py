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
