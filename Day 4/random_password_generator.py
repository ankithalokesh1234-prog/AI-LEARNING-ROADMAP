import random
letters="qwertyuioplkjhgfdsazxcvbnmAQWERTYUIOPLKJHGFDSZXCVBNM"
numbers="1234567890"
symbols="!@#$%"
characters=letters+symbols+numbers
password=""
for i in range(8):
  password+=random.choice(characters)
print("GENERATED PASSWORD:",password)
