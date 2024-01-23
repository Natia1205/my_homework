

#1 savarjisho
from random import randint
from time import time
def list_gen(a,b):
    arr=[]
    for _ in range(1,a):
        arr.append(randint(1,b))
    return arr
list_1=list_gen(10,10)
print(list_1)


#2 savarjisho
def insertion_sort(list):
    ind_length=range(1,len(list))
    for i in ind_length:
        m_value=list[i]
        while list[i-1]>m_value and i>0:
            list[i],list[i-1]=list[i-1], list[i]
            i-=1
    return list

print("Insertion Sort")
print(insertion_sort(list_1))


#3  savarjisho
#linearSearch
def linearSearch(arr, elem):
    for i in range(len(arr)):
        if arr[i]==elem:
            return i
    return -1
linearSearch(list_1,5)

print(linearSearch(list_1,5))

#binnarySearch

def binnary_search(arr,begin, end, elem):
    if end>=begin:
        mid_elem=(begin+end)//2
        if arr[mid_elem]==elem:
            return mid_elem
        elif arr[mid_elem]>elem:
            return binnary_search(arr, begin, mid_elem-1,elem)
        else:
            return binnary_search(arr,mid_elem+1,end, elem)
    return -1
print(binnary_search(list_1,0,10, 5))

#4 
#დათვალე ძიების თითოეული მეთოდისთვის საჭირო დრო (დეკორატორის გამოყენებით) და დააკვირდი დროში სხვაობას მცირე, საშუალო და გრძელი სიის შემთხვევებში

def calculate_time(fun):
    def body(*arg, **tar):
        start_time=time()
        result=fun(*arg,**tar)
        end_tiem=time()
        result_time=end_tiem-start_time
        return result_time
    return body


@calculate_time
def linearSearch(arr, elem):
    for i in range(len(arr)):
        if arr[i]==elem:
            return i
    return -1
linearSearch(list_1,5)

print(linearSearch(list_1,5))

#binnarySearch
@calculate_time

def binnary_search(arr,begin, end, elem):
    if end>=begin:
        mid_elem=(begin+end)//2
        if arr[mid_elem]==elem:
            return mid_elem
        elif arr[mid_elem]>elem:
            return binnary_search(arr, begin, mid_elem-1,elem)
        else:
            return binnary_search(arr,mid_elem+1,end, elem)
    return -1
print(binnary_search(list_1,0,10, 5))