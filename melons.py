"""Classes for melon orders."""


class AbstractMelonOrder():
    def __init__(self, species, qty, order_type, tax):
        self.species= species 
        self.qty= qty
        self.order_type= order_type
        self.tax=tax
        self.ship= False


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order purchased by the US Government."""

    def __init__(self, species, qty):
        super().__init__(species, qty, "government", 0.0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Record whether the melon order has passed inspection or not."""

        self.passed_inspection = passed



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08 )
        

    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas melon":
            base_price=5
            new_price= base_price*1.5

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
   
    
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", 0.17)
        self.country_code=country_code


    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas melon":
            base_price=5
            new_price= base_price*1.5

        if self.qty <10:
            base_price = 5
            new_price= base_price +3
            total = (1 + self.tax) * self.qty * new_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
