from string import ascii_lowercase

def printer_error(s):
    letters = ascii_lowercase[13:]# n to z
    errors = 0
    for l in letters:
        errors += s.count(l)

    return f'{errors}/{len(s)}'


s = 'aaabbbbbbbcccccccdegggxxxxxxxxx'
x = printer_error(s)
print(x)