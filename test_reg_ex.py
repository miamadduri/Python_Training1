#test extraction
import re

test_data = open('test.txt')
extracted_num = list()
total=0
for line in test_data:
    line = line.rstrip()
    extracted = re.findall('[0-9]+', line)
    if extracted: 
        print(extracted)
        for num in extracted:
            num = int(num)
            extracted_num.append(num)
            total = sum(extracted_num)
print(total)

        
