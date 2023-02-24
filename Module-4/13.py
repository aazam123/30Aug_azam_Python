# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class
class Student:
    def stdata(self):
      self.name=input("Enter the name")
      self.roll=int(input("Enter the roll no"))
    def display(self):
        print("name",self.name)
        print("roll",self.roll)
a=Student()        
a.stdata()
a.display()