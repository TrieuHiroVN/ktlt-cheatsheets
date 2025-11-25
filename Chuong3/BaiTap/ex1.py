# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
# hourly rate for hours worked above 40 hours.

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hours > 40:
    overtime_hours = hours - 40
    pay = (40 * rate) + (overtime_hours * rate * 1.5)
else:
    pay = hours * rate

print("Pay:", pay)