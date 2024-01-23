
#1 savarjisho
#რეკურსიის დახმარებით შექმენი ფუნქცია, რომელიც იმდენჯერ დაბეჭდავს მისალმებას, რა რიცხვსაც გადასცემ არგუმენტად. (ციკლის გამოყენება არ შეიძლება)


def say_hi(message, time):
   
    if time<=1:
        return  message
    else:
       print(message) 
    return say_hi(message, time-1)
        
print(say_hi("hello", 6))


#2 savarjisho
#შექმენი ფუნქცია, რომელიც მიიღებს შეკვეთას, ანუ კერძის სახელს და რაოდენობას და დაბეჭდავს მას, თუმცა რაოდენობას თუ არ მივუთითებთ შეცდომას არ ამოაგდებს და 1_ად ჩათვლის.

def order(dish, quantity=1):
    if quantity<=1:
        return dish
    else:
        print(dish)
    return order(dish, quantity-1)

    

print(order("cake"))


#3 savarjisho
#შექმენი ფუნქცია, რომელიც მიიღებს მინიმუმ 3 რიცხვს, და დააბრუნებს და დაბეჭდავს ნარმავლს.

def numbers(*num):
    if len(num)<3:
        return " Enter three or more numbers"
    result=1
    for i in num:
      
        result *=i
    return result
info=(2,3,4)
print(numbers(*info))