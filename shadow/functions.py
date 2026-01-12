from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
import base64

# Generate key with optional seed
def generate_fernet_key(seed: bytes | None = None) -> bytes:
        if not seed:
            return Fernet.generate_key()

        digest = hashes.Hash(hashes.SHA256())
        digest.update(seed)
        key = digest.finalize()
        return base64.urlsafe_b64encode(key)


# Encrypt message using the key
def encrypt(key, text):
        fernet = Fernet(key)
        return str(fernet.encrypt(bytes(text, "utf-8")))[2:-1]


# Decrypt message using the key
def decrypt(key, text):
    fernet = Fernet(key)
    try:
        return str(fernet.decrypt(bytes(text, "utf-8")))[2:-1]
    except Exception:
        return "Wrong key!"


# Converting text to binary
def text_to_binary(key, text):
    return ' '.join(format(ord(char), '08b') for char in encrypt(key, text))


# Converting binary to text
def binary_to_text(key, binary):
    return decrypt(key, ''.join(chr(int(byte, 2)) for byte in binary.split()))


# Converting binary to zero width characters 0 => "\u200B", 1 => "\u200C" and " " => "\u200D"
def binary_to_zero_width(binary):
    lista = []
    for bit in binary:
        if bit == '0':
            lista.append("\u200B")
        elif bit == '1':
            lista.append("\u200C")
        elif bit == ' ':
            lista.append("\u200D")
    lista.reverse()
    return lista


# Converting zero width characters to binary "\u200B" => 0, "\u200C" => 1 and "\u200D" => " "
def zero_width_to_binary(text):
    lista = []
    for bit in text:
        if bit == "\u200B":
            lista.append('0')
        elif bit == "\u200C":
            lista.append('1')
        elif bit == "\u200D":
            lista.append(' ')
    return ''.join(lista)  # return the zero-width as text


# Hide the real message into the mask message after the first character
def hide(key, message, mask):
    msg_binary = text_to_binary(key, message)  # convert message to binary
    msg_hide = binary_to_zero_width(msg_binary)  # convert binary to zero-width characters
    mask_list = list(mask)  # convert mask message to list
    for bit in msg_hide:
        mask_list.insert(1, bit)  # insert the zero-width characters into mask message
    return ''.join(mask_list)    


# Extracting the real message from the combined message
def extract(key, message):
    flag = 0
    for char in message:
        if not char.isalpha() and not char.isdigit():  # check if the message contains zero-width characters
            flag = 1
            break
    if flag:
        msg_binary = zero_width_to_binary(message)  # convert the zero-width characters to binary
        return(binary_to_text(key, msg_binary))  # show the extracted message in the output entry
    else:
        return("No hidden message")