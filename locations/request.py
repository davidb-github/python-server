LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]

# return all locations
def get_all_locations():
    return LOCATIONS

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
    # add an `id` property to the animal dictionary
    location["id"] = new_id
    # add the location dict to the list
    LOCATIONS.append(location)

    # return the dict w/ id property added
    return location