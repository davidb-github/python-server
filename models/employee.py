class Employee():
    def __init__(self, id, name, address, location_id):
        self.id          = id
        self.name        = name
        self.address     = address
        self.locationId = location_id
        self.location = None