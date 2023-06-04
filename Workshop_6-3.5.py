def join_integers(int_list):
    joined_int = ''
    for i in int_list:
        joined_int +=str(i)
    return int(joined_int)
integers = [11, 33, 50]
joined_integer = join_integers(integers)
print(joined_integer)