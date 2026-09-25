number =  123456789
result = 0

while number > 0: 
  
  digit = number % 10 # reminder - Get last digit
  result = result + digit # add last digit to result
  number = number // 10  # remove last digit from number

print("1st:" , result)

number = result

result = 0

while number > 0: 
  
  digit = number % 10 # reminder - Get last digit
  result = result + digit # add last digit to result
  number = number // 10  # remove last digit from number

print(result)