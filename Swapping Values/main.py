
a = 10
b = 15
c = 120

a, b = b, a # swap values a to be and b to a
print(f"{a=}, {b=}")


a = 10
b = 15
c = 120

a, b, c = c, a, b # swap a -> b, b -> c, c -> a
print(f"{a=}, {b=}, {c=}")