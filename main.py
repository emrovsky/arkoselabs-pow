import random
import string
from hashlib import sha256

def generate_value(long):
    base36_string = ''.join(
        random.choices(string.ascii_lowercase + string.digits, k=long))
    return base36_string


def create_pow():
    iV = 0
    while True:
        iL = generate_value(9)
        uwu = generate_value(11)
        iw = iL + uwu
        im = sha256(iw.encode('utf-8')).hexdigest()

        iS = random.randint(100, 999) # performance.now()
        ia = random.randint(iS, 1500) # performance.now()

        iz = (ia - iS) / 1000  # 0x3e8 is 1000 in decimal
        iV += 1
        if im[:2] == '00':
            break
    iB = iz / iV
    return {
                                                    'cs_': iL, #9 len
                                                    'ct_': iV, #random shit will work too, attempt count
                                                    'g_': uwu, # 11 len
                                                    'h_': im, # sha-256
                                                    'pt_': iz,
                                                    'aht_': iB
                                                }
print(create_pow())
