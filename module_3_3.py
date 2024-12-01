def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)
print_params()
print_params(224, 'Urban', False)
print_params(25, 'num')
print_params(23)
print_params(b = 25)
print_params(c = [1,2,3])
print('---------------------------------')



value_list = [15, 'string', False]
value_dict = {'a': 5, 'b': 7, 'c': 12}
print_params(*value_list)
print_params(**value_dict)
print('---------------------------------')


value_list_2 = [54.32, 'string']
print_params(*value_list_2)
