""" Type Casting or Explicit Type Conversion """

#print("Hello" + 42)		    # output: TypeError
print("Hello" + str(42))		# output: Hello 42

total = 35
user_val = "26"
#total = total + user_val		# output: TypeError
total = total + int(user_val)	# total will be 61

