a = int (input("ievadi summu: "))
if a >= 200 and a < 500:
  b = a/100*90
elif a >= 500:
   b= a/100*80
print(int(input("summa ar atlaidi: "+str(b))))