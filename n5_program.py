#1 savarjisho
consumer_info=[]
per1=[]
per2=[]
per3=[]
for i in range(3):
    info1=input("enter your name: ")
    info2=input("enter your Lastname: ")
    info3=input("enter your age: ")
    per1.append(info1)
    per2.append(info2)
    per3.append(info3)
    consumer_info=[per1,per2,per3]
print(consumer_info[0])
col1=int(input("Enter first index: "))
col2=int(input("Enter first index: "))
col3=int(input("Enter first index: "))
if col1==0 and col2==1 and col3==2 :
    print(f"name: {consumer_info[col1][col1]}, Lastname {consumer_info[col2][col1]} , Age: {consumer_info[col3][col1]} ", end=" ")
    
elif col1==0 and col2==2 and col3==1 :
    print(f"name: {consumer_info[col1][col3]}, Lastname {consumer_info[col2][col2]}, Age: {consumer_info[col3][col2]}", end=" ")
   
elif col1==1 and col2==2 and col3==0 :
    print(f"name: {consumer_info[col3][col2]}, Lastname {consumer_info[col1][col2]}, Age: {consumer_info[col2][col2]}", end=" ")
    
else:
    print("error")
          


#2 savarjisho
log=input("name:")
pas=input("pass:")
user1=[]
pas1=[] 
if len(pas)>=8 and len(log)>0:
    print("registrirebulia")
    user1.append(log)
    pas1.append(pas)
    print(pas1[0][0:])
    answer=input("ginda eqauntshi shesvla: ")
    if answer.lower()=="yes":
        user=input("enter user: ")
        pas=input("enter pas: ")
        if user1[0][0:]==user and pas1[0][0:]==pas:

            print("longed in")
        else:
            print("error")
    else:
        print(" Have a good day")
else:
    print("error")

#3 savarjisho
    
    actors_information = [
    ["Tom Hanks", "age 65", "movies" "Forrest Gump", "Cast Away", "Saving Private Ryan"],
    [ "Meryl Streep", "age 72", "movies" "The Devil Wears Prada", "Sophie's Choice", "Mamma Mia!"],
    [ "Leonardo DiCaprio", "age 47", "movies" "Titanic", "Inception", "The Revenant"]
    
]
actor=[]
actor_name=input("Enter actor name and lastname: ")
for  i in actors_information:
      for item in i:
        if item[0:]==actor_name:       
         ind=item.index(actor_name)
         print(actors_information[ind])
         break
        else:
               print("We don't have information about this actor.")
      break
  

#3 savarjisho
    











   

