
def reversDigits(num): 

	# Handling negative numbers 
	negativeFlag = False
	if (num < 0): 
	
		negativeFlag = True
		num = -num 
	

	prev_rev_num = 0
	rev_num = 0
	while (num != 0): 
	
		curr_digit = num % 10

		rev_num = (rev_num * 10) + curr_digit 

		# checking if the reverse overflowed or not. 
		# The values of (rev_num - curr_digit)/10 and 
		# prev_rev_num must be same if there was no 
		# problem. 
		if (rev_num >= 2147483647 or
			rev_num <= -2147483648): 
			rev_num = 0
		if ((rev_num - curr_digit) // 10 != prev_rev_num): 
		
			print("WARNING OVERFLOWED!!!") 
			return 0
		

		prev_rev_num = rev_num 
		num = num //10
	

	return -rev_num if (negativeFlag == True) else rev_num 




# Driver code 
if __name__ =="__main__": 
	num = 12345
	print("Reverse of no. is ",reversDigits(num)) 

	num = 1000000045
	print("Reverse of no. is ",reversDigits(num)) 
		
