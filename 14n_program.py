#1
#დაწერე კოდი რომელიც article.txt _დოკუმენტში იპოვის რიგით მეორე ყველაზე ხშირად განმეორებად სიტყვას.
import csv
from collections import Counter
import re

def find_words(file_path):
    with open(file_path, 'r') as file:
        words = re.findall(r'\b\w+\b', file.read().lower())
        word_count = Counter(words)
        rep_words = [word for word, count in word_count.items() if count >= 2]
        return rep_words

file = 'article.txt'
rep_words = find_words(file)
print(f' {", ".join(rep_words)}')


#2
#names.csv ფაილში არსებული ინფორმაცია გადმოაკოპირე names.txt ფაილში.
with open("names.csv", "r") as file1:
    csv_reader = csv.reader(file1)

    with open("names.txt", "w",newline="") as new_file:
        txt_writer = csv.writer(new_file)

        for line in csv_reader:
            txt_writer.writerow(line)
                
                
     

   
    
       





