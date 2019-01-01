import codecs

def is_hex(s):
    hex_digits = set("0123456789abcdef")
    for char in s:
        if not (char in hex_digits):
            return False
    return True

hex_string = str(input("Input Your Hexadecimal Code Here: "))

while is_hex(hex_string) is False:
    hex_string = str(input("That was not Hex, Input ONLY Hexadecimal Here: "))

hexdecoded = codecs.decode(hex_string, "hex")

b64 = codecs.encode(codecs.decode(hex_string, "hex"), 'base64').decode()

print("Your decoded Hex is: " + str(hexdecoded)[2:])

print("Your encoded Base64 is: " + str(b64))
