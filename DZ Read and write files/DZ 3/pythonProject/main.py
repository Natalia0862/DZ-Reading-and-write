import os
import operator

path = r"C:\Users\New\Desktop\Netology\DZ Read and write files\DZ 3\pythonProject\5.txt"

list_files = [x for x in os.listdir(r'C:\Users\New\Desktop\Netology\DZ Read and write files\DZ 3') if x == '1.txt' or x == '2.txt' or x == '3.txt']

new_dict = dict()
sorted_dict = dict()
count = int(0)

for file in list_files:
    def strings_count(file):
       with (open(os.path.join(r'C:\Users\New\Desktop\Netology\DZ Read and write files\DZ 3', file), 'r') as f):
            return sum(1 for line in f)
    with (open(os.path.join(r'C:\Users\New\Desktop\Netology\DZ Read and write files\DZ 3', file), 'r') as f):
        list_news = f.read()
        count = strings_count(file)
        new_dict[file] = count, list_news


sorted_dict = sorted(new_dict.items(), key=operator.itemgetter(1))
new_dict = dict(sorted_dict)

for item in new_dict:
    opening_files = open(path, 'a', encoding= 'utf-8')
    opening_files.write(f'Количество строк {new_dict[item]}\n')
    opening_files.write(f'\n')
    opening_files.close()



