#1 savarjisho
#დაწერე ფუნქცია რომელიც ლექსიკონიდან დუბლიკატებს ამოშლის და ყველა უნიკალური value_ს მქონე ლექსიკონს დააბრუნებს.
from collections import defaultdict
dict_n={'a': 1, 'p': 2, 'l': 1, 'e': 1}

def dupl_value(in_dict):
    un_value=set()
    un_dic={}
    for key, value in in_dict.items():
        if value not in un_value:
            un_value.add(value)
            un_dic[key]=value
    return un_dic

print(dupl_value(dict_n))

#2 savarjisho
#დაწერე ფუნქცია რომელიც შეამოწმებს გადაცემული ლექსიკონი ცარიელია თუ არა და დააბრუნებს შესაბამის პასუხს.
a={
    "name": "natia", 
    "surename":"tsabadze",
    "age":"26",
    "name": "natia", 
    "surename":"tsabadze",
    "age":"26"
}

b={}
def empty_diction(diction):
    if not diction:
        return "The dictionary is empty."
    else:
        return "The dictionary is not empty."
print(empty_diction(b))


#3 savarjisho
# დაწერე ფუნქცია, რომელიც გადაცემული სტრიქონისგან ლექსიკონს შექმნის და დააბრუნებს. ვთქვათ გადავეცით ფუნქციას სტრიქონი, უნდა დააბრუნოს სიმბოლოები key_ს ადგილას და მათი რაოდენობა value_ს ადგილას. მაგალითად გადავეცით სტრიქონი : 'racoon' უნდა დააბრუნოს ლექსიკონი: {'r': 1, 'a': 1, ‘c': 1, 'o': 2, ‘n': 1}

list_fruit = "apple"
def count_value(diction):
    dict1 = {}
    for symbol in diction:
        dict1[symbol]=dict1.get(symbol,0)+1
    return dict1
        


print(count_value(list_fruit))


  




















