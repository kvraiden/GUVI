# Program to make use of class and objects
class Human():
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def method(self):
        print("Hello My name is "+self.name)


h1 = Human("Sherlock", 6)
h2 = Human("Kandarp", 22)
h2.method()


print(h1.name)
print(h1.age)

num = int(input("Enter a number: "))


def prime():
    if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num//i, "is", num)
            break
    else:
        print(num, "is a prime number")


else:
    print(num, "is not a prime number")
