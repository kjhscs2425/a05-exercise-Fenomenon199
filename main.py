
"""
`check_fever` should return `True` if the temperature is `100.4` or higher. For
any lower temperature, it should return `False`.
"""
def check_fever(temperature): 
  if temp >= 100.4:
    return True
  else: 
    return False 
  
  return

# Get temperature from user and convert to float
temp = float(input("whats your temperature"))
if check_fever(temp): 
  print("You have a fever.")
else:
  print ("you are very sick! you need a doctor")