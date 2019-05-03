#test extraction
import re

test_data = open('test.txt')
extracted_num = list()

for line in test_data:
    line = line.rstrip()
    extracted = re.findall('[0-9]+', line)
    x=0
    if len(extracted) >0 :
        print('String: ', extracted)
        x += 1
       while x>0 :
           num = int(extracted[x])
           extracted_num.append(num)
print(extracted_num)
    #num = int(extracted[0])
    #extracted_num.append(num)
    #extracted_num = [int(x) for x in extracted_num]


#print(extracted_num)
#print('Sum: ', sum(extracted_num))

