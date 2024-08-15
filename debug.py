import ipdb
from lib import *

#code here


c1 = Company(name="Tech Innovators Inc.", year=2001)
c2 = Company(name="Green Solutions Ltd.", year=2010)
c3 = Company(name="Global Dynamics LLC", year=1998)
c4 = Company(name="Future Horizons Co.", year=2023)
c5 = Company(name="Pioneer Enterprises", year=1985)

dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
dev3 = Dev(name="Charlie")
dev4 = Dev(name="Dana")
dev5 = Dev(name="Eve")

freebie1 = Freebie(item_name="T-Shirt", value=20, company=c1, dev=dev2)
freebie2 = Freebie(item_name="Mug", value=15, company=c2, dev=dev2)
freebie3 = Freebie(item_name="Notebook", value=10, company=c3, dev=dev3)
freebie4 = Freebie(item_name="Pen", value=5, company=c4, dev=dev4)
freebie5 = Freebie(item_name="Sticker", value=2, company=c5, dev=dev5)

freebie6 = Freebie(item_name="Backpack", value=25, company=c1, dev=dev4)
freebie7 = Freebie(item_name="Hat", value=12, company=c2, dev=dev2)
freebie8 = Freebie(item_name="Mousepad", value=8, company=c3, dev=dev3)
freebie9 = Freebie(item_name="Water Bottle", value=18, company=c4, dev=dev4)
freebie10 = Freebie(item_name="USB Drive", value=30, company=c5, dev=dev5)

freebie11 = Freebie(item_name="Keychain", value=4, company=c1, dev=dev1)
freebie12 = Freebie(item_name="Desk Organizer", value=22, company=c2, dev=dev2)
freebie13 = Freebie(item_name="Phone Stand", value=14, company=c3, dev=dev5)
freebie14 = Freebie(item_name="Notebook", value=10, company=c4, dev=dev5)
freebie15 = Freebie(item_name="Bluetooth Speaker", value=50, company=c5, dev=dev5)

import ipdb
ipdb.set_trace()