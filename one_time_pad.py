import random

plaintext = input("Enter your message: ")
ciphertext = ""
key = ""

def xor(s1, s2, keylen):
    out:str = ""
    for i in range(keylen):
        if (s1[i] == s2[i]): out += "0"
        else : out += "1"
    
    return out

def cipher(p:str):
    binP:str = format(abs(hash(p)), "b")
    keylen = len(binP)
    global key
    key = "".join([str(random.randint(0, 1)) for _ in range(keylen)])
    # print(f"{binP=}")
    # print(f"{key=}")
    return xor(binP, key, keylen)

def decipher(c:str, key:str):
    bin_string = xor(c, key, len(key))
    # plaintext = "".join([chr(int(bin_message[i:i+8],2)) for i in range(0,len(bin_message),8)])
    binary_int = int(bin_string, 2);
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    
    plaintext = ""
    for enc in ['utf-8', 'ascii', 'ansi']:
        try:
            plaintext = binary_array.decode(encoding=enc)
            break
        except:
            pass

    return (plaintext)

ctext = cipher(plaintext)
print(decipher(ctext, key))





