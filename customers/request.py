import sqlite3
import json
from models import Customer

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
# def get_all_customers():
#     return CUSTOMERS

# return all customers - sql
def get_all_customers():
    #open a connection to db
    with sqlite3.connect("./kennel.db") as conn:

        # setup row and cursor
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # select query
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer AS c
        """)

        # init an emply list to hold customer representations
        customers = []

        # convert rows of data into python list
        dataset = db_cursor.fetchall()

        # iterate list returned from database
        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'],
                                row['email'], row['password'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)


# return customer by id
# def get_single_customer(id):
#     requested_customer = None

#     for customer in CUSTOMERS:
#         if customer["id"] == id:
#             requested_customer = customer

#     return requested_customer

#return customer by id
def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer AS c
        WHERE c.id = ?
        """, ( id, ))

        # load the single returned result into memory
        data = db_cursor.fetchone()

        # create a customer instance from the current row
        customer = Customer(data['id'], data['name'], data['address'], data['email'], data['password'])

        #return
        return json.dumps(customer.__dict__)

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
