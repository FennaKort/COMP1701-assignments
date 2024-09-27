# pension calculator inputs:
RATE = 0.014
RETIREMENT_AGE_55 = 55
RETIREMENT_AGE_60 = 60
RETIREMENT_AGE_65 = 65
# worker's current age:
current_age = float(input("enter current age in years: "))
# worker's current years of service:
current_years_of_service = float(input("enter current years of service: "))

# worker's largest three expected incomes:
average_of_three_largest_expected_incomes = (float(input("enter the largest expected annual income:")) + float(input("enter the second-largest expected annual income:")) + float(input("enter the third-largest expected annual income:")))/3
# print(average_of_three_largest_expected_incomes)
    # print function to check if variable has been assigned the correct value, not necessary to display to end user

# pension income if retiring at 55:
pension_income_retirement_age_55 = average_of_three_largest_expected_incomes*RATE*(RETIREMENT_AGE_55-current_age+current_years_of_service)
# pension income if retiring at 60:
pension_income_retirement_age_60 = average_of_three_largest_expected_incomes*RATE*(RETIREMENT_AGE_60-current_age+current_years_of_service)
# pension income if retiring at 65:
pension_income_retirement_age_65 = average_of_three_largest_expected_incomes*RATE*(RETIREMENT_AGE_65-current_age+current_years_of_service)

# table headers
RETIREMENT_AGE_HEADING = "retirement age"
RETIREMENT_INCOME_HEADING = "retirement income"

# output 
print(f"{RETIREMENT_AGE_HEADING:20}{RETIREMENT_INCOME_HEADING:20}")

print(f"{RETIREMENT_AGE_55:<20}${pension_income_retirement_age_55:<20,.2f}")

print(f"{RETIREMENT_AGE_60:<20}${pension_income_retirement_age_60:<20,.2f}")

print(f"{RETIREMENT_AGE_65:<20}${pension_income_retirement_age_65:<20,.2f}")
    # prints expected pension income as a float with the correct level of precision to display dollars and cents