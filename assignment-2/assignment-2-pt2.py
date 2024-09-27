# pension calculator inputs:
#current_age = input("worker's current age as a whole number is: ")
#current_years_of_service = input("worker's current years of service: ")
print("What are your three largest expected annual incomes?")
# three_largest_expected_incomes = input("income 1: $")+input("income 2: $")+input("income 3: $") 
    # RIGHT because if I do it like this it just concatenates the strings lol
average_of_three_largest_expected_incomes = (float(input("income 1: $")) + float(input("income 2: $")) + float(input("income 3: $")))/3
print(average_of_three_largest_expected_incomes)