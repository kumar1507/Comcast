def greet():
    print("Greetings Mr. Sachin, Welcome to the event. ...")


def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.....")


def greetGstCty(gname, city):
    print(f"Greetings Mr. {gname} from {city}, Welcome to the event. ....")


greet()
greetGst("Rahul")
greetGstCty("Rohit", "Mumbai")

print("-" * 40)


def admission(fname, lname, age, conno, adr, edqlf, des):
    print(f"Name : {fname}{lname}")
    print(f"Age : {age}")
    print(f"Contact No : {conno}")
    print(f"Address : {adr}")
    print(f"Education Qualification : {edqlf}")
    print(f"Designation : {des}")


admission(age=34, adr="indra nagar , banglore", des="MGR", fname="Mike", lname="Tyson", conno=23492394,
          edqlf="Graduate")

print("-" * 40)
# recursive calls
def fun(n):
    if n == 0:
        return n
    # print ("Hello World")
    print(n)
    fun(n - 1)


fun(10)
