if "o World" in "Hello World":
    print("yes")

# 1) 1-5
# 2) _IK_ or _FK
# 3) z or a or b at the end

# ^ - the beginning of the string
# .* - any symbol in any count
# .+ - any symbol 1 or more times
# .? - any symbol 0 or 1 times
#.{3} - any symbol 3 times 
# | - or
# [azb] - any letters of azb at least once
#\Z - end of a string

s_1 = "5_blabla_IK_blabla_z"
# s_2 = ...

import re

template = re.compile("^[1-5]+.*(FK_|_IK_)+.*[azb]+\Z")

if template.match(s_1):
    print ("yes")
else:
    print("No")



import re

# text = "xyzgaga"
# formula = re.compile("^xyz")

# text = "gagaxyz"
# formula = re.compile("....xyz")

# text = "gagaxyz"
# formula = re.compile(".*xyz")

text = "gagaxyz"
formula = re.compile(".+xyz")
# .+ means any symbol once or more 

if formula.match(text):
    print ("yes")
else:
    print("No")




import re

text1 = "xgz"
text2 = "x6z"
text3 = "xuz"

# # .
# formula = re.compile("x.z")

# a-z letter
# formula = re.compile("x[abcdefghijklmnoprstuvwxyz]z")
# formula = re.compile("x[a-z]z")
# formula = re.compile("x[a-z]*z")
# formula = re.compile("x[a-z]+z")

# 0-9
# formula = re.compile("x[1-9]z")

#a-z A-Z
# formula = re.compile("x[a-zA-Z]z")

#a-z A-Z 0-9
# formula = re.compile("x[a-zA-Z0-9]z")

if formula.match(text1):
    print ("yes")
else:
    print("No")

if formula.match(text2):
    print ("yes")
else:
    print("No")

if formula.match(text3):
    print ("yes")
else:
    print("No")






import re

text1 = "x_car_z"
text2 = "x_bus_z"
text3 = "x_cat_z"

# car or bus 
formula = re.compile("^x(_car_|_bus_)z\Z")

if formula.match(text1):
    print ("yes")
else:
    print("No")

if formula.match(text2):
    print ("yes")
else:
    print("No")

if formula.match(text3):
    print ("yes")
else:
    print("No")




# groups
import re
text1 = "/net/homedir/rvolodin/dev/project/sequences/LS_ABB_P/shots/LS_ABB_0021_001"
text2 = "/net/homedir/rvolodin/dev/project/sequences/LX_CCG_P/shots/LX_CCG_0022_001"
text3 = "/net/homedir/rvolodin/dev/project/sequences/LZ_ABC_P/shots/LZ_ABC_0023_001"

#get name of sequence (like ABB or CCG), and name of the shot like ABB_0021

formula = re.compile("^.*/L[A-Z]_([A-Z]{3})_P.*/L[A-Z]_([A-Z]{3}_[0-9]{4})_[0-9]{3}$")

for i in [text1, text2, text3]:
    result = formula.match(text1)
    if result:
        # group 0 means the whole text, so counting will start from group 1
        sequence = result.group(1)
        frame = result.group(2)
        print(sequence, frame)



import re
text1 = "ha_ho_hu_he"

formula = re.compile ("^[a-z]{2}_([a-z]{2})_[a-z]{2}_([a-z]{2})")
result = formula.match(text1)

print (result.group(1))
print (result.group(2))





import re
# Split string with symbols !.? and get the substring with maximum of words
def solution(S):
    result = re.split('[!.?]+', S)
    #split string by any of [! . ?] symbols
    # do it when they appear like . or ... or ???
    out = 0
    substring = None
    for i in result:
        # first check if this split i is not spaces only
        sub = i.strip() #delete spaces from both sides of the string
        if not len(sub): #if there were only spaces - continue
            continue
        sub = ' '.join(sub.split()) # join "sub" elements with ' '. Becomes a single word
        length = len(sub.split(" ")) # get number of words in i
        if length > out:
            # if it gives better result
            out = length
            substring = sub
    return out
print (solution("Forget CVs..Save time . x x"))