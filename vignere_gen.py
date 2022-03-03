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

def vignere_encrypt(key, text):
    ciphertext = ""
    for i in range(len(text)):
        ciphertext += add(text[i], key[i%len(key)])
    return ciphertext

# Read the key from file
with open("encryption.txt", "rb") as f:
    text = f.read().decode("utf-8").strip()

target = 'ddc'

def main():
    # Danish text, flag is in text
    with open("keys_clean.txt", "rb") as file:
        keys = file.read().decode("utf-8").strip()
    for i in range(0, len(keys), 7):
        key = clean_input(keys[i])+clean_input(keys[i+1])+clean_input(keys[i+2])+clean_input(keys[i+3])+clean_input(keys[i+4])+clean_input(keys[i+5])
        ciphertext = vignere_encrypt(key, text)
        if target in ciphertext:
            with open('results.txt', 'ab+') as file:
                file.write(("\n" + key + "\n").encode('utf-8'))
                file.write(ciphertext.encode('utf-8'))


    # Once you have decrypted the ciphertext, remember to add flag formatting
    # For example:
    # ddc example flag
    # to
    # ddc{example_flag}


if __name__ == '__main__':
    main()
