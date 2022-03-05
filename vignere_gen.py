import string

alphabet = 'abcdefghijklmnopqrstuvwxyzæøå'

# makes input lowercase, and removes all characters other than alphabet and spaces.
def clean_input(text):
    text = text.lower()
    tmp = [c if c in (alphabet + string.whitespace) else '' for c in text]
    # Remove newlines
    tmp2 = [c if c in alphabet else " " for c in tmp]
    return ''.join(tmp2)


def add(a, b):
    # ignore spaces and newlines
    if a in string.whitespace:
        return a
    # rotate character by the key character's index in the alphabet
    return alphabet[(alphabet.index(a) + alphabet.index(b)) % len(alphabet)]
def rem(a, b):
    # ignore spaces and newlines
    if a in string.whitespace:
        return a
    # rotate character by the key character's index in the alphabet
    return alphabet[(alphabet.index(a) - alphabet.index(b)) % len(alphabet)]


# code = plain + key
def vignere_encrypt(key, text):
    ciphertext = ""
    for i in range(len(text)):
        ciphertext += add(text[i], key[i%len(key)])
    return ciphertext
# plain = code - key
def vignere_decrypt(key, code):
    plaintext = ""
    for i in range(len(code)):
        plaintext += rem(code[i], key[i%len(key)])
    return plaintext
# key = code - plain
def vignere_key(text, code):
    key = ""
    for i in range(len(code)):
        key += rem(code[i], text[i%len(text)])
    return key

# Read the ciphered text from file
with open("encryption.txt", "rb") as f:
    text = f.read().decode("utf-8").strip()
# clean the results file
with open("results.txt", "w") as f:
    f.write('start\n')

target = 'ddc'

def main():
    # Danish text, flag is in text
    with open("words_length_9.txt", "rb") as file:
        words = file.read().decode("utf-8").strip()
    # read for possible first word
    for i in range(0, len(words), 10):
        word = ''
        for x in range(0, 10):
            word += clean_input(words[i+x])
        # generate and check key
        key = vignere_key(word[:6],text[:6])
        decrypt = vignere_decrypt(key, text[:9])
        if decrypt[:9] == word[:9]:
            # if this passes there's a potential key
            decipheredtext = vignere_decrypt(key, text)
            if target in decipheredtext: #check for DDC
                with open('results.txt', 'ab+') as file:
                    file.write(("\n" + key + "\n").encode('utf-8'))
                    file.write(decipheredtext.encode('utf-8'))


        #ciphertext = vignere_encrypt(key, text)
        #if target in ciphertext:
        #    with open('results.txt', 'ab+') as file:
        #        file.write(("\n" + key + "\n").encode('utf-8'))
        #        file.write(ciphertext.encode('utf-8'))


    # Once you have decrypted the ciphertext, remember to add flag formatting
    # For example:
    # ddc example flag
    # to
    # ddc{example_flag}


if __name__ == '__main__':
    main()
