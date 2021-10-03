def zip_str(string):
    counter = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            counter += 1
            if counter > 2:
                break  # Если встретилась последовательность одинаковых букв, длиной больше 2х, то нужно сжимать строку
        else:
            counter = 1
    if counter < 3:  # Не нужно сжимать строку, возвращаем исходную
        return string
    counter = 1
    new_str = ""
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            counter += 1
        else:
            if counter != 1:
                new_str = new_str + string[i] + str(counter)
            else:
                new_str = new_str + string[i]
            counter = 1
    return new_str


str1 = "AAAABBBCDDDDDDDDEEEEF"
str2 = ""
str3 = "AABBCC"

print(zip_str(str1), zip_str(str2), zip_str(str3))
