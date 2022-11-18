class Racer:
  def intro(self):
    print("I am a racer")
     
  def bike(self):
    print("I have a bike")
   
class Honda(Racer):
  def bike(self):
    print("I am a racer from Honda")
     
class Yamaha(Racer):
  def bike(self):
    print("I am a racer from Yamaha.")
     
racer1 = Racer()
racer2 = Honda()
racer3 = Yamaha()
 
racer1.intro()
racer1.bike()
racer2.bike()
racer3.bike()