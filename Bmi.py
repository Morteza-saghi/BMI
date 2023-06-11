weight = float(input("please enter your weight in KG: "))
height = float(input("please enter your height in CM: "))
BMI = weight // height**2

if BMI < 18.5:
    print("you are underweight")
elif 18.5 < BMI < 24.9:
    print("you are normal")

elif 25 < BMI < 29.5:
    print("you are overweight")

elif 30 < BMI < 34.9:
    print("you are obese")

elif BMI > 35:
    print("you are exeteremly obese")
