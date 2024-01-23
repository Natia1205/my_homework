#1
#დაწერე ფუნქცია რომელიც მომხმარებელს ჩააწერინებს ტექსტურ ფაილში ინფორმაციას Input ფუნქციის დახმარებით, მანამ სანამ მომხმარებელი არ შეიყვანს სიტყვას _ “enough”.

import csv
with open("new_data", "w") as file:
    while True:
        a=input("enter info: ")
        if a.lower()=="enough":
            break

        file.write(f"{a}\n")
#2
#დაწერე ფუნქცია რომელიც input ფუნქციის დახმარებით მომხმარებლისგან მიიღებს საქაღალდის ლოკაციას და შესაქმნელი ფაილის სახელს, შემდეგ მიღებულ ლოკაციაზე შექმნის შესაბამის ფაილს და ამოპრინტავს საქაღალდეში არსებულ ყველა ფაილის სიას.
                
import os
a=input("enter file location and file name: ")
with open(a+ ".csv", "w") as file:
    file.write("Natia")
    dir_list = os.listdir(input("enter files location: "))
    print(dir_list)

