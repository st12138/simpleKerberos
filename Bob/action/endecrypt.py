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
            plain += c

    return plain


def main():
    plain = "123456"
    #c = plain[0]
    #print(c.isdigit())
    key = 123456
    a= encrypt(key,plain)
    print(a)
if __name__=="__main__":
    main()