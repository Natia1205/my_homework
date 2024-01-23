#1 savarjisho
#შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე სიას, თუმცა უნიკალური ელემენტებით (გამოიყენე set მონაცემთა ტიპი).
def unique_list(elements):
    set_1=set(elements)
    return set_1
list1=[1,4,5,6,7,7,9,8,8,10,100]

print (unique_list(list1))


#2 savarjisho
#შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე set ტიპის მონაცემს უნიკალური ელემენტებით, რომლის შეცვლაც შეუძლებელი იქნება (გამოიყენე frozenset).
def immutable_set(elements):
    
    set_2=set(elements)
    return set_2
list1=[1,4,5,6,7,7,9,8,8,10,100]
a=frozenset(list1)
print (immutable_set(a))


#3 savarjisho
#შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს tuple ტიპის მონაცემად და დააბრუნებს შედეგს.
def set_to_tuple(set1,set2):
    com_set=set1.union(set2)
    com_tuple=tuple(com_set)
    return com_tuple
set_1= {2,3,6,8,9,4}
set_2= {3,8,9,40,50,35,20,100}
print(set_to_tuple(set_1,set_2))
