name = input("Name: ")
print (name)
###################################
light =  input("What is color of light is present to check what to do now :")

if(light == "Red"):
  print("STOP")
elif(light == "Yellow"):
  print("READY")
elif(light == "Green"):
  print("GO")
else:
  print("Invalid Input")
###################################
# prompt: wap in py to check marks of student using conditonal statement

name = input("Name: ")
print(name)

marks = int(input("Enter marks: "))

if marks >= 90:
  print("Grade: A")
elif marks >= 80:
  print("Grade: B")
elif marks >= 70:
  print("Grade: C")
elif marks >= 60:
  print("Grade: D")
elif marks >= 35:
  print("Grade: E")
else:
  print("Grade: F")

