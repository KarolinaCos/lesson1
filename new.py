
def get_summ(one, two, delimeter="&"):
    my_string = one + delimeter + two

    return my_string


a = get_summ('aa', 'bb')

print(a)

a = get_summ("Learn", "python")
print(a)
