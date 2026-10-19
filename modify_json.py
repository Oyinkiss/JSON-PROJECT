import json
student_json="""
{
"name":"Oyinkansola",
"age":25,
"job":"Data Analyst",
"is_a_student_json":true,
"salary":[20, 310,410]
}
"""
student=json.loads(student_json)
print(student)
print(type(student))
print(student["salary"])
print(student["salary"][2])

#modifies
student["email"]="ooyin@gmail.com"
print(student["email"])

#add new arrayy
student["salary"].append(510)
print(student["salary"])
student["salary"].remove(20)
print(student["salary"])

with open("advancedstudent.json", "w", encoding="utf-8") as file:
    json.dump(student,file, indent=4)
print("Modification carried out and saved succesfully")