import re
import os

path_to_file = "C:/p_tests/numbers_data.txt"

#get numbers from text
source_text = []
with open (path_to_file , "r") as f:
    source_text = f.readlines()

# can be done with a i.strip build in function
def delete_extra_symbols(i):
    #delete spaces in the beginning
    pattern = re.compile("^([ ]+)(.*)")
    result = pattern.match(i)
    if result:
        # print (i)
        # print ("len of i ", len(i))
        # print ("section 1", result.group(1), len(result.group(1)))
        # print ("section 2", result.group(2), len(result.group(2)))
        space_count = len(result.group(1))
        i = i[space_count:]
    #delete end of a line symbols
    if "\r\n" in i:
        i = i.replace("\r\n", "")
    return i

source_numbers = map(delete_extra_symbols, source_text)

# for n in source_numbers:
#     print(n)

def check_numbers(i):
    pattern = re.compile("(-|\+)?[0-9]+$")
    result = pattern.match(i)
    if result:
        if  -1000000 <= float(i) <= 1000000:
            if not (float(i) == 0 and len(i) > 1):
                return i


final_numbers = filter(check_numbers, source_numbers)

for n in final_numbers:
    print(n)


