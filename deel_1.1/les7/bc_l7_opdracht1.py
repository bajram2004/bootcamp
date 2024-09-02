a=5
b=3
c=2

# if statement 1
if (a==6 and b==4 or c==2):
   print("De conditie is waar")
else: 
   print("De conditie is niet waar")    

# if statement 2
if (a==6 and (b==4 or c==2)):
   print("De conditie is waar")
else:
   print("De conditie is niet waar")

#UITLEG:If Statement 1: De or-operator heeft een lagere prioriteit dan de and-operator, dus a==6 en b==4 of c==2 wordt geïnterpreteerd als (a==6 en b==4) of c==2.
#De or-voorwaarde is True als a==6 en b==4 True is of c==2 True is. 
#Omdat c==2 True is, is de algehele voorwaarde True.
#If Statement 2: Haakjes veranderen de volgorde van evaluatie.
#Hier wordt de voorwaarde (b==4 of c==2) eerst geëvalueerd en vervolgens wordt het resultaat gecombineerd met a==6 met behulp van de and-operator. 
#Om de hele voorwaarde True te laten zijn, moet a==6 True zijn en (b==4 of c==2) True. 
#Omdat a==6 False is, wordt de hele voorwaarde geëvalueerd naar False.
