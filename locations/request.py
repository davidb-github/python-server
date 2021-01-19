import sqlite3
import json
from models import Location

LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike",
        "status": "Open"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive",
        "status": "Open"
    }
]

# return all locations
# def get_all_locations():
#     return LOCATIONS

#return all locations via sql
def get_all_locations():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        """)

        # init empty list to hold all locations
        locations = []

        # convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a location instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Location class above.
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)
    # Use `json` package to properly serialize list as JSON
    return json.dumps(locations)


# Return single location by id
def get_single_location(id):
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location


# function to create new location - accepts location parameter
def create_location(location):
    # determine max id in location list
    max_id = LOCATIONS[-1]["id"]
    # increment max_id
    new_id = max_id + 1
    # add an `id` property to the location dictionary
    location["id"] = new_id
    # add the location dict to the list
    LOCATIONS.append(location)

    # return the dict w/ id property added
    return location

# function to delete location - accepts location id as parameter
def delete_location(id):
    location_index = -1

    # Iterate the LOCATIONS list, but use enumerate() so that you
    # can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Store the current index.
            location_index = index

    # If the location was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index)

# update existing location - accepts location id and new_location dict as input parameters
def update_location(id, new_location):
    # Iterate the LOCATIONS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Update the value.
            LOCATIONS[index] = new_location
            break