def vow(st):

    vowel=set(['a','e','i','o','u'])
    new=set()
    for string in st:
        if string[0].lower() in vowel:
            new.add(string)
    return new
strings = set(['shrek','panda','ayoyama','ddt'])
vowel_st= vow(strings)
print(vowel_st)