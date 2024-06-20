import os.path
import os

#3 Задача
with open('text_one.txt','r', encoding='utf-8') as file_1:
    text_1=file_1.readlines()
    file_1.seek(0)
    line_count_1=len(file_1.readlines())
    file_1.seek(0)
    data_1 = len(file_1.read())
# print(line_count_1)
# print(data_1)
# print(text_1)
with open('text_two.txt', 'r', encoding='utf-8') as file_2:
    text_2=file_2.readlines()
    file_2.seek(0)
    data_2=len(file_2.read())
    file_2.seek(0)
    line_count_2 = len(file_2.readlines())
 #print(line_count_2)
 #print(data_2)
 #print(text_2)
with open('text_three.txt', 'r', encoding='utf-8') as file_3:
    text_3=file_3.readlines()
    file_3.seek(0)
    data_3=len(file_3.read())
    file_3.seek(0)
    line_count_3 = len(file_3.readlines())
 #print(line_count_3)
 #print(data_3)
 #print(text_3)
total_text={line_count_1:[['text_one.txt'],['8'],[text_1]],line_count_2:[['text_two.txt'],['1'],[text_2]],line_count_3:[['text_three.txt'],['9'],[text_3]]}
sorted_total_text=dict(sorted(total_text.items()))
    #print(total_text)
final_text_1=list(sorted_total_text.values())
print(final_text_1,end='\n')
# print(' '.join(final_text_1[0][0]))
# print(' '.join(final_text_1[0][1]))
# print(final_text_1[0][2][0][0])
# print(' '.join(final_text_1[1][0]))
# print(' '.join(final_text_1[1][1]))
# print(final_text_1[1][2][0])
final_text=(",".join(map(str,final_text_1)))
#print(final_text)
import re
#final_text_2=final_text.split('\\n')
import re

#print(final_text_2)
#print(text_1)
with open('final_text_over.txt',"w",encoding='utf-8') as file:
    file.writelines(f"{item}\n"for item in final_text_1)


#print(sorted_total_text)
# f= open('Total_text.txt', 'w', encoding='utf-8')
#
# f.write(final_text)
# f.close()



#with open('Total_text', 'w',encoding='utf-8') as outfile:
 #   for f in ['text_one.txt', 'text_two.txt','text_three.txt']:
  #      with open(f, 'r') as infile:
   #         outfile.write(infile.read())
#import shutil

#with open('Total_text.txt', 'wb') as outfile:
 #   for f in ['text_two.txt', 'text_one.txt','text_three.txt']:
  #      with open(f, 'rb') as infile:
   #         shutil.copyfileobj(infile, outfile)