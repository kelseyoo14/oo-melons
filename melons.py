"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """A melon order at UberMelon."""

    # initializing class attributes that are default for all melons order
    shipped = False

    def __init__(self, species, qty, order_type, tax, country_code):
        """Initialize melon order attributes"""

        # bind user input to class attributes
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.country_code = country_code
        # 
    def get_total(self):
        """Calculate price."""

        # calculate and return a total price given tax, qty, and price
        if self.species.lower() == "christmas melon": 
            base_price = 5 * 1.5
        else: 
            base_price = 5

        total = (1 + self.tax) * self.qty * base_price
        if order_type == 'international' and qty < 10:
            total += 3
            return total
        else:
            return total

    def mark_shipped(self):
        """Set shipped to true."""

        # mark order as shipped 
        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""


    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        # user super method to use superclass init on species and qty
        super(DomesticMelonOrder, self).__init__(species, qty, 'domestic', 0.08, None)



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""


    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        # user super method to use superclass init on species and qty
        super(InternationalMelonOrder, self).__init__(species, qty, 'international', 0.17, country_code)


    def get_country_code(self):
        """Return the country code."""

        # return the value of country code 
        return self.country_code


