class Employees:
    def __init__(self, name, last):
        self.name = name
        self.last = last
        
class Supervisors(Employees):
    def __init__(self, name, last, password):
        super().__init__(name, last)
        self.password = password
        
class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for {} days?".format(days)
        
adrian = Supervisors('Adrian', 'Smith', '12345')
emily = Chefs('Emily', 'Jones')
juno = Chefs('Juno', 'J')
print(emily.leave_request(3))
print(adrian.password)
print(emily.name)