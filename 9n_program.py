#1 savarjisho
#დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sort() მეთოდის გამოყენებით (ზრდადობით).
import random
a=[random.randint(1,100) for x in range(10)]
a.sort()
print(a)


#2 savarjisho
#დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sorted() ფუნქციის გამოყენებით (კლებადობით).
def bubble(list1):
    indx=len(list1)-1
    sorteed=False
    while not sorteed:
        sorteed=True
        for i in range(0, indx):
            if list1[i]<list1[i+1]:
                sorteed=False
                list1[i], list1[i+1]=list1[i+1], list1[i]
    return list1
list1=a
print(bubble(list1))


#3 savarjisho
#დაწერე პროგრამა რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას და შექმნილი სიის სორტირება სცადე ორი განსხვავებული მეთოდით (მაგ. Bubble და Selection). დათვალე თითოეული მეთოდისთვის სორტირებისთვის საჭირო დრო და დააკვირდი რომელი უფრო ეფექტურია მცირე(1000 ელემენტი), საშუალო(2000 ელემენტი) და გრძელი(3000 ელემენტი) სიის შემთხვევებში.
from random import randint
from time import time

def list_gen(a,b):
    arr=[]
    for _ in range(1,a):
        arr.append(randint(1,b))
    return arr
list_1=list_gen(1000,1000)
list_2=list_gen(2000,1000)
list_3=list_gen(3000,1000)
def selection_sort(some_arr):
    
    arr=some_arr
    length= range(0, len(arr)-1)
    for i in length:
        m_value=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[m_value]:
                m_value=j
        if m_value!=i:
            arr[m_value], arr[i]=arr[i], arr[m_value]
            def time():
                start=time()
                some_arr()
                end=time()
                x=start-end
                return x
            
            
    return arr
selection_sort(list_1)
print(f"SELECTION TIME: {time()}")
def bubble_sort(list_a):
    length= len(list_a)-1

    for i in range(length):
        sortedFlag=True
        for j in range(length):
            if list_a[j]<list_a[j+1]:
                list_a[j],list_a[j+1]=list_a[j+1], list_a[j]
                sortedFlag=False
        if sortedFlag:
            break
        def time():
                start=time()
                list_a()
                end=time()
                x=start-end
                return x
    return list_a
bubble_sort(list_1)
print(f"BUBBLE Time: {time()}")




        
        















