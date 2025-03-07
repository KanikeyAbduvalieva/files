# Task 1
file = open('test.txt', 'w')
file.write('HELLOWORLD\nPython')
file = open('test.txt', 'r')
print(file.read())
file.close()

# Task 2
file = open('users.txt', 'w')
log = input('Введите логин: ')
pas = input('Введите пароль: ')
file = open('users.txt', 'a')
file.writelines([log, ' ', pas])
file = open('users.txt', 'r')
print(file.read())
file.close()

# Task 3
with open("text.txt", "r") as f:
    text = f.read()
    print("Да, в тексте есть w" if "w" in text else "Нет, в тексте нет w")

# Task 4
text = '''Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;\nyou need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),\nbut you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.'''
with open("python.txt", "w") as f:
    f.write(text)

o_words = [word for word in text.split() if "o" in word]
print(o_words)

# Task 5
some_texts = """
    .detacilpmoc naht retteb si xelpmoC
    .xelpmoc naht retteb si elpmiS
    .ticilpmi naht retteb si ticilpxE
    .ylgu naht retteb si lufituaeB
    """
with open("some_texts.txt", "w") as f:
    f.write(some_texts)

with open("some_texts.txt", "r") as f:
    revers_text = f.read()[::-1]
    print(revers_text)

# Task 6
numbers_text = """
123
aaa456
fxdya 5 0 0
"""
with open("numbers.txt", "w") as f:
    f.write(numbers_text)

with open("numbers.txt", "r") as f:
    words_ = f.read()
    numbers = map(int, re.findall(r"\d+", words_))
    print("Сумма чисел: ", sum(numbers))
