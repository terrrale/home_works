def print_params(a = 1, b = 'строка', c = True):
    print(f'a: {a}, b: {b}, c: {c}')
# print_params()
# # print_params(2, 'not', False, 2)
# print_params(c = [1,2,3])
# print_params(b=25)
values_list = [2, 'text']
values_list2 = [14, False]
values_dict ={"c": True}
print_params(*values_list, **values_dict)
print_params(*values_list2, 42)