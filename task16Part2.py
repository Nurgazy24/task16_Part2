def func(x):
    if x < 0:
        return -1
    elif x == 0:
        return x     
    else:
        return 1

list_ = [-4, -3, -2, -1, 0,  1, 2, 3, 4]
end_list = list(map(func, list_))
print(end_list)