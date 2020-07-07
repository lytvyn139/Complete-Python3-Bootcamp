#https://docs.python.org/3/howto/regex.html
import re
text = 'The agent phone number is 402-325-2951. Call now!'
print('phone' in text) #true

pattern = 'phone'
print(re.search(pattern, text))
#<re.Match object; span=(10, 15), match='phone'>

pattern = 'ANY'
print(re.search(pattern, text))
#none

""" regex match object """
pattern = 'phone'
#if we have many matches, it still will return first match
match = re.search(pattern, text)
match.span() #10-15
match.start() #10
match.end() #10

""" FIND ALL """
text = 'my phone once, my phone twice, my phone is mango'
matches = re.findall('phone', text)
print(len(matches)) #3

for match in re.finditer('phone', text):
    print('printing all match in:', text)
    print(f'\n {match}')
    print(f'{match.span()}')
    print(f'{match.group()}')

""" \d - digit """
#file_\d\d  => file_25
#r"(\d\d\d)-\d\d\d-\d\d\d\d"

"""\w alphanumeric """
#\w-\w\w\w  => A-b_1 

""" \s white space """
#a\sb\sc => a b c

""" \D A non digit """
#\D\D\D => ABC

""" \W Non-alphanumeric	 """
#\W\W\W\W\W => *-+=)

""" \S Non-whitespace  """
#\S\S\S\S => Yoyo 

text = 'my phone number 408-912-2341'
phone = re.search(r'(\d{3})-\d{3}-\d{4}', text)
print(phone)
#<re.Match object; span=(16, 28), match='408-912-2341'>

print(phone.group()) #408-912-2341

#########################
""" quntifiers """
#########################
""" +	Occurs one or more times	 """
#Version \w-\w+	 => Version A-b1_1
""" {3}	Occurs exactly 3 times	 """
#\D{3}	abc
""" {2,4}	Occurs 2 to 4 times	 """
#\d{2,4}	123
""" {3,}	Occurs 3 or more """	
#\w{3,}	anycharacters
""" *	Occurs zero or more times	 """
#A\*B\*C*	=> AAACC
""" ?	Once or none	 """
#plurals?	plural

""" Compile, compiles different regex patter codes  """

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
#index starts at 1
print(results.group(1))  #408
print(results.group(2))  #914
print(results.group(3))  #2341


""" OR OPERATOR """
z = re.search(r'cat | or ','the cat is here')
print(z)

""" . wild card """
z = re.findall(r'.at','the cat in the hat sat there')
print(z)

""" ^\d string starts with number """
z = re.findall(r'^\d','1 is z number')
# will not work
#z = re.findall(r'^\d','is 2 a number')
print(z)

""" \d$ string ends with number """
z = re.findall(r'\d$','ends with number 2')
print(z)

""" exclude numbers """
phrase = 'there are 3 numbers 34 inside 5 this sentence'
digit_pattern = r'[^\d]+' #sentence
#digit_pattern = r'[^\d]' #letters
z = re.findall(digit_pattern, phrase)
print(z)

delete_punctuation = 'this is a string! but it has, commas and such !?'
clean = re.findall(r'[^!?.]+', delete_punctuation)
print(''.join(clean))

letters = re.findall(r'[^!?.]', delete_punctuation) 
print(letters)


""" Brackets for Grouping """
text = 'Only find the hyphen-words in this sentence. But you do not know how long-ish they are'
z = re.findall(r'[\w]+-[\w]+',text)
print(z)

""" PIPE """
# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"
re.search(r'cat(fish|nap|claw)',text)
#<_sre.SRE_Match object; span=(27, 34), match='catfish'>

re.search(r'cat(fish|nap|claw)',texttwo)
#<_sre.SRE_Match object; span=(32, 38), match='catnap'>

