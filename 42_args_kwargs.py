#Note : we cannot pass args first and then statement because the convention says that
# we have to pass norml statements first and then args and then kwargs
# Eg: (normal,*args,**kwargs) and not like (*args,normal,**kwargs)

def function_print_name(statement,*args,**kwargs):  # this *args can be given any name like *argument,*myname,*names...etc
    print(statement) # this is a normal argument which is passed
    # print(args[0])     # this args are passed in this function as tuple
    for i in args:
        print(i)
    print("This are our heroes:")
    for key,value in kwargs.items():
        print(f"{key} is {value} of the class.")
# function_print_name("Hari", "Hemant", "Nihal", "Raju", "Shubam")
list = ["Hari", "Hemant", "Nihal", "Raju", "Shubam","Jay"]
statement = "This the list of students: "
kw = {"Hari":"Monitor","Sunil":"Topper","Rahul":"Coordinator"}
function_print_name(statement,*list,**kw)