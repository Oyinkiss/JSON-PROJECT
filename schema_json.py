import jsonschema
student_schema={
    "type":"object",
    "properties":{
        "name":{"type":"string"},
        "age":{"type":"number"},
        "job":{"type":"string"},
        "is_a_student_json":{"type":"boolean"}},
    "required":["name","age","job","is_a_student_json"],
    "additionalProperties":False
    }

#valid data
student_json={
"name":"Oyinkansola",
"age":25,
"job":"Data Analyst",
"is_a_student_json":True
}

jsonschema.validate(
    instance=student_json,
    schema=student_schema
)
print("Student data validated")