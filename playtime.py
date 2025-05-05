# teaching myself a wee bit about classes and objects.
# classes are like the blueprint off of which i make my objects. they're like the object builder.

# here i'm making a class called ExampleClass with a property of x.
class ExampleClass:
    # in this little object builder, i'll say that the property x has a value of 5.
    x = 5

# now i'll make an object called p1, based off of ExampleClass, and print x.
p1 = ExampleClass
print(p1.x)

# all classes come with a function called __init__(). it's always called when the class is being used.
# use __init__ to assign values to object properties or do other important starting-up stuff.

# let's make a class called Person. it'll have two properties: name and age.
class Person:
    # now we'll use __init__ to assign values for name and age.
    def __init__(self, name, age): # this is our template for making people. it has to look like this.
        self.name = name
        self.age = age

# now let's make a person!
person1 = Person("Eli", 23)

# we can print the properties of the object individually:
print(person1.name)
print(person1.age)

# what happens if we try to just print the object?
print(person1)

# hmm. it just prints out the location of the object in our memory.
# "<__main__.Person object at 0x104822900>" blah blah blah
# if we want the object returned in plain English, we have to use the __str__ function.
# (that's pronounced "stir")

# let's try it with a class that's for pets instead of people.
# (question: why can we use the same property names for stuff in different classes?)
class Pet:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    # now let's make it print this stuff out legibly. return f"(blah blah) will do the trick.
    # (question: what is return f?)
    def __str__(self):
        return f"{self.name}, {self.breed}"

# let's make some pets!
pet1 = Pet("Mowgli", "Goldendoodle")
pet2 = Pet("Louie", "Goldendoodle")

# did it work? let's print them out.
print(pet1)
print(pet2)

# what if I want to automatically write a sentence using object data?
# we can do it by using a method. that's just a function that belongs to a specific object.
# let's talk about some of the different flowers you can see in pittsburgh's early spring.
class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    # here we'll make our function, and name it flowerFunc (hehe)
    def flowerFunc(self):
        # we want it to print a sentence about the flower.
        print("In spring you can see " + self.name + " in beautiful shades of " + self.color)

# now let's make some flowers!
flower1 = Flower("lilacs", "purple")
flower2 = Flower("cherry blossoms", "pink")
flower3 = Flower("dogwood flowers", "white and pink")

# we have our class, our function, and our objects. let's put them all together and talk about flowers.
flower1.flowerFunc()
flower2.flowerFunc()
flower3.flowerFunc()

# YES!

# at this point it's prob self-evident, but 'self' is just like a magic word that means,
# "refer to the current instance of this class to access the variables you need"