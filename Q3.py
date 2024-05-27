import json
f=open('E:\kheder.json','r')
file = json.load(f)
f.close()
name=input("enter name:")
number=input("enter number:")
result=0
for i in file:
  ans = int (input (i))
  if ans == file[i]:
      result = result + 1 
a=open('E:\ khederaudi.json','w')
json.dump ({"name" : name , "number" : number , "result" : result},a)