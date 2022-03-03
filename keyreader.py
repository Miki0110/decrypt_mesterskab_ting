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
print(vignere_encrypt('tsrmab', text))