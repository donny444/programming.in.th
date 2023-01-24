word=input()
def line1():
  print('.',end='')
  for element in range(1,len(word)+1):
     if element%3==0:
       print('.*..', end='')
     else:
       print('.#..', end='')
def line2():
  print('.',end='')
  for element in range(1,len(word)+1):
    if element%3==0:
      print('*.*.', end='')
    else:
      print('#.#.', end='')
  print('')
line1()
print('')
line2()
print('#', end='')
for element in range(1,len(word)+1):
  print('.'+word[element-1]+'.', end='')
  if ((not element==1) and (element%3==0 or (element+1)%3==0)) and not (len(word)==element and (element+1)%3==0):
    print('*', end='')
  else:
    print('#', end='')
print('')
line2()
line1()