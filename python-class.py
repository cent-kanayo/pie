# myTuple = ("Apple", "Mango", "Orange", "Banana")

# myTuple = tuple(("Apple", "Orange", "Guava", "Pineapple"))


# print("My best fruit is " + myTuple[1])

# jobOffer_1 = {"salary": 70000, "isTimeOff": False}
# jobOffer2 = {"salary": 30000, "isTimeOff": True}
# jobOffer3 = {"salary": 50000, "isTimeOff": True}


# if jobOffer_1["salary"] >= 40000 and jobOffer_1["isTimeOff"] == True:
#     print("I am taking this job") 
# else:
#     print("This job is not my type")
# if jobOffer2["salary"] >= 40000 and jobOffer2["isTimeOff"] == True:
#     print("I am taking this job") 
# else:
#     print("This job is not my type")
# if jobOffer3["salary"] >= 40000 and jobOffer3["isTimeOff"] == True:
#     print("I am taking this job") 
# else:
#     print("This job is not my type")


# personAge = 0
# if personAge < 13:
#     print("You are a child, your bus fair is 5💷" )
# elif personAge > 12 and personAge < 19:
#     print("You are a young adult, Your bus fair is 7💷" )
# elif personAge > 18 and personAge < 65:
#     print("You are an adult, Your bus fair is 10💷" )
# else:
#     print("You are a veteran, Your bus fair is 6💷")

# friend1 = "David"
# friend2 = "Mike"
# friend3 = "Mark"
# friend4 = "James"
# friend5 = "John"
friends = ["David","Mike","Mark","James","John"]
# print(len(friends))
reversedList = []

# for i in range(0, len(friends)):
#     if friends[i] == "Mark":
#         break
#     print(friends[i])
   

# print(reversedList)

# for i in friends:
#     print(i)
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# Day 1 todos before going to school

# Void function
# def todos(day):
#     print("Day " + day)
#     print("Wake up")
#     print("Brush teeth")
#     print("Take a bath")
#     print("Eat breakfast")
#     print("Wear Uniform")
#     print("Go to school")
#     return 10
    
# todos("6")
# result = todos()
# print(result)

# # Day 2 todos before going to school
# myDailyTodos = todos()

# print(myDailyTodos)

# Non-void functions

# def return_function():
#     return 2 + 2
# print(return_function())

# def add(num_1, num_2):
#     return num_1 + num_2
# value_1 = int(input("Enter first number"))
# value_2 = int(input("Enter second number"))
# result = add(value_1, value_2)
# new_value = 40 + result
# print(new_value)

def calc(num_1, num_2, operator):
    if(operator == "+"):
        return num_1 + num_2
    if(operator == "-"):
        return num_1 - num_2
    if(operator == "/"):
        return num_1 / num_2
    if(operator == "*"):
        return num_1 * num_2
    return "Please select the right operator"
value_1 = int(input("Enter first number"))
operator = input("Enter operator: +-*/")
value_2 = int(input("Enter second number"))

result = calc(value_1, value_2, operator)
print(int(result))

# def call():50
#     print("Hello, World")
#     return
#     print("Hi, I won't even run")

# def greeting (firstname, lastname, state):
#     return f"Your name is {firstname} {lastname}, and you live in {state}"

# firstName = input("Enter first name: ")
# lastName = input("Enter last name: ")
# state = input("Enter state: ")
# sayGreeting = greeting(firstName, lastName, state)
# print(sayGreeting)

# firstname = "Mark"
# print(firstname)

# def sayName():
#     print("Mark")