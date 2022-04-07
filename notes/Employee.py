class Employee:

    # constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.salary = 0
        self.birthday = ''

    # methods
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id


