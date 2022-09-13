"""
Patrick Robinson
9/9/22

This code calculates how much money you owe in taxes based on your income
"""
import sys


taxOwed = 0.0

earnedIncome = float(input("Enter the amount of income you earned in 2022: "))
if earnedIncome < 0:
	print("You made less than $0. Contact an accountant")
	sys.exit()

print("Are you married or single?")
maritalStatus = input("Type m for married and s for single: ")


#Ensures you have a valid marital status
while maritalStatus != "m" and maritalStatus != "s":
	print("you entered an invalid marital status")
	maritalStatus = input("Type m for married and s for single: ")




# Your code goes here
if maritalStatus=="s" :  #Detects marital status
	if earnedIncome<= 10275:
		earnedIncome=earnedIncome*.1  #Applys tax rate to income
		taxOwed=earnedIncome  #Calculates how much you owe
		print("This year you owe", taxOwed, "in taxes" )
	if(earnedIncome >= 10276 and earnedIncome <= 41775):
		earnedIncome=(10275*.1)+(earnedIncome-10275)*.12
		taxOwed=earnedIncome
		print("This year you owe", taxOwed, "in taxes" )
	if(earnedIncome >= 41776 and earnedIncome <= 89075):
		earnedIncome=(41775*.12)+(earnedIncome-41775)*.22
		taxOwed=earnedIncome
		print("This year you owe", taxOwed, "in taxes" )
	if(earnedIncome >=89076):
		print("You made too much for this calculator. Hurray! ")
	

if maritalStatus=="m" : #Detects marital status
	if earnedIncome <= 20550 : 
		earnedIncome=earnedIncome*.1 #Applys tax rate to income
		taxOwed=earnedIncome #Calculates how much you owe
		print("This year you owe", taxOwed, "in taxes" )
	if (earnedIncome >=20551 and earnedIncome <=83550) :
		earnedIncome=(20550*.1)+(earnedIncome-20550)*.12 
		taxOwed=earnedIncome
		print("This year you owe", taxOwed, "in taxes" )
	if(earnedIncome >=83551 and earnedIncome<=178150) :
		earnedIncome=(83550*.12)+(earnedIncome-83550)*.22
		taxOwed=earnedIncome
		print("This year you owe", taxOwed, "in taxes" )
	if (earnedIncome>=83551):
		print("You made too much for this calculator. Hurray! ")
