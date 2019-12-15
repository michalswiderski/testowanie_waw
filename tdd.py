# def func(a, b):
#     return a / b


# if func(10, 5) == 2:
#     print("Passed")
# else:
#     raise Exception("Failed")
#
# if func(10, 2) == 5:
#     print("Passed")
# else:
#     raise Exception("Failed")

# assert func(10, 5) == 2, "Failed"
# print("Passed")
# assert func(10, 2) == 5, "Failed"
# print("Passed")
# assert func(10, 2) == 4, "Dupa"
# print("Passed")
#
# # syntax sugar
# Asercje nie służą tylo do testowania
#
# def func(a, b):
#     return (a + b) ** 2
#
#
# assert func(2, 2) == 16, "Błąd"
# print("Poszło")
# assert func(10, 5) == 225, "Błąd"
# print("Poszło")
# assert func(10, 5) == 180, "Błąd"
# print("Poszło")

# def func1(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("Nie można dzielić przez zero")
#
# func1(5, 0)

# def func1(a, b):
#     assert b != 0, "Nie można dzielić przez zero"
#     return a / b
#
# func1(5, 0)

def func(str1, str2):
    return str1 + str2


assert func("Nie można", " dzielić przez zero.") == "Nie można dzielić przez zero.", "FAILED1"
# assert func("Nie można1", " dzielić przez zero.") == "Nie można dzielić przez zero.", "FAILED2"
# assert func(1, 10) == "Nie można dzielić przez zero.", "FAILED3"
assert func("", "") == "Nie można dzielić przez zero.", "FAILED4"
