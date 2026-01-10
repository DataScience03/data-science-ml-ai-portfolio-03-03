#salary alayser

'''Take number of employees
Store salaries in a list
Calculate:
Total payout
Average salary
Highest salary
Lowest salary'''



salaries = []

employees = int(input("enter a number of emp: "))


for i in range(1, employees+1):
    salary = float(input(f"enter a salary of employee {i}: "))
    salaries.append(salary)
    
    
total_payout = sum(salaries)
ave_salary = total_payout/len(salaries)
highest_salary = max(salaries)   
lowest_salary = min(salaries)

print("\n ====salary alayzer=======\n")
print("\n enter a emp:", employees)
print("total_payout:", total_payout)
print("ave_salary", round(ave_salary,2))
print("highest_salary:", highest_salary)
print("lowest_salary: ",lowest_salary)
