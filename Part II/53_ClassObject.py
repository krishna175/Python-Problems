class student:   #created a class named student
    teachers = ["Mahesh", "Girish","Shiv"] # creating a variable inside class
    pass         # pass is used to do nothing in python

hemant = student()     # created an object of class student
nihal = student()

hemant.name = "Hemant Saw"
hemant.age = 19
hemant.div = "A"



nihal.name = "Nihal Tiwari"
nihal.age = 20
nihal.subjects = ["IOT","INS","Networking"]
print(hemant.name,hemant.div, nihal.name,nihal.subjects,nihal.age)
print(hemant.teachers)  # using the variable inside calss which is common for all the objects
print(nihal.teachers)
print(student.teachers)

student.teachers = ["Mahesh", "Girish","Shiv", "Drahsti", "Neha"]
nihal.teachers = ["Mahesh", "Girish","Shiv", "Drahsti"]
hemant.teachers  = ["Mahesh", "Girish","Shiv","Neha"]


print(hemant.teachers) # here a new variable instance is generated in the object as hemant.teachers
print(nihal.teachers)
print(student.teachers)


print(hemant.__dict__)
print(nihal.__dict__) # dict prints the attributes of a class of object in distiocnary format
