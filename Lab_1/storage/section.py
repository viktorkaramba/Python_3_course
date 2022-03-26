class Section:
    id = None
    name = None

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name
