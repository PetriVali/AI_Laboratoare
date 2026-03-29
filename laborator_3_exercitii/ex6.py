def fun_odd(x):
    odd_list = [lambda x: x % 2 != 0]
    if x in odd_list:
        return True
    else:
        return False
    
def fun_even(x):
    even_list = [lambda x: x % 2 == 0]
    if x in even_list:
        return True
    else:
        return False
    
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_odd = list(filter(fun_odd, my_list))
filtered_even = list(filter(fun_even, my_list))
