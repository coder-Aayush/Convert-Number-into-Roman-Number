roman_num = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
userinput = int(input("Enter Number: "))
def romanConverter(num):

    roman = ''

    while num > 0:
        for i, r in roman_num:
            while num >= i:
                roman += r
                num -= i

    return roman

result = romanConverter(userinput)
print("Your Number {} in Roman Number => {}".format(userinput, result))
