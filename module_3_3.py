#1
def print_params (a = 1, b = 'строка', c = True):
    print (a,b,c)

print_params (b = 25)
print_params(c = [1,2,3])


#2
values_list = [False, 2, 'cool']
values_dict = {'a': 1, 'b': 'строка','c': True}
print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = [4, 'Black']
print_params(*values_list_2, 42)


