#%%
name = "Jase Estrin"
print(name)

#%%
age = 16
print(age)

height = 1.8542
print(height)

print(age + height)
print(age * height)
print(age / height)

#%%
intro = name + " " + str(age)
print(intro)

print(intro.upper())
print(intro.lower())
print(intro.title())
print(intro.swapcase())

#%%
hobbies = ["ice hockey", "video editing", "movies"]
print(hobbies)

hobbies.append("running")
print(hobbies)

hobbies.remove("ice hockey")
print(hobbies)

hobbies.reverse()
print(hobbies)

hobbies.sort()
print(hobbies)

#%%
profile = {
    "Name": name,
    "Age": age,
    "Height": height,
    "Hobbies": hobbies
}
print(profile)

profile["Favorite Color"] = "blue"
print(profile)

profile.pop("Height")
print(profile)

print(profile.get("Hobbies"))

profile.update({"Age":17})
print(profile)
