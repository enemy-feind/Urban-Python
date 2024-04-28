def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a=3)
print_params(b='str')
print_params(c=False)
print_params(a=3, b='str')
print_params(a=3, c=False)
print_params(a=3, b='str', c=False)
print_params(b='str', c=False)
#print_params(b = 25)
#print_params(c = [1,2,3])

values_list = [5, 'word', False]
values_dict = {'a': 17, 'b': 'seventeen', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = []
print_params(*values_list_2, 42)
