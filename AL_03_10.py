import math

def integrate(x,coeffs):
  a = coeffs[0]
  b = coeffs[1]
  c = coeffs[2]
  d = coeffs[3]
  e = coeffs[4]
  f = coeffs[5]
  ans = (a-d)*(x**3)/3 + (b-e)*(x**2)/2 + (c-f)*x
  return ans
  
t = int(raw_input())
while t > 0:
  line1 = raw_input().split()
  line2 = raw_input().split()
  # f(x) = a x^2 + b x + c, a > 0
  a = float(line1[0])
  b = float(line1[1])
  c = float(line1[2])
  # g(x) = d x^2 + e x + f, d < 0
  d = float(line2[0])
  e = float(line2[1])
  f = float(line2[2])
  # delta for f(x)-g(x)
  delta = (b-e)**2 - 4*(a-d)*(c-f)
  if delta <= 0:
    print "%.2f" % 0
    t -= 1
    continue
  x1 = (-(b-e)-math.sqrt(delta)) / (2*(a-d))
  x2 = (-(b-e)+math.sqrt(delta)) / (2*(a-d))
  p = 0
  q = 0
  if x2 >= x1:
    p = x1
    q = x2
  else:
    p = x2
    q = x1
  # p < q
  cfs = [a,b,c,d,e,f]
  area = integrate(q,cfs) - integrate(p,cfs)
  answer = abs(area)
  print "%.2f" % answer
  t -= 1

