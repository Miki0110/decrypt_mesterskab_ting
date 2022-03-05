with open("ordbog.txt", encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    if len(line) == 9+1:
        with open('words_length_9.txt', 'ab+') as file:
            file.write(line.encode('utf-8'))
