#1 savarjisho
#დაწერე პროგრამა რომელიც გადაამრავლებს სიის ყველა წევრს კონკრეტულ რიცხვზე ლამბდას გამოყენებით.

list1 = [lambda arg=x, y=2: arg*y for x in range(1, 10)]
print(list1)
for fun in list1:
    print(fun())


#2 savarjisho
#დაწერე პროგრამა ლამბდას გამოყენებით, რომელიც გადაცემული სიის სიგრძეს დააბრუნებს, მას შემდეგ რაც წაშლის სიიდან ყველა სახელს რომელიც პატარა სიმბოლოთი იწყება. (გამოიყენე .isupper() მეთოდი)
names_list=["Natia", "mariami", "Irakli", "giorgi", "Emili"]
remove = list(filter(lambda x:  x[0].isupper(), names_list))
length_ = len(remove)
print("Length of modified list:", length_)



#3 savarjisho 
#დაწერე პროგრამა რომელიც დააჯამებს სიაში არსებულ დადებით და უარყოფით რიცხვებს ცალცალკე. გამოიყენე ლამბდა ფუნქცია და filter.
lis=range(-10,10)
pos=list(filter(lambda x: x>0,  lis))
neg=list(filter(lambda x: x<0,  lis))
sum_pos=sum((pos))
sum_neg=sum((neg))
print(f"Sum of Positive Numbers: {sum_pos}")
print(f"Sum of Negative Numbers: {sum_neg}")


#4 savarjisho
#დაწერე ბანკის ექაუნთის შექმნის, ანგარიშზე თანხის განთავსების და შემდგომ ექაუნთში შესვლის პროგრამა, არასწორი ინფორმაციის შეყვანა მომხმარებლისგან დააზღვიე try და except ბლოკის მეშვეობით.
def bank_account( account_number, account_name):
    account_number_=account_number
    account_name_=account_name
    
def deposit(amount):
     balance=0
     if amount>0:
         balance+=amount
         print(f" your Deposited is {balance}")
     else:
        print("error")
def login(enter_account_num):
    try: 
        enter_account_num=int(enter_account_num)
        if enter_account_num==account_number_:
            return "login"
        else:
            return "Pleas try again."
    except Error:
        return " Please enter a valid account number"

account_number_=12345678
account_name_="Natia"
amount=500
user_input = input("Enter account number to log in: ")
print(bank_account(account_number_, account_name_))
print(deposit(amount))
print(login(user_input))




