coins = [1,5,10,25,100]
a = 36
def shortNum(c,a):  
  out = []
  coins2 = c[::-1] 
  for i in coins2:
    num = a//i
    out=out+[i,]*num
    a = a-num*i
    if a<=0:
      break
  return out

print(shortNum(coins,a))