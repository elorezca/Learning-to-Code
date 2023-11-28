FEDERAL_STANDARD_DEDUCTION = 13200 
STATE_STANDARD_DEDUCTION = {
 'California': 4609,
 'New York': 8000 
}
FEDERAL_TAX_BRACKETS = [
(10400, 0.10),
(41225, 0.12),
(89400, 0.22),
(174050, 0.24),
(215400, 0.32),
(549900, 0.35),
(1000000, 0.37)
]
STATE_TAX_BRACKETS = {
 'California': [
(9076, 0.01),
(22771, 0.02),
(34211, 0.04),
(48898, 0.06),
(48897, 0.08),
(59878, 0.093),
(71805, 0.103),
(100000, 0.113)
],
 'New York': [
(8500, 0.04),
(11700, 0.045),
(13900, 0.0525),
(21400, 0.059),
(80650, 0.0645),
(215400, 0.0685),
(1077550, 0.0882),
(1000000, 0.103)
]
}

def calculate_federal_tax(gross_salary):
    deducted_salary = gross_salary - FEDERAL_STANDARD_DEDUCTION
    federal_tax = 0
    prev_bracket_limit = 0

    for bracket in FEDERAL_TAX_BRACKETS:
        bracket_limit, tax_rate = bracket
        taxable_amount_in_bracket = min(deducted_salary, bracket_limit) - prev_bracket_limit
        federal_tax += taxable_amount_in_bracket * tax_rate
        prev_bracket_limit = bracket_limit

        if deducted_salary <= bracket_limit:
            break

    return federal_tax

def calculate_california_tax(gross_salary):
    deducted_salary = gross_salary - STATE_STANDARD_DEDUCTION['California']
    state_tax = 0
    prev_bracket_limit = 0

    for bracket in STATE_TAX_BRACKETS['California']:
            bracket_limit, tax_rate = bracket
            taxable_amount_inbracket = min(deducted_salary, bracket_limit) - prev_bracket_limit
            state_tax += taxable_amount_inbracket * tax_rate
            prev_bracket_limit = bracket_limit

            if deducted_salary <= bracket_limit:
                break

    return state_tax

def calculate_new_york_tax(gross_salary):
    deducted_salary = gross_salary - STATE_STANDARD_DEDUCTION['New York']
    state_tax = 0
    prev_bracket_limit = 0

    for bracket in STATE_TAX_BRACKETS['California']:
            bracket_limit, tax_rate = bracket
            taxable_amount_inbracket = min(deducted_salary, bracket_limit) - prev_bracket_limit
            state_tax += taxable_amount_inbracket * tax_rate
            prev_bracket_limit = bracket_limit

            if deducted_salary <= bracket_limit:
                break
    return state_tax
    
def calculate_fica(gross_salary):
    fice_rate = 0.0765
    fica_limit = 147000
    return min(gross_salary * fice_rate, fica_limit)

Gross_Salary = float(input("Please enter you gross salary: "))
state = input("Please enter the sate you live in (California or New York): ")

federal_tax = calculate_federal_tax(Gross_Salary)
state_tax = 0

if state == 'California':
    state_tax = calculate_california_tax(Gross_Salary)
elif state == 'New York':
    state_tax = calculate_new_york_tax(Gross_Salary)

fica = calculate_fica(Gross_Salary)

net_salary = Gross_Salary - federal_tax - state_tax - fica

print(f"Gross Salary: ${Gross_Salary:.2f}")
print(f"Federal Tax: ${federal_tax:.2f}")
print(f"State Tax: ${state_tax:.2f}")
print(F'FICA: ${fica:.2f}')
print(F"Net Salary: ${net_salary:.2f}")