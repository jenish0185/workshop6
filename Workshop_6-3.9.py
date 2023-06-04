def inst(lst, st):
    return [st + str(item) for item in lst]

lst = [1,2,3,4]
st = 'emp'
new_lst = inst(lst, st)
print(new_lst)