
x = [int(x) for x in input().split()]

first = x[0] * x[1] + 2 * x[3]
second = x[0] * x[2] + 2 * x[4]

if first > second:
    print('Second')
elif first < second:
    print('First')
elif first == second:
    print('Friendship')