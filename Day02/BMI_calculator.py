height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
result = round(weight/(height*height),2)
print(f"Your BMI is equal to {result}")