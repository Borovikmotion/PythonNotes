# about files
a = "hello world 123"
f = open("C:/Users/borov/Desktop/MayaFiles/newFile.txt", mode="w")
# "hello \n world"
# "hello \t world"

# flags when opening file
# w
# w+
# r
# a

f.write(a)
f.write("\nsurprise mothefucker")
# f.writelines(a,"hello", "world")

f.close()

text = ["a", "b", "c"]
for i in text:
    f.write(i + "\n")
f.close()



f = open("C:/Users/borov/Desktop/MayaFiles/newFile.txt", mode="r")
data = f.read()
print data 
f.close()

data = f.read()
data = data.split("\n")
for i in data:
    print i

f.close()


# proper way to open file

f =  open("C:/Users/borov/Desktop/MayaFiles/newFile.txt", mode="r")

with open("C:/Users/borov/Desktop/MayaFiles/newFile.txt", mode="w") as f:
    f.write("hello")

with open("C:/Users/borov/Desktop/MayaFiles/newFile.txt", mode="r") as f:
    f.read()