# this block of code will convert centimeters to meters
def convert_cm_to_m(cm: int):
    formula = int(cm) / 100
    return formula


user_input = int(input("Please enter a value in cm "))

call_function = convert_cm_to_m(user_input)

print(call_function)


# this code will convert meters to feet
def convert_m_to_ft(m: float):
    formula = float(m) * 3.281
    return formula


user = float(input("Please enter a value in meters "))

new_function = convert_m_to_ft(user)
print(new_function)
