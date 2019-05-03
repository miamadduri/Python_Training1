#test extraction: using regular expressions to extract integers from a file and returning the sum
#test extraction
import re

test_data = open('test.txt')
extracted_num = list()

for line in test_data:
    line = line.rstrip()
    extracted = re.findall('[0-9]+', line)
    length = len(extracted)
    if length > 0 :
        #print(extracted)
        num = int(extracted[length-1])
        extracted_num.append(num)
    #print(extracted_num)
     
print('Sum of all numbers in this file: ', sum(extracted_num))

