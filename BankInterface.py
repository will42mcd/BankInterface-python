# Bank Version 1
# Single account
accountName = 'Joe' #defines account name
accountBalance = 100 #current balence 
accountPassword = 'soup' # curret password 
while True: #loops code while password is correct
	print() #prints a line skip
	print('Press b to get the balance') #prints option for balance
	print('Press d to make a deposit') #prints option for deposit 
	print('Press w to make a withdrawal') #prints option for withdrawl 
	print('Press s to show the account') #prints option to show the account
	print('Press q to quit') #prints option to quit 
	print()# prints a line skip
	action = input('What do you want to do? ')# creates the first action in the account 
	action = action.lower() # force lowercase
	action = action[0] # just use first letter
	print()# prints a line skip

	if action == 'b': # imput for user wanting to select balance 
		print('Get Balance:')# prints get balance 
		userPassword = input('Please enter the password: ')# enters password to move forward with account 
		if userPassword != accountPassword:# if statement for if password is incorrect
			print('Incorrect password')# prints incorrect password
		else: # if password is correct
			print('Your balance is:', accountBalance)# shows account balance 
	elif action == 'd':# action for deposit 
		print('Deposit:')# prints deposit 
		userDepositAmount = input('Please enter amount to deposit: ') #asks to input a deposit amount
		userDepositAmount = int(userDepositAmount) #deposit should be an integer  
		userPassword = input('Please enter the password: ') # imput for password
		if userDepositAmount < 0: # if user deposits a negative amount 
			print('You cannot deposit a negative amount!') # print You cannot deposit a negative amount
		elif userPassword != accountPassword: # else if statement for if password is incorrect
			print('Incorrect password') # print incorrect password 
		else: # OK
			accountBalance = accountBalance + userDepositAmount # sets the account after the deposit 
			print('Your new balance is:', accountBalance)# prints new account balance 
	elif action == 's': # show
		print('Show:')#prints show
		print(' Name', accountName)# prints account name
		print(' Balance:', accountBalance)#prints account balance 
		print(' Password:', accountPassword)# prints account password 
		print()# prints line skip

	elif action == 'q':# action imput for quit
		break# breaks loop all together 
	elif action == 'w':# account action for withdrawl 
		print('Withdraw:')# prints withdrawl 
		userWithdrawAmount = input('Please enter the amount to withdraw: ')# action for how much to withdrawl 
		userWithdrawAmount = int(userWithdrawAmount)# sets the imput as an integer 
		userPassword = input('Please enter the password: ')# input for password 
		if userWithdrawAmount < 0:# if statment for when user withdrawls an negative amount 
			print('You cannot withdraw a negative amount')# prints You cannot withdraw a negative amount
		elif userPassword != accountPassword:# else-if statement for when password is incorrect 
			print('Incorrect password for this account')# prints Incorrect password for this account
		elif userWithdrawAmount > accountBalance:# else-if statement for when user attempts to withdrawl more than they have
			print('You cannot withdraw more than you have in your account') #prints You cannot withdraw more than you have in your account
		else: #OK
			accountBalance = accountBalance - userWithdrawAmount# new account balance after withdrawl 
			print('Your new balance is:', accountBalance)# prints new account balance 
print('Done')# return 
