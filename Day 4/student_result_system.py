def calculate_percentage(total_marks):
  return (total_marks/500)*100
marks=[]
for i in range(5):
   mark=int(input(f"Enter the marks for subject{i+1}:"))
   marks.append(mark)
total=sum(marks)
percentage=calculate_percentage(total)
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
