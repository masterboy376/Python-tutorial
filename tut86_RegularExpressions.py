import re
mystr = "Tata Stories Leading India's E-Mobility Revolution Tata Motors is taking bold and transformative actions towards connected and green-mobility solutions for a 'Connected Indiaiiiiiiiii aiai 11111-23 +91-1111111111'"

# main functions:- findall, search, split, sub, finditer

# meta characters 
# patt = re.compile(r'leading')
# patt = re.compile(r'.ed')# any character
# patt = re.compile(r'^Tat')# starts with
# patt = re.compile(r'India\'$')# ends with
# patt = re.compile(r'ai*')# zero or more i after a
# patt = re.compile(r'ai+')# one or more i after a
# patt = re.compile(r'ai{2}')# two i after a
# patt = re.compile(r'(ai){2}')# two ai
# patt = re.compile(r'(ai){2}|t')# two ai or t

#special sequence
# patt = re.compile(r'\ATata')# string Starts with Tata
# patt = re.compile(r'\bIn')# word Starts with In
# patt = re.compile(r'ia\b')# word ends with In

# complicated
# patt = re.compile(r'\d{5}-\d{2}')# number of this pattern: 11111-21

# quiz
patt = re.compile(r'\b91-\d{10}\b')# number of this pattern: 11111-21

matches = patt.finditer(mystr)
listOfPhone = []
for match in matches:
    print(match)
