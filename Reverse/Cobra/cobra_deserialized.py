from Crypto.Cipher import AES
import base64

def check(serial):
    expressions = [
     '1790 + 1543', '1234 * 3', '9999 - 1337', '2048 // 2', '3 ** 8']
    for index, value in enumerate(serial.split('-')):
        if eval(expressions[index]) != int(value):
            return False

    return True


def generate_flag(serial):
    cipher = AES.new(serial, AES.MODE_ECB)
    decoded = cipher.decrypt(base64.b64decode('0P8pV0G6WlqUxuuKNk+y4N5PTfamGAln9gDhXDxi5rM='))
    return decoded.strip()


serial = raw_input('enter serial: ')
if check(serial):
    print generate_flag(serial) 
