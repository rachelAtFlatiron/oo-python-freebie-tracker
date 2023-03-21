from .freebie import Freebie

class Company:
    all = []
    def __init__( self, name, year ):
        self.name = name
        self.founding_year = year
        Company.all.append( self )

    @property
    def freebies( self ):
        # our_final_list = []
        # for freebie in Freebie.all:
        #     if freebie.company == self:
        #         our_final_list.append( freebie )
        # return our_final_list
        return [ f for f in Freebie.all if f.company == self ]

    @property
    def devs( self ):
        return [ f.dev for f in self.freebies ]

    # takes a dev (an instance of the Dev class), an item_name (string), and a 
    # value as arguments, and creates a new Freebie instance associated with 
    # this company and the given dev.
    def give_freebie( self, dev_instance, item_name, value ):
        Freebie( dev_instance, self, item_name, value )

    # returns the Company instance with the earliest founding year
    @classmethod
    def oldest_company( cls ):
        earliest_year = 3000
        found_instance = 'We tried to search nothing?'

        for company in cls.all:
            if company.founding_year < earliest_year:
                earliest_year = company.founding_year
                found_instance = company
        return found_instance
