af=int(input())
if(af>1):
   for i in range(2,af):
      if(af%i)==0:
         print("no")
         break
   else:
         print("yes")
 
else:
   print("no")
