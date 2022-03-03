with open("ordbog.txt", encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    if len(line) == 7:
        with open('keys_clean.txt', 'ab+') as file:
            file.write(line.encode('utf-8'))
