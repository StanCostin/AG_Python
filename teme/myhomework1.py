# define list

lst = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# sort list in ascending order without modify the list

l1 = sorted(lst)

# print sorted list in ascending order

print(l1)

# sort in descending order without modify the list

l1.reverse()

# print list

print(l1)

# print the even numbers in a list

even = l1[::2]
print(sorted(even))

# print the odd numbers in a list

odd = l1[1::2]
print(sorted(odd))

# print numbers of multiple of 3 in a list

multi = [y for y in l1 if y % 3 == 0]
sm = sorted(multi)
print(sm)
