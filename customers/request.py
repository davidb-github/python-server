CUSTOMERS = [
     {
        "email": "jake@jake.com",
        "password": "kennel",
        "name": "jake b",
        "id": 1
    }
]

# return all customers
def get_all_customers():
    return CUSTOMERS

# return customer by id
def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

# add new customer - accepts customer parameter
def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)

    return customer
