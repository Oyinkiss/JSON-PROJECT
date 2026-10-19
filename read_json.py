#Reading a json file 
import json
with open("student.json", "r", encoding="utf-8") as file:
    student=json.load(file)
    print(student)
    print(student["age"])
    print(student["skills"])