import num2words

f = open("C:\\Users\\vyask\\Desktop\\GUVI\\Basics_Programs\\int1.txt", "r")
c = f.read()
print(c)

for i in c:
    num2words.num2words(i)
    print(i)


d = open("C:\\Users\\vyask\\Desktop\\GUVI\\Basics_Programs\\int1.txt", "a+")
d.write(i)
