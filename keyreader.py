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


# Read the key from file
with open("encryption.txt", "rb") as f:
    text = f.read().decode("utf-8").strip()

# Test decrypt
target = 'ddc'
print(vignere_decrypt('klmraå', text))

# Test key
print(vignere_key('velkommen', 'cpxøolwpz'))