import math # initializes the math functions built into python, necessary before using more advanced math module functions
number = float(input("type a whole number bigger than one:" + " "))
counter = 1
result =  math.sqrt(12)
print(result)
while counter < number:
    term = (math.sqrt(12))/(((-3) **counter) * (2 * counter + 1))
    print(term)
    result = term + result
    print(result)
    counter = counter + 1
    print(counter)
print("the final result is" + " " + str(result))