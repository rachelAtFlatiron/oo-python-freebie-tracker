import ipdb
from lib import *

#code here

apple = Company( 'Apple Inc', 1976 )
ibm = Company( 'IBM computers', 1911 )
google = Company( 'Google Search', 1998 )

adam = Dev( 'Adam' )
emiley = Dev( 'Emiley' )
norris = Dev( 'Norris' )

ibm.give_freebie( emiley, "Rolex", 70000 )
the_sticker = Freebie( adam, apple, "Sticker", 5 )

the_lambo = Freebie( emiley, google, "Lambo", 250000 )



ipdb.set_trace()