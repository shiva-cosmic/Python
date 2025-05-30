marks = {
  "Shivansh":100,
  "Devansh": 85,
   "Rohan": 23
}


print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Shivansh":99})

# Difference Between
print(marks.get("Shivansh")) #it will give none of key is wrong
# or 
print(marks["Shivansh"]) #If the key is wrong then it will give error,