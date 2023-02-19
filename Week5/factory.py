
class SauceSelection:
 
 
    def __init__(self):
 
        self.sauces = {"s1": "normal", "s2": "spicy",
                             "s3":"none"}
 
    def ingredients(self, msg):
 
        return self.sauces.get(msg, msg)
 
class CheeseSelection:
 
    def __init__(self):
 
        self.cheeses = {"s1": "mozzarrella", "s2": "feta",
                             "s3":"dairy free"}
 
    def ingredients(self, msg):
 
        return self.cheeses.get(msg, msg)
 
class ToppingSelection:
 
    def __init__(self):
 
        self.toppings = {"s1": "pineapple", "s2": "hamburger",
                             "s3":"none"}
 
    def ingredients(self, msg):
 
        return self.toppings.get(msg, msg)
 
if __name__ == "__main__":
 
    s = SauceSelection()
    c = CheeseSelection()
    t = ToppingSelection()
    
 
    # list of strings
    selection = ["s1", "s2", "s3"]
 
    for sec in selection:
        print(sec)
        print(s.ingredients(sec))
        print(c.ingredients(sec))
        print(t.ingredients(sec))
        print()