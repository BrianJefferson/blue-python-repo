# Salary calculator
#Ask the user for the number of hours they worked last month and their hourly rate (both numbers should be floats). Use the following prompts:
#How many hours did you work last month? << add a space at the end of this prompt
#What is your hourly rate? << add a space at the end of this prompt
#Then, show the following message with the calculated salary:
#Last month, you earned {hours * hourly_rate} dollars
#The salary should be shown as a float number. For example, for input 30 hours and hourly rate 10.5, show:
#Last month, you earned 315.0 dollars




hours = float(input('How many hours did you work last month? '))
rate = float(input('What is your hourly rate? '))

print('Last month, you earned', hours * rate ,'dollars')