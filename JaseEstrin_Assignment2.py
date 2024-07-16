# %%
for n in range(1, 11):
    print(n)


# %%
name_list = ["Bruno", "Lara", "Aidan", "Tiara"]
for name in name_list:
    print(f"Hello {name}")


# %%
num_list = [1, 4, 5, 7, 10]
sum = 0
for num in num_list:
    sum = sum + num
print(sum)


# %%
my_string = "python"
new_string = ""
for i in reversed(my_string):
    new_string = new_string + i
print(new_string)   


# %%
string = "banana"
dictionary = {}
for key in string:
    dictionary[key] = string.count(key)
print(dictionary)


# %%
student_info = {
    "Josh": 72,
    "Elizabeth": 42,
    "Josiah": 94,
    "Hunter": 59
}
for key in student_info:
    if student_info[key] > 60:
        print(f"{key} passed with a grade of {student_info[key]}")


# %%
n = 5
for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")


# %%
i = 1
while i < 11:
    print(i)
    i += 1


# %%
on = True
while on:
    resp = input("Enter your name or quit").lower()
    if resp == "quit":
        on = False
        print("Goodbye")
        break
    else:
        print(f"Hello, {resp}")


# %%
userinput = int(input("Enter number: "))
if ((userinput % 2) == 0):
    print(f"{userinput} is even.")
else:
    print(f"{userinput} is odd.")


# %%
ran_list = []
import random
for i in range(1, 11):
    ran_list.append(random.randrange(1, 101, 1))
print(ran_list)
large_val = ran_list[0]
small_val = ran_list[0]
for i in ran_list:
    if i > large_val:
        large_val = i
print(large_val)
for i in ran_list:
    if i < small_val:
        small_val = i
print(small_val)


# %%
on = True
fruit_list = ["apples", "bananas", "oranges"]
fruit_dict = {}
for key in fruit_list:
    fruit_dict[key] = random.randrange(4, 10, 1)
while on:
    fruit_resp = input("Enter fruit name: ").lower()
    if fruit_resp == "apples":
        print(fruit_dict[fruit_resp])
    elif fruit_resp == "bananas":
        print(fruit_dict[fruit_resp])
    elif fruit_resp == "oranges":
        print(fruit_dict[fruit_resp])
    else:
        print("Sorry, we don't have that fruit.")

