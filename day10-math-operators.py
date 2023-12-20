# Basic Mathematical Operations
# In python, we can perform basic mathematical operations on numbers.
# Operators are symbols that perform operations on numbers. 
# addition_result = 5 + 3
# subtraction_result = 7 - 2
# multiplication_result = 4 * 6
# division_result = 20 / 5
# exponentiation_result = 2 ** 3
# modulo_result = 10 % 3


myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent?"))


bill_with_tip = tip / 100 * myBill + myBill
bill_per_person = bill_with_tip / numberOfPeople
final_amount = round(bill_per_person, 2)


print("You all owe", final_amount)