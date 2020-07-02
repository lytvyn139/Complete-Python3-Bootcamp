#		Comparison and Logic Operators
""" 
== Checks if the value of two operands are equal
!= Checks if the value of two operands are not equal			
>  Greater than
<  Less than
>= Greater or equal
<= Less or equal
and
or
not
"""

x = 10
if x > 50:
	print(str(x)+" bigger than 50")
else:
	print(str(x)+" smaller than 50")

y = 55
if y > 14:
	print(str(y)+"bigger than 14")
elif y > 53:
   	print(str(y)+"bigger than 53")
else:
   	print(str(y)+"smaller than 10")

###################################
if some_condition:
    #execute code
else:
    #do something

###################################
if some_condition:
    #execute code
elif some_other_condition:
    #do something
elif some_other_condition:
    #do something
elif some_other_condition:
    #do something
else:
    #lastly do something

