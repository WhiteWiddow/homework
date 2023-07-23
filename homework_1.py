def check_palindrom(a):
    return a == a[::-1]
a = 'аргентинаманитнегра'
b = 'червячок'
print(check_palindrom(a))
print(check_palindrom(b))