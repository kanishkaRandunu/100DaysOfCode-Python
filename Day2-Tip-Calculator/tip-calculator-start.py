#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print('Welcome to the tip calculator!')
tot_bill = float(input("What was the total bill? "))
tip = int(input("What is the prefered tip? "))
ppl = int(input("How many people? "))

price_pp = (tot_bill * (1+(tip/100))) / ppl
output = round(price_pp,2)

print(f"Each person should pay: {output}")