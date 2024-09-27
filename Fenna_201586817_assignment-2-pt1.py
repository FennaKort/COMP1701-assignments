# test of writing Assignment2pt1 algorithm and manual calculations as python code
# pension calculator inputs:
RATE = 0.014
# worker's current age:
current_age = float(input("What is your current age? "))
# worker's current years of service:
current_years_of_service = float(input("What are your current years of pensionable service? "))
expected_retirement_age = float(input("What age do you expect to retire at? ")) # for the purposes of assignment2pt1, use age 65

# years of service at retirement calculation:
years_of_service_at_retirement = expected_retirement_age-current_age+current_years_of_service
print("At retirement you will have "+str(int(years_of_service_at_retirement))+" years of pensionable service.")
    # print function to check if variable has been assigned the correct value, not necessary to display to end user - decided to convert it into a print function that WOULD display the information to the end user in a useful way

# worker's largest three expected incomes:
print("What are your three largest expected annual incomes?")
# three_largest_expected_incomes = input("income 1: $")+input("income 2: $")+input("income 3: $") 
    # RIGHT because if I do it like this it just concatenates the strings lol
average_of_three_largest_expected_incomes = (float(input("income 1: $")) + float(input("income 2: $")) + float(input("income 3: $")))/3
# print(average_of_three_largest_expected_incomes)
    # print function to check if variable has been assigned the correct value, not necessary to display to end user

# pension income calculation:
pension_income = average_of_three_largest_expected_incomes*RATE*years_of_service_at_retirement
# print("Your expected yearly pension income at retirement is $"+str(pension_income))
    # this prints the correct output for the pt1 inputs, but needs to be formatted in order to display the correct level of decimal precision
    # I previously cast the value assigned to pension_income to a string during assignment, but have decided against that in order to use f-string formatting as per below:
print(f"Your expected yearly pension income at retirement is ${pension_income:.2f}")
    # prints expected pension income as a float with the correct level of precision to display dollars and cents