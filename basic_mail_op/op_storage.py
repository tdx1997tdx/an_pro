class Storage:

    def __init__(self):
        self.temp_storage = {}

    def add(self,name,v_code):
        self.temp_storage[name]=v_code

    def verification(self,name,v_code):
        print(name)
        print(v_code)
        print(self.temp_storage.get(name))
        return self.temp_storage.get(name) and self.temp_storage.get(name)==v_code

    def remove(self,name):
        self.temp_storage.pop(name)

storage=Storage()