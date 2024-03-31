import assets

print(assets.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
exit = False
direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, mode):
    result_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            if mode == 'encode':
                new_index = (index + shift) % len(alphabet)
            elif mode == 'decode':
                new_index = (index - shift) % len(alphabet)
            result_text += alphabet[new_index]
        else:
            result_text += char
    return result_text

print(caesar(text = text, shift = shift, mode = direction))