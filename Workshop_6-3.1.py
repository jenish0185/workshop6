def st(list_of_strings):
    new_list=[]
    for string in list_of_strings:
        if 'a' in string:
            new_list.append(string)
    return new_list

list_of_strings=['apple','ball','cat','dog','egg']
a=st(list_of_strings)
print(a)