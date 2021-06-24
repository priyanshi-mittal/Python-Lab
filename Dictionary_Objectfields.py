import datetime

class Priyanshi(object):
    def __init__(self):
        self.Name = 'Priyanshi'
        self.Class = 'BTech'
        self.Sec = 'N'
        self.Roll = 7
        self.Branch = 'CSE'
        self.dt = str(datetime.datetime.now())

a = Priyanshi()
print(a.__dict__) # This is how we print all the objects fields using __dict__ method.
