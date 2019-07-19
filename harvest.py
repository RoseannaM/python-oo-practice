############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    muskemelon = MelonType("musk", 1988, "green", True, True, "Muskmelon")
    all_melon_types.append(muskemelon)
    muskemelon.add_pairing("mint")


    casaba = MelonType("cas",2003,"orange",False, False, "Casaba")
    all_melon_types.append(casaba)
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")

    crenshaw = MelonType("cren",1996, "green", True ,False, "Crenshaw")
    all_melon_types.append(crenshaw)
    crenshaw.add_pairing("proscuitto")

    yellow_watermelon = MelonType("yw",2013,"yellow",True,True,"Yellow Watermelon")
    all_melon_types.append(yellow_watermelon)
    yellow_watermelon.add_pairing("ice cream")



    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    # Fill in the rest
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pair in melon.pairings:
            print(f"- {pair}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_codes = {}
    for melon in melon_types:
        melon_codes[melon.code] = melon
    # Fill in the rest
    return melon_codes

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
    
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester
        # self.sellable = None

    @property
    def sellable(self):
        return self.shape_rating > 5 and self.color_rating > 5 and self.field !=3

    # def is_sellable(self):
    #     """Evaluates if melon is sellable."""
    #     self.sellable = self.shape_rating > 5 and self.color_rating > 5 and self.field !=3
      
    #     return self.sellable

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons_by_id = make_melon_type_lookup(melon_types)
    melon_inventory = []

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_inventory.append(melon_1)

    melon_2 = Melon(melons_by_id['yw'],3,4,2,'Shiela')
    melon_inventory.append(melon_2)

    melon_3 = Melon(melons_by_id['yw'],9,8,3,'Shiela')
    melon_inventory.append(melon_3)

    melon_4 = Melon(melons_by_id['cas'],10,6,35,'Shiela')
    melon_inventory.append(melon_4)
    
    return melon_inventory

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:

        sellable = "(CAN BE SOLD)" if melon.sellable else "(NOT SELLABLE)"

        print(f"harvested by {melon.harvester} from Field {melon.field} {sellable}")

    # Fill in the rest 

test = make_melon_types()
get_sellability_report(make_melons(test))


