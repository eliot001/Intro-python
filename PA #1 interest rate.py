#Elliott Soelter 
#Sept. 1, 2017
#CptS 111
#PA #1
#Student loan calculator 
#no commas in amount owe
#interest rate needs to be a fraction
#whereas (int_rate/1200) is to get the interest rate into a percent form and then divide by number of years. 


amount_owe = float(input('Enter the amount you owe: '))   #Principle loan amount
int_rate = float(input('Enter the interest rate [%]:'))   #Annual interest rate divided by 100
num_years = float(input('Enter the number of years you want to spend to pay back loan: '))   #number of years

monthly_pmt = ( ((amount_owe)*(int_rate/1200)) / (1 - (1 + (int_rate/1200) ) ** (-num_years*12) ) )
total_pmt = ((monthly_pmt)*(num_years*12))
interest_total = (total_pmt - amount_owe) 

print('Your monthly payment is $', round(monthly_pmt,2))
print('The total amount you ended up paying is $',round(total_pmt,2))
print('The total amount of interest you paid is $',round(interest_total,2))
