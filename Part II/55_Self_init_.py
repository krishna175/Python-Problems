class Employee:
    no_of_leave = 9

    def printDetail(self):        # here if we pass an object self will become that object
        return f"My name is : {self.name}\nMy salary is : {self.salary}\nMy role is : {self.role}"
hemant = Employee()
nihal = Employee()





hemant.name = "Hemant Saw"
hemant.salary = 5000
hemant.role = "Instructor"

nihal.name = "Nihal Tiwari"
nihal.salary = 4000
nihal.role = "Student"

print(nihal.printDetail())       #calling self nihals object will be passed as an aurgument in the self
print("---------------")
print(hemant.printDetail())