# n = input("please enter a password: ")
# f = ["0","1","2","3","4","5","6","7","8","9"]
# b = 0
# # print(len(f))
# for i in range (len(n)):
#   for j in range (len(f)):
#     if n[i] == f[j]:
#       b = 1
# if b == 0:
#   print("password is valid: ")
# else:
#  print("invalid password")

# taking a string and provide the fist common letter
n = input("please enter a string: ")
l = input("please enter a string: ")
b = -1
for i in range (len(n)):
  for j in range (len(l)):
    if n[i] == l[j]:
      b = i
      break
  if b != -1:      # if found, break outer loop
   break
if b != -1:
  print("the first common letter is: ", n[b])
else:
 print("No common word")