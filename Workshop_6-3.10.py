def lst(list1,list2):

    set1 = set(list1)
    set2 = set(list2)
    diff1 = list(set1 - set2)
    diff2 = list(set2 - set1)
    return diff1, diff2

list1 = ["red", "orange", "green", "blue", "white"]
list2 = ["black", "yellow", "green", "blue"]
diff1, diff2 = lst(list1, list2)
print("Color1-Color2:", diff1)
print("Color2-Color1:", diff2)