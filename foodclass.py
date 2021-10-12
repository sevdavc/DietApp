class food():
    def __init__(self,name,change,cho,pro,fat,cal):
        self.name=name
        self.change=change
        self.cho=cho
        self.pro=pro
        self.fat=fat
        self.cal=cal


MilkObj=food("Süt",1,9,6,6,114)
MeatObj=food("Et",1,0,6,7,69)
GrainObj=food("Tahıl",1,15,2,0,68)
LegumeObj=food("Kuru Baklagil",1,15,5,0,80)
VegObj=food("Sebze",1,6,1,0,28)
FruitObj=food("Meyve",1,15,0,0,60)
FatObj=food("Yağ",1,0,0,5,45)
SugarObj=food("Şeker",1,5,0,0,20)