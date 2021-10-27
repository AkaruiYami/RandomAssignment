min_value = 10
max_value = 40

user_value = int(input("$  "))

# if user_value > min_value and user_value < max_value:
#     print("The value is within the range.")
# else:
#     print("The value is outside the range!")

if min_value < user_value < max_value:
    print("The value is within the range.")
else:
    print("The value is outside the range!")