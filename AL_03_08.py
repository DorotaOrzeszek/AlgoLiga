import sys

def answer():
  max1 = -1
  max2 = -1
  numbers = [int(x) for x in sys.stdin.readline().split()[:-1]]
#  numbers.remove('0')
  for n in numbers:
#    n = int(el)
    if n > max1:
      max2 = max1
      max1 = n
    elif max1 != n > max2:
      max2 = n
  if max2 == -1:
    return max1
  else:
    return max2
print(answer())
'''
n = 0
nr = ''
maxpresent = -1
secondmaxpresent = -1
last = ''

while True:
  char = sys.stdin.read(1)
  if char == '0' and last == ' ':
    break
  elif char == ' ':
    n = int(nr)
    if n > maxpresent:
      secondmaxpresent = maxpresent
      maxpresent = n
    elif n != maxpresent and n > secondmaxpresent:
      secondmaxpresent = n
    nr = ''
    n = 0
  else:
    nr = "".join([nr,char])
  last = char
 
if secondmaxpresent == -1:
  print maxpresent
else:
  print secondmaxpresent
  '''
