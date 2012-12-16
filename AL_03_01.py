n = int(raw_input())

top = ' ' *(n-1) + 'o'# + ' ' *(n-1)
print top
for i in range(1,n-1):
  middle = ' '*(n-i-1) + '/' + ' '*(i-1) + '|' + ' '*(i-1) + '\\'# + ' '*(n-i-1)
  print middle
bottom = '/' + '_'*(n-2) + '|' + '_'*(n-2) + '\\'
print bottom
end = ' ' *(n-1) + '|'# + ' ' *(n-1)
print end
