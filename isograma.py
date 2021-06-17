def is_isogram(string):
    alph = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    word = []
    for letter in alph:
        check_str = string.lower().count(letter)
        if check_str <= 1:
            word.append(True)
        else:
            word.append(False)
    no_isogram = word.count(False)

    if no_isogram > 0:
        print(False)
    else:
        print(True)

is_isogram("tigre")
is_isogram("arara")
is_isogram("oOl")