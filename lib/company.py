from .freebie import Freebie

class Company:
    all = []
    def __init__(self, name, year):
        self.name = name 
        self.year = year 
        Company.all.append(self)

    def freebies(self):
        #look through all freebies
        #flter out freebies with matching company 
        return [freebie for freebie in Freebie.all if freebie.company == self]
    
    def devs(self):
        #look through all freebies for this company 
        #extract the dev 
        return list(set([freebie.dev for freebie in self.freebies()]))
    
    def give_freebie(self, dev, item_name, value):
        return Freebie(dev=dev, company=self, item_name=item_name, value=value)
    
    @classmethod 
    def oldest_company(cls):
        #look through all companies
        #keep track of oldest company
        oldest_year = float('inf')
        oldest_company = None 
        for company in Company.all:
            if(company.year < oldest_year):
                #updating our trackers for oldest companies
                #so we can continue comparing with the next companies in the list
                oldest_year = company.year 
                oldest_company = company 
        return oldest_company

    def __repr__(self):
        return f'<Company name={self.name} year={self.year} />'
    
