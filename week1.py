class Teams:

   def __init__(self, members):

       self.__myTeam = members
       

   def __len__(self):

       return len(self.__myTeam)

   def __contains__(self):
    for person in self.__myTeam:
        if person == 'Tim' or person == 'Sam':
            return True

   def __iter__(self):
    for person in self.__myTeam:
        print(person)


    
    

    
    

 

classmates = Teams(['John', 'Steve', 'Tim'])

print (len(classmates))
print (Teams.__contains__(classmates))
Teams.__iter__(classmates)