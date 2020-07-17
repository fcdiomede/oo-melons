"""Classes for melon orders."""

from random import randint
import datetime as dt

class AbstractMelonOrder():
    """ An abstract base class that other melon orders inhert from """
    order_type = "Not Set"
    tax = 0.00
    shipped = False

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        if qty > 100:
            raise TooManyMelonsError("No more than 100 melons!")

        self.species = species
        self.qty = qty


    def get_base_price(self):
        """Determine a random price for melons, accounting for splurge pricing"""
        current_time = dt.datetime.now() 
        current_hour = current_time.hour
        current_weekday = current_time.weekday()

        base_price = randint(5,9)

        if (
            (current_weekday <= 5) #It is currently Mon-Fri
            and
            (current_hour >= 8 and current_hour < 11) #It is betwwn 8-11AM
            ):
            base_price += 4.00

        return base_price


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):

        if self.qty < 10:
            return super().get_total() + 3.00
        else:
            return super().get_total()

class GovernmentMelonOrder(AbstractMelonOrder):
    passed_inspection = False

    def mark_inspection(passed):
        self.passed_inspection = passed

class TooManyMelonsError(ValueError):
    """Raise an error when too many melons are ordered"""
