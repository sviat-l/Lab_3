"""Module to get into OOP, create first class"""


class Markets:
    """
    Class for Markets with several variable that has two functions:
    __init__ - to initializise variables
    __str__ - to print class object info in stated format
    >>> market_family_food = Markets('Family Food', 80,\
                             ['Bread and Bakery', 'Dairy', 'Beverages'])
    >>> market_family_food.name
    'Family Food'
    >>> market_family_food.area
    80
    >>> market_family_food.food_categories
    ['Bread and Bakery', 'Dairy', 'Beverages']
    >>> print(market_family_food)
    Supermarket Family Food has an area of 80 m2 and has the following \
categories: Bread and Bakery, Dairy, Beverages.
    """

    def __init__(self, name: str, area: float, food_categories: list):
        """Init values for class Markets
        Parameters:
        :name - name of the Market
        :area - are of the Market object
        :food_categories - categories for food of the Markets object
        >>> market_family_food = Markets('Family Food', 80,\
                             ['Bread and Bakery', 'Dairy', 'Beverages'])
        >>> market_family_food.name
        'Family Food'
        >>> market_family_food.food_categories
        ['Bread and Bakery', 'Dairy', 'Beverages']
        """
        self.name = name
        self.area = area
        self.food_categories = food_categories

    def __str__(self):
        """ return print information about class object
        >>> market_family_food = Markets('Family Food', 80,\
                             ['Bread and Bakery', 'Dairy', 'Beverages'])
        >>> print(market_family_food)
        Supermarket Family Food has an area of 80 m2 and has the following \
categories: Bread and Bakery, Dairy, Beverages.
        """
        return f'Supermarket {self.name} has an area of {self.area} m2 ' +\
            'and has the following categories: ' + \
            ', '.join(self.food_categories) + '.'


# if __name__ == '__main__':
#     import doctest
#     print(doctest.testmod())
