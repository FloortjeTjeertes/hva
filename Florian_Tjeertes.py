import datetime

class Main:
   def start():
    print("hello")
    dt = datetime.date.today()

    Fname=str()
    Lname=str()
    Date=int()

    while Fname=="":
        Fname=input("wat is uw voornaam?: ")
    
    while Lname=="":
        Lname=input("wat is uw achternaam?: ")

    while isinstance(Date, int)==False or int(Date) <= 0 or  int(Date) >= dt.year:
        temp=input("wat is uw geboorte jaar?: ")
        try:
         Date=int(temp)
        except:
         print('datum is niet valide')




    age =main.calc(int(Date))[0]
    SpaceAge=main.calc(int(Date))[1]
    print("Beste "+Fname+" "+Lname+", in 2021 is je leeftijd: "+str(age)+".\nEn je leeftijd is dan afgerond: "+str(SpaceAge)+" in Venusjaren.")

   def calc(years):
    dt = datetime.date.today()
    age= dt.year - years
    venus=(age*365)/224.7 
    rounded = round(venus)

    cars = [
        age, 
        rounded] 
    return cars

main = Main
main.start()

