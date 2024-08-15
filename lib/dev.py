from .freebie import Freebie
import ipdb 
class Dev:
    def __init__(self, name):
        self.name = name 

    def freebies(self):
        return [freebie for freebie in Freebie.all if freebie.dev == self]
    
    def companies(self):
        #look through all freebies for this company (self.freebies())
        #extract the company 
        return list(set([freebie.company for freebie in self.freebies()]))
    
    def received_one(self, item_name):
        #look through all self's freebies
        #check if any of the freebies item_name==item_name
        for freebie in self.freebies():
            if(freebie.item_name == item_name):
                return True 
        return False

    def give_away(self, dev, freebie):
        freebie.dev = dev 
        
    def __repr__(self):
        return f'<Dev name={self.name} />'

