class Pizza:
    def __init__(self):
        self.__cheese = None
        self.__sauce = None
        self.__toppings = None

    def setCheese(self, cheese):
        self.__cheese = cheese

    def setSauce(self, sauce):
        self.__sauce = sauce

    def setToppings(self, topping):
        self.__toppings = topping
    
    def specification(self):
        print( "chesse: %s" % self.__cheese.type)
        print( "sauce: %s" % self.__sauce.type)
        print( "toppings: %s" % self.__toppings.type)
    
class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getPizza(self):

        pizza = Pizza()

        cheese = self.__builder.getCheese()
        pizza.setCheese(cheese)

        sauce = self.__builder.getSauce()
        pizza.setSauce(sauce)

        toppings = self.__builder.getToppings()
        pizza.setToppings(toppings)

        return pizza

class Builder:
    def getCheese(self): pass
    def getSauce(self): pass
    def getToppings(self): pass

class MeatBuilder(Builder):
    def getCheese(self):
        cheese = Cheese()
        cheese.type = "mozzarella"
        return cheese

    def getSauce(self):
        sauce = Sauce()
        sauce.type = "spicy"
        return sauce
    
    def getToppings(self):
        toppings = Toppings()
        toppings.type = "meat"
        return toppings

class Cheese:
    type = None

class Sauce:
    type = None

class Toppings:
    type = None

def main():
    meatBuilder = MeatBuilder()

    director = Director()

    print("pizza")
    director.setBuilder(meatBuilder)
    special = director.getPizza()
    special.specification()
    print()

if __name__ == "__main__":
    main()