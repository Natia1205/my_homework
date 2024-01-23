#2 savarjisho
num=int(input("{:d} enter your number:"))
for i in range(1,num+1):
    for j in range(1,num+1):
        n="x"
        print(f"{i} {n} {j}={i*j}")

#3 savarjisho
init_money=3000

while True:
    spend_money=int(input("enter how much money did you spend?:"))
    if spend_money==0 :
        print(f"your balance is {init_money}")
        break
    if  spend_money>init_money:
         
         print("not enough money")    
         continue
    else:
        init_money-=spend_money
    
#4 tutiyushi

while True:
    ans=input("User Said Whaaat!?: ")
    if ans=="quit":
        break
    if ans=="hello":
        print("User Said Whaaat!?")
        print("User said hello!")
        break
    else:
        print(ans)
    
  

    
         
    
    
