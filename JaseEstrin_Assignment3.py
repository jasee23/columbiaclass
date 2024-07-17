# %%

def is_palindrome(string: str) -> bool:
    empt_string = ""
    for i in reversed(string):
        empt_string += i
    if string == empt_string:
        return True
    else:
        return False
    
print(is_palindrome("racecar"))
print(is_palindrome("tacocat"))
print(is_palindrome("car"))
# %%

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
r = Rectangle(3, 4)

print("Area", r.area())
print("Perimeter", r.perimeter())

# %%

word_list = ["hello", "world", "hello", "python"]

def count_words(word_list: list) -> dict:
    word_count = {}
    for key in word_list:
        word_count[key] = word_list.count(key)
    return word_count

print(count_words(word_list))

