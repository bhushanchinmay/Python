a=[]
a=input("Enter Expression")
q=[]
for i in a:
    if i=='(':
        q.append('(')
        print(q)
    else:
        try:
            q.pop()
            print(q)
        except Exception:
            print("Stack Empty")    
if len(q)==0:
     print("Experssion Have right number of Parenthesis",q)
else:
     print("Experssion Incorrect")
        
    
        
