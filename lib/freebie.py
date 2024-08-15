
class Freebie:
    all = []
    def __init__(self, item_name, value, company, dev):
        self.item_name = item_name
        self.value = value 

        self.company = company 
        self.dev = dev

        Freebie.all.append(self)

    def print_details(self):
        return f'{self.dev.name} owns a {self.item_name} from {self.company.name}'
    
    def __repr__(self):
        return f'<Freebie item_name={self.item_name} value={self.value} company={self.company.name} dev={self.dev.name} />'