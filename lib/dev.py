from .freebie import Freebie

class Dev:
    all = []
    def __init__( self, name ):
        self.name = name
        Dev.all.append( self )

    @property
    def freebies( self ):
        return [ f for f in Freebie.all if f.dev == self ]

    @property
    def companies( self ):
        return [ f.company for f in self.freebies ]


    def received_one( self, item_name ):
        for freebie in self.freebies:
            if freebie.item_name == item_name:
                return True
        return False
        
    # accepts a Dev instance and a Freebie instance, changes the freebie's dev 
    # to be the given dev; your code should only make the change if the freebie 
    # belongs to the dev who's giving it away
    def give_away(self, dev_recipient, freebie): 
        if freebie.dev == self:
            freebie.dev = dev_recipient
        else:
            print( 'DO NOT GIVE WHAT IS NOT YOURS!')