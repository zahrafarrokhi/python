n=float(input("Enter your weight in kg:"))
m=float(input("Enter your height in meters:"))
bmi=n/(m**2)

print('%.2f' % bmi)

if bmi < 18.5:
    print('Underweight')
elif 25>bmi>=18.5:
    print('Normal')
elif 30>bmi>=25:
    print('Overweight')
elif bmi >=30:
    print('Obese')

# in 
# 65
# 1.67

# out
# 23.31
# Normal