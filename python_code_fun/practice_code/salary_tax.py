#Salary Tax Calculator

salary = float(input("Enter annual salary: "))

if salary >= 500000:
    tax = salary * 0.10
elif salary >= 300000:
    tax = salary * 0.05
else:
    tax = 0

print("Tax to pay:", tax)
print("Net salary:", salary - tax)
