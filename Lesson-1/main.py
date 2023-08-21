# -1-
print("---")
nums = [1, 2, 3, 4, 5]
total = 0

for num in nums:
    total +=num
    print(total) # 1, 3, 6, 10, 15

# -2-
print('---')
nums = [3, 8, 1, 9, 4]
max_num = nums[0]

for num in nums:
    if num > max_num:
        max_num = num

print(max_num) # 9

# -3-
print('---')
n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial) # 120

a = "Hello"
b = "panda"
c = 51

a,b = b,a
print(a, b, c)

# -Просто функция для отработки input() и print()
def user_auth():
    start = True
    while (start):
        name = input("Please, enter your NAME: ")
        surname = input("Please, enter your SURNAME: ")

        # надо отметить, что в python (в отличие от C# оператор && - and; оператор || - or)
        if (name != "" and surname != ""):
            print("Your name is: ", name, "Your surname is: ", surname)
            start = False
            break
        else:
            print("Please restart this app again!")

user_auth()

print("Answer to the Ultimate Question of Life, the Universe, and Everything —", 42)
# Ответ на главный вопрос жизни, вселенной и всего такого — 42

print("Число PI: ", 3.14159)
# Число PI: 3.14159

# Еще небольшой пример работы с input() и print()
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
age = input("Enter your age:")
city = input("Enter your city of residence:")

print("")
print("Hello,", first_name, last_name, "!")
print("")
print("Your profile:")
print("Age:", age, "years")
print("City:", city)