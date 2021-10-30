height = float(input('enter your height in m: '))
wight = float(input('enter your weight in kg: '))

bmi = round(wight / height ** 2)
if bmi < 18.5:
    print(f'Your bmi is {bmi}, you are underweight!')
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal wight.")
elif bmi < 30:
    print(f'Your bmi is {bmi}, you are overweight!')
elif bmi < 35:
    print(f'Your bmi is {bmi}, you are obese!')
else:
    print(f'Your bmi is {bmi}, you are clinically obese!')
