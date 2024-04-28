immutable_var = ('uno', True, 123)
print(immutable_var)
#immutable_var[2] = '123' - Не будет выполненно, тк это "кортеж", а не обычный список.
mutable_list = [1, 'two', 'three']
mutable_list[0] = 2
mutable_list[1] = 'one + 2'
mutable_list[2] = 'one + 3'
print(mutable_list)