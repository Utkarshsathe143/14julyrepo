# functions 
# def avg():
#     a = int(input("enter the value for a"))
#     b = int(input("enter the value for b"))
#     c = int(input("enter the value for c"))
#     avgr = (a+b+c)/3
#     print(avgr)
# avg()

# passing a function with argument
# def naam(name):
#     # name = input("enter a name: ")
#     print("good morning " + name)
# naam("utkarsh")

#recurrsive fucntion 
def factorial(n):
    b = n * factorial(n-1)
    return(b)
n = int(input("enter a number"))
b = factorial(n)
print(b)

