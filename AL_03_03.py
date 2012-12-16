import datetime

def lensetless4(string):
  ans = [0]*11
  count = 0
  for char in string:
    if char == '-':
      if ans[10] == 0:
        ans[10] = 1
        count += 1
        if count > 4:
          return False
    else: 
      if ans[int(char)] == 0:
        ans[int(char)] = 1 
        count += 1
        if count > 4:
          return False
  return True
  
t = int(raw_input())
m31 = [1,3,5,7,8,10,12]
m30 = [4,6,9,11]

while t > 0:
  date = raw_input().split("-")
  d = int(date[0])
  m = int(date[1])
  y = int(date[2])
  while True:
    while not lensetless4(str(y)):
      y += 1
      d = 0
      m = 1
    d += 1
    if ( d > 31 and m in m31 ) or ( d > 30 and m in m30 ) or ( d > 29 and m == 2 and (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)) ) or ( d > 28 and m == 2 and (y % 400 != 0 and (y % 4 != 0 or y % 100 == 0)) ):
      m += 1
      d = 1
      if m > 12:
        m = 1
        y += 1
    dateformat = ['%02d' % xx for xx in [d,m]]+[str(y)]
    newdate = "-".join(dateformat)
    if lensetless4(newdate):
      print newdate
      break
  t -= 1
