import random
def encrypt(key,plain):
    offset =  key%26
    cipher = ""
    for i in range(len(plain)):
        c = plain[i]
        if c.isalpha():
            if c>='a' and c<='z':
                c = chr(ord('a') +((ord(c)-ord('a')+offset)%26))
                cipher+= c
            else:
                c = chr(ord('A') + ((ord(c) - ord('A') + offset) % 26))
                cipher += c
        elif c.isdigit():

            c = chr(ord('0') + ((ord(c) - ord('0') + offset) % 10))

            cipher += c
        else:
            cipher += c

    return cipher

def decrypt(key,cipher):
    offset =  key%26
    plain = ""

    for i in range(len(cipher)):
        c = cipher[i]
        if c.isalpha():

            if c>='a' and c<='z':
                c = chr(ord('z') -(ord('z')-ord(c)+offset)%26)
                plain += c
            else:
                c = chr(ord('Z') - (ord('Z') - ord(c)+ offset) % 26)
                plain += c
        elif c.isdigit():

            c = chr(ord('9') - (ord('9') - ord(c) + offset) % 10)
            plain += c
        else:
            print("%s nn" % (c))
            plain += c

    return plain


def main():
    plain = "{'yheajp_ez': 'Wheya', 'yheajp_wzznaoo': '349.2.2.3', 'peia_opwil': 3709316501.7715500, 'hebapeia': 822, 'Gw_x': 7287}"

    key = 146831
    a= encrypt(key,plain)
    print(a)
if __name__=="__main__":
    main()