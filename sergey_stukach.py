param = {'weight': 0, 'height': 0}

param['weight'] = int(input("Input your weight (kg): "))
param['height'] = int(input("Input your height (cm): "))
bmi = param['weight'] / ((param['height'] / 100) ** 2)
print(f"Your BMI (body mass index): {bmi:.2f} kg/m2")

max_value = 70
min_value = 10
before = round(bmi) - min_value
after = max_value - round(bmi)

print(str(min_value) + '=' * before + '|' + '=' * after + str(max_value))
