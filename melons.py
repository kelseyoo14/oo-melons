"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """A melon order at UberMelon."""

    # initializing class attributes that are default for all melons order
    shipped = False
    order_type = None
    tax = None

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        # bind user input to class attributes
        self.species = species
        self.qty = qty

        # 
    def get_total(self):
        """Calculate price."""

        # calculate and return a total price given tax, qty, and price
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""
        
        # mark order as shipped 
        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    # instance attributes unique domestic orders only
    order_type = "domestic"
    tax = .08

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        # user super method to use superclass init on species and qty
        super(DomesticMelonOrder, self).__init__(species, qty)



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        # initializing country code based on user input
        self.country_code = country_code

        # user super method to use superclass init on species and qty
        super(InternationalMelonOrder, self).__init__(species, qty)


    def get_country_code(self):
        """Return the country code."""

        # return the value of country code 
        return self.country_code
