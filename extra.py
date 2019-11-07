def move_zeros(x):

    for i in range(x.count(0)):
        x.remove(0)
        x.append(0)

    return x

print(move_zeros([1,0,3,0,0,5,7]))
