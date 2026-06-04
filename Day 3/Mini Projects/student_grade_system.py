name= input("Enter the name:")
m1=int(input("Enter the marks in Python:"))
m2=int(input("Enter the marks in Mathematics:"))
m3=int(input("Enter the marks in English:"))
total=m1+m2+m3
percentage=total/3
print("NAME:",name)
print("TOTAL:",total)
print("PERCENTAGE:",percentage)
if percentage>=90:
  print("GRADE A")
elif percentage>=75:
  print("GRADE B")
elif percentage>=50:
  print("GRADE C")
else:
  print("FAIL")
