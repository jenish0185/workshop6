students=[
{"student_id": 1, "name": "Jean Castro", "class": "V"},
{'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
{'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
{'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
{'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]
key='name'
value='Jean Castro'
if any(student.get(key)==value for student in students):
    print(f"key: '{key}' and value: '{value}' do exist")
else:
    print(f"key: '{key}' and value: '{value}' do not exist")

key='address'
value='New York'
if any(student.get(key)==value for student in students):
    print(f"key: '{key}' and value: '{value}' do exist")
else:
    print(f"key: '{key}' and value: '{value}' do not exist")



