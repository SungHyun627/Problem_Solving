p = [str(i) for i in range(10)]

def matching_deci_to_digit(x):
  if x < 10:
    return str(x)
  elif x == 10:
    return 'A'
  elif x == 11:
    return 'B'
  elif x == 12:
    return 'C'
  elif x == 13:
    return 'D'
  elif x == 14:
    return 'E'
  else:
    return 'F'
  

def matching_digit_to_deci(x):
  if x in p:
    return int(x)
  if 'A':
    return 10
  elif 'B':
    return 11
  elif 'C':
    return 12
  elif 'D':
    return 13
  elif 'E':
    return 14
  elif 'F':
    return 15
  

def convert_digit_to_deci(x, y):
  x = x[2:]
  x_len = len(x)
  result = 0
  for i in range(x_len):
    result += (matching_digit_to_deci(x[x_len - 1 - i])* (y ** (i)))
  return result

def convert_deci_to_digit(x, y):
  result = ''
   
  while (True):
    result += matching_deci_to_digit(x % y)
    x //= y 
    if x < y:
      result += matching_deci_to_digit(x)
      break
  
  result = result[::-1]
  if y == 2:
    return '0b' + result
  elif y == 8:
    return '0o' + result
  else:
    return '0x' + result
  

a = [str(i) for i in range(10)]

def xtd(x):
  if x in a:
    return int(x)
  return 10 + (ord(x) - ord('A'))

def dtx(x):
  if x < 10:
    return str(x)
  return chr(ord('A') + x - 10)


def cxtd(x, y):
  x = x[2:]
  x_len = len(x)
  result = 0
  for i in range(x_len):
    result += xtd(x[x_len - 1 - i]) * (y ** i)
  return result

def cdtx(x, y):
  result = ''
  if x == 0:
    return 0
  while True:
    result += dtx(x%y)
    x //= y
    if x < y:
      if x != 0:
        result += dtx(x)
      break
  result = result[::-1]
  if y == 2:
    return '0b' + result
  elif y == 8:
    return '0o' + result
  elif y == 16:
    return '0x' + result
  else:
    pass
    
x = '123'
y = int(x, 4)
z = bin(10)[2:]
print(x, y, z, convert_digit_to_deci('0b01011', 2), convert_deci_to_digit(26, 16))
print(x, y, z, cxtd('0b01011', 2), cdtx(26, 16))
