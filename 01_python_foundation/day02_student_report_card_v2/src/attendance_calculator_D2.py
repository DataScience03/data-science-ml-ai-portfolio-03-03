#attendance calculator


'''P = Present

A = Absent

Eligibility ≥ 75%'''


attendance =[]

days = int(input("enter a days present: "))



for day in range(1,days + 1):
    status =input(f"days precent{day} (P/A): ").upper()
    attendance.append(status)
    
precent_days = attendance.count("P")  
absent_days = attendance.count("A")


# total_dayspresent = precent_days/attendance
percentage = (precent_days/days)*100


if percentage >= 75:
    print("eligible")
    
else:
    print("not eligibible")
    
    
print("\n====calculate the values===")
print("days", days)
print("precent_days:", precent_days)
print("absent_days:", absent_days)
# print("total_dayspresent:", total_dayspresent)
print("percentage:", percentage) 
       
