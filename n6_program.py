#1 savarjisho
# . შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულინფორმაციას გაასამმაგებს და დაბეჭდავს შემდეგნაირად: 


def tripled_user_input():
    input_1=input("Enter info: ")
    tripled_info=input_1*3
    return tripled_info
print(f"Tripled:{tripled_user_input()}")


#2 savarjisho
# შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას დადააბრუნებს მის წონას მთვარეზე. (მთვარის გრავიტაცია 6_ჯერნაკლებია დედამიწისაზე)


def weight():
    your_weight=int(input("Enter your weight: "))
    your_weight_in_moon=your_weight/6
    return your_weight_in_moon
print(weight())


#3 savarjisho
# შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას მომხმარებლისგან input() ფუნქციის დახმარებით

def calculator():
    exa=input("Enter Mathematical representation: ")
    
    parts=exa.split()
    if len(parts) != 3:
        return "Invalid input. Please provide an expression in the format: 'number operator number."
    num1, operator, num2=parts
    
    if not (num1.isnumeric() and num2.isnumeric()):
        return "Please enter numeric values for the numbers."

    if operator=="+":
        result=int(num1)+int(num2)
    elif operator=="-":
        result=int(num1)-int(num2)
    elif operator=="*":
        result=int(num1)*int(num2)
    elif operator=="/":
        if num2==0:
            return "Division by zero is not allowed."
        result=int(num1)/int(num2)
    elif operator=="^":
        result=int(num1)**int(num2)
    else:
        return " error"
    return result
print(calculator())




# arasavaldebulo
# გავლილი მასალის გამოყენებით შექმენი ფუნქცია, რომელიც მიიღებს ლათინური სიმბოლოებით დაწერილ სიტყვას, დაშიფრავს მორწეს ანბანით და დააბრუნებს შედეგს. 

morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
}

def morse_code():
    word=input("enter word: ")
    morse_code1=[]
 
    for c in word.upper():
        morse_code1+=morse_code_dict[c].split()
        
    return " ".join( morse_code1)
print(morse_code())