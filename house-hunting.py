total_cost = float(input("How much is your dream home? "))
portion_down_payment = .25
current_savings = 0
r = .04
annual_salary = float(input("How much do you make per year? "))
portion_saved = float(input("What portion of your salary will you save towards the down payment? (enter as a decimal) "))
counter = 0

while current_savings < (total_cost * portion_down_payment):
    counter += 1
    current_savings += (current_savings * r / 12)
    current_savings += (annual_salary * portion_saved / 12)

print(counter)