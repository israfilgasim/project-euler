dic = {
    0 : '',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eigth',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
    100 : 'hundred',
    1000 : 'thousand'
}

length = ''

for i in range(1, 1001):
    if i in range(1, 21):
        length += dic[i]
    elif i in range(21, 100):
        a = i % 10
        length += dic[a]
        b = i - a
        length += dic[b]
    elif i in range(100, 1000):
        a = i % 100
        if a in range(1, 21):
            length += dic[a]
        if a in range(21, 100):
            b = a % 10
            length += dic[b]
            c = a - b
            length += dic[c]
        i = i // 100
        length += dic[i]
        if a == 0:
            length += dic[100]
        else:
            length += 'hundredand'
    else:
        length += dic[1]
        length += dic[1000]

print(len(length))

# answer: 21124