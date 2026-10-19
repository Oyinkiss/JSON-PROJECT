import json
from xml.etree.ElementTree import indent
student_json='{"name": "John Doe", "age": 20, "major": "Computer Science"}'
student=json.loads(student_json)
print(student)
print(type(student))

#parse python to json FOR THE DUMP
import json
student={
    "name": "John Doe", "age": 20, "major": "Computer Science"
    }
student_json=json.dumps(student)
print(student_json)
print(type(student_json))

#Indent to make it more easier to read 
#dump convert python to json
import json
student= {"name":"Oyinkansola",
    "age":25,
    "department":"chemical engineering",
    "is_a_student":True,
    "skills":["python","javascript","design"]}

print(json.dumps(student, indent=3))
print(type(student))

#create a json file
import json
student= {"name":"Oyinkansola",
    "age":25,
    "department":"chemical engineering",
    "level":"400 level",
    "is_a_student":True,
    "skills":[
        "python","ML/AL","Data Science"
              ]
    }
with open("student.json", "w",encoding="utf-8") as file:
    json.dump(student,file, indent=3)
    print(student)
    print("Student data saved successfully")


    