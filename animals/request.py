from models.customer import Customer
import animals
import sqlite3
import json
from models import Animal
from models import Location

ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "location_id": 1,
        "customer_id": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "location_id": 1,
        "customer_id": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "location_id": 2,
        "customer_id": 1,
        "status": "Admitted"
    }
]

# Function with no parameter
def get_all_animals():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name AS location_name,
            l.address AS location_address,
            c.id AS customer_id,
            c.name AS customer_name,
            c.address AS customer_address
        FROM animal AS a
        JOIN location AS l
            ON l.id - a.location_id
        JOIN customer AS c
            ON c.id = a.customer_id
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id']) # location optional property
            
            # Create a Location instance from the current row
            location = Location(row['id'], row['location_name'], row['location_address'])

            customer = Customer(row['customer_id'], row['customer_name'], row['customer_address'])
            animal.customer = customer.__dict__
            
            # Assign the dictionary representation of the location object instance to the Animal.location property
            animal.location = location.__dict__

            # add newly created animal object instance to the animals list as type dictionary
            animals.append(animal.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(animals)


# function with single param that calls sqllite
def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name AS animal_name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.id AS location_id,
            l.name AS location_name,
            c.id AS customer_id,
            c.name AS customer_name,
            c.address AS customer_address
        FROM animal AS a
        JOIN location AS l
            ON l.id = a.location_id
        JOIN customer AS c
            ON c.id = a.customer_id
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['animal_name'], data['breed'],
                            data['status'], data['location_id'],
                            data['customer_id'])
        
        location = Location(data['id'], data['location_name'])
        animal.location = location.__dict__

        customer = Customer(data['customer_id'], data['customer_name'], data['customer_address'])
        animal.customer = customer.__dict__

        return json.dumps(animal.__dict__)

# get animal by location id
def get_animals_by_location(location_id):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            a.id,
            a.name,
            a.status,
            a.breed,
            a.customer_id,
            a.location_id
        from Animal AS a
        WHERE a.location_id = ?
        """, ( location_id, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['status'], row['breed'] , row['customer_id'], row['location_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)

# get animal by status
def get_animals_by_status(status):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            a.id,
            a.name,
            a.status,
            a.breed,
            a.customer_id,
            a.location_id
        from Animal AS a
        WHERE a.status = ?
        """, ( status, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['status'], row['breed'] , row['customer_id'], row['location_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)

# function to create new animal - accepts animal parameter
def create_animal(animal):
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal

# function to delete animal - accepts animal (id) as parameter
def delete_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))

# update existing animal - accepts animal id and new_anmial dict as parameters        
def update_animal(id, new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'], new_animal['location_id'],
              new_animal['customer_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


# update existing animal - accepts animal id and new_anmial dict as parameters
# def update_animal(id, new_animal):
#     # Iterate the ANIMALS list, but use enumerate() so that
#     # you can access the index value of each item.
#     for index, animal in enumerate(ANIMALS):
#         if animal["id"] == id:
#             # Found the animal. Update the value.
#             ANIMALS[index] = new_animal
#             break