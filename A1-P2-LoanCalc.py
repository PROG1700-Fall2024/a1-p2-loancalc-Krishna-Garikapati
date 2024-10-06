"""Student Name:Krishna Priyanka Garikapati
Student number:W0502117
Assignment#1
program#2"""

#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 

########################################Pseudocode##############################################
#enter the rate of interest using input command and assign it to variable r. Change datatype to float.
#enter the dollars borrowed using input command and assign it to variable A. Change datatype to float.
#Enter the years for to repay total amount using input command and assign variable n. Change datatype to float.
#store r/5200 in variable i.
#store (1+i) power -52n in x
#WeeklyPayment=(i/(1-x))*A
#using print command print weeky payment in dollars with two decimal places

def main():
    r=float(input("Enter the percentage of rate at which money is borrowed:"))
    A=float(input("Enter the total amount of money borrowed: $"))
    n=float(input("Enter the years to repay amount borrowed:"))
    i=(r/5200)
    x=pow((1+i),(-52*n))
    #To make calculation little easier variable x is introduced.
    WeeklyPayment=(i/(1-x))*A
    print("Weekly payment is ${0:.2f}".format(WeeklyPayment))
    
main()