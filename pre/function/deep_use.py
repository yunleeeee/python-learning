def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result

def add(x, y):
    return x + y


def mul(x, y):
    return x * y

print(calc(0, add, 1, 2, 3, 4, 5))  # 15



#sort
old_string = ['in','out','subs','qb']
new_string = sorted(old_string)
print(new_string)
new_string = sorted(old_string,key = len)
print(new_string)
