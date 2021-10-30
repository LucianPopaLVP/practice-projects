height = input('enter your height in m: ')
wight = input('enter your weight in kg: ')

bmi = int(wight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)