def add_everything_up(a, b):
    try:
        if type(a) == int and type(b) == float or type(a) == float and type(b) == int:
            return format(a + b, '.3f')
        else:
            return a + b
    except TypeError:
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

