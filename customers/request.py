CUSTOMERS = [
     {
        "email": "jake@jake.com",
        "password": "kennel",
        "name": "jake b",
        "active": True,
        "id": 1
    },
    {
        "email": "david@david.com",
        "password": "kennel",
        "name": "david b",
        "active": True,
        "id": 2
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

# function to delete customer - accepts customer id as parameter
def delete_customer(id):
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

# update existing customer - accepts customer id and new_customer dict as input parameters
def update_customer(id, new_customer):
    # Iterate the CUSTOMERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break
