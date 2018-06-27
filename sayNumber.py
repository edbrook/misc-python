#!/usr/bin/env python3

units = ['zero','one','two','three','four',
    'five','six','seven','eight','nine']

specials = ['eleven','twelve','thirteen','fourteen',
    'fifteen','sixteen','seventeen','eighteen','nineteen']

tens = ['ten','twenty','thirty','fourty','fifty',
    'sixty','seventy','eighty','ninety']

orders = ['','thousand','million','billion','trillion',
    'quadrillion','quintillion','sextillion']

def say(num):
    if num < 10:
        return units[num]

    words = []
    o = 0
    last_triple = 0
    while num > 0:
        str = "";
        n = num % 1000
        h = n // 100
        t = n // 10 % 10
        u = n % 10

        # Hundreds
        if h > 0:
            str += "{} hundred".format(units[h])

        nm = n%100
        if nm > 0 and  h > 0:
            str += " "

        # Tens
        if 10 < nm < 20:
            str += specials[nm - 11]
        elif t > 0:
            str += tens[t-1]

        # Units
        if u > 0 and (nm < 10 or nm > 20):
            if t > 0:
                str += "-"
            str += "{}".format(units[u])

        # Order
        if nm > 0:
            str += " {}".format(orders[o])
            if o > 0 and last_triple > 0:
                str += ","

        if str:
            words.append(str)

        last_triple = num % 1000
        num //= 1000
        o += 1

    return ' '.join(words[::-1])


if __name__ == '__main__':
    while True:
        try:
            i = int(input("Next Number: "))
            if i < 0:
                break
            print(say(i))
        except Exception as e:
            break
