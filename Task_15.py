def rot_encode(string, offset):
    my_alphabet = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
    new_string = ""
    for i in range(len(string)):
        if string[i] in my_alphabet or string[i] in my_alphabet.lower():
            for j in range(len(my_alphabet)):
                if my_alphabet[j] == string[i]:
                    new_string = new_string + my_alphabet[(j + offset) % len(my_alphabet)]
                if my_alphabet[j].lower() == string[i]:
                    new_string = new_string + my_alphabet[(j + offset) % len(my_alphabet)].lower()
        else:
            new_string = new_string + string[i]

    return new_string


def rot_decode(string, offset):
    offset = -offset
    return rot_encode(string, offset)


string1 = "abc"
string2 = "aboba"
string3 = "bcd"
print(rot_encode(string1, 1), rot_decode(string3, 1))
