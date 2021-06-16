import datetime

class Main:
   def start():


    dt = datetime.date.today()

    Fname=str()
    Lname=str()
    Date=int()


    age =Main.calc(int(Date))[0]
    SpaceAge=Main.calc(int(Date))[1]
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



