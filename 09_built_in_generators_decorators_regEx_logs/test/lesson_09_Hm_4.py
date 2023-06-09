import re
import os


def filepath(full_path_to_file):
    def decorator(function):
        def wrapper(*args):
            result = full_path_to_file
            print (result)
            function()
            return result
        return wrapper 
    return decorator

def check_numbers(list_of_objects):
    for i in list_of_objects:
        pattern = re.compile("([+-]?([0-9]+|[1-9]+[0-9]*|[1-9]+[0-9]*[.]?[0-9]*[1-9]+|[0-9]?[.]?[0-9]*[1-9]+))$")
        result = pattern.match(i)
        if result:
            if  -1000000 <= float(i) <= 1000000:
                if not (float(i) == 0 and len(i) > 1):
                    yield i

# need to figure out how to plug path from a decorator to a function (minute 37)
@filepath(full_path_to_file = "C:/p_tests/numbers_data.txt")
def main():
    path_to_file = "C:/p_tests"
    file_name = "numbers_data"

    #get numbers from text
    source_text = []
    with open (path_to_file + "/" + file_name + ".txt", "r") as f:
        source_text = f.read().splitlines()

    source_numbers = map(lambda i: i.strip(), source_text)

    #do stuff through a generator 
    final_numbers = [i for i in check_numbers(source_numbers)]

    for n in final_numbers:
        print(n)

    with open (path_to_file + "/" + file_name + "_filtered_" + ".txt", "w") as f:
        for line in final_numbers:
            f.write(line)
            f.write('\n')


main()




# [+-]

# (?:0|[1-9]+[0-9]*)


# # old bad code
# def delete_extra_symbols(i):
#     #delete spaces in the beginning,     #same can be done with a simple strip
#     pattern = re.compile("^([ ]+)(.*)")
#     result = pattern.match(i)
#     if result:
#         space_count = len(result.group(1))
#         i = i[space_count:]


#     i = i.strip()
#     #delete end of a line symbols (if simple readlines have been used) 
#     if "\r\n" in i:
#         i = i.replace("\r\n", "")
#     return i

# def check_numbers(i):
#     pattern = re.compile("(-|\+)?[0-9]+$")
#     result = pattern.match(i)
#     if result:
#         if  -1000000 <= float(i) <= 1000000:
#             if not (float(i) == 0 and len(i) > 1):
#                 return i