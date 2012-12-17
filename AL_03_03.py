m31 = [1,3,5,7,8,10,12]
m30 = [4,6,9,11]
armageddon = {}

for year in xrange(1800,9999):
  months = {}
  for month in xrange(1,13):
    days = []
    if len(set("%02d%d" % (month,year))) >= 4:
      continue
    for day in xrange(1,32):
      date = "%02d%d%d" % (day,month,year)
      if len(set(date)) < 4:
        if not ( ( day > 31 and month in m31 ) 
        or ( day > 30 and month in m30 ) 
        or ( day > 29 and month == 2 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) ) 
        or ( day > 28 and month == 2 and (year % 400 != 0 and (year % 4 != 0 or year % 100 == 0)) ) ):
          days.append(day)
    months[month] = days
  armageddon[year] = months

def nextArmageddon(d,m,y):
  found = (0,0,0)
  while True:
    if armageddon[y] == {}:
      y += 1
      m = 1
      d = 0
      continue
    else:
      if not armageddon[y].has_key(m):
        m += 1
        if m <= 12:
          continue
        else:
          y += 1
          m = 1
          d = 0
          continue
      else:
        if d >= armageddon[y][m][-1]:
          m += 1
          if m <= 12:
           continue
          else:
            y += 1
            m = 1
            d = 0
            continue
        else:
          for di in armageddon[y][m]:
            if d < di:
              found = (di, m, y)
              break
    if found != (0,0,0):
      break
  return found

t = int(raw_input())
while t > 0:
  date = raw_input().split("-")
  d = int(date[0])
  m = int(date[1])
  y = int(date[2])
  nextdate = nextArmageddon(d,m,y)
  if nextdate[1] == 2 and (nextdate[0] in [29,]):
    p
  printableanswer = "-".join(['%02d' % xx for xx in nextdate])
  print printableanswer
  t -= 1
