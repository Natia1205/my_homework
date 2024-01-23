import re
#1 savarjisho
inf=input("Enter information: ")
for i in inf:
    print(i.isalpha())
    print(i.isdigit())
    print(i.isalpha())
a=len(re.findall(r'\d',inf))
b=len(re.findall('[a-zA-Z]', inf))
c=len(re.findall('[+, *, ., |, (), $,{}]', inf))
print(a)
print(b)
print(c)


#2 savarjisho 
sen_1=input("enter sentence:")
sen_2=input("enter sentence: ")
sen_3=(f"{sen_1[:1]}{sen_2[-1]}{sen_1[2]}{sen_2[-2]}")
print(sen_3)


#3 savarjisho
sen_4=input("enter sentence:")
sen_5=input("enter sentence:")
sentence_1=re.findall(r"[a-zA-Z].*", sen_4)
sentence_2=re.findall(r"[a-zA-Z].*" , sen_5)

for symbol_1 in sentence_1:
    for simbol_2 in sentence_2:
        if symbol_1>=simbol_2 :
            print("Strings are balanced") 
        elif simbol_2>=symbol_1:
            print("Strings are balanced") 
    
        else:
            print("Strings aren't balanced")

