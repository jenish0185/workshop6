def over_age_of_18(people_list):
    new_list = []
    for person in people_list:
        if person ['age'] > 18:
            new_list.append(person)
    return new_list


people_list = [
    {'name':'jenish', 'age':'18'},
    {'name':'tenzin', 'age':'16'},
]

over_age_of_18_people = over_age_of_18(people)
print(over_age_of_18_people)