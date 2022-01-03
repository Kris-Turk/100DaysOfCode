class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.employer = 'HybrIT UK'
        
    def migrate_south(self):
        self.employer = 'HybrIT NZ'
        
    def migrate_north(self):
        self.employer = 'HybrIT UK'
        

  
user1 = User('John',51)


print(user1)
print(user1.name)
print(user1.age)
print(user1.employer)