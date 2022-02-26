"""Program to run logistic system with track functional"""


class Location:
    """class Location with info and method that refers to the Locations"""

    def __init__(self, city: str, post_office: int) -> None:
        """Init Function
        >>> located = Location('Lviv', 73000)
        >>> located.city
        'Lviv'
        >>> located.post_office
        73000
        """
        self.city = city
        self.post_office = post_office

    def __str__(self) -> str:
        """
        Return string with text format in which print class object information
        >>> located = Location('Lviv', 73000)
        >>> print(located)
        City: Lviv with post office number: 73000
        """
        return f"City: {self.city} with post office number: {self.post_office}"


class Item:
    """Class Item with information and methods related to one Item"""

    def __init__(self, name: str, price: float) -> None:
        """
        Init class values
        >>> item = Item('book', 100)
        >>> item.name
        'book'
        >>> item.price
        100
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        Return string with text format in which print class object information
        >>> test_item = Item('Pen', 10)
        >>> print(test_item)
        Item: Pen has price: 10
        """
        return f"Item: {self.name} has price: {self.price}"


class Vehicle:
    """
    Class Vehicle with information and methods reletad to vehicles
    """

    def __init__(self, vehicle_no: int, is_available: bool = True) -> None:
        """
        Init class values
        >>> vehocle = Vehicle(1, False)
        >>> vehocle.vehicle_no
        1
        >>> vehocle.is_available
        False
        """
        self.vehicle_no = vehicle_no
        self.is_available = is_available


class Order:
    """
    Class with information and methods related to order system
    """

    def __init__(self, order_id: int, user_name: str, location: Location,
                 items: list[Item], vehicle: Vehicle = None) -> None:
        """
        >>> items = [Item('laptop',1000), Item('book',100), Item('pencil', 10)]
        >>> case_order = Order(order_id=0 ,user_name='Oleg',\
                               location=Location('Lviv', 73000), items=items)
        >>> case_order.user_name
        'Oleg'
        """
        self.order_id = order_id
        self.user_name = user_name
        self.location = location
        self.items = items
        self.vehicle = vehicle

    def __str__(self) -> str:
        """
        >>> items = [Item('laptop',1000), Item('book',100), Item('pencil', 10)]
        >>> case_order = Order(order_id=0 ,user_name='Oleg', location=Location('Lviv', 73000), items=items)
        >>> print(case_order)
        Order nubmer:0 from Oleg to City: Lviv with post office number: 73000. with total price: 1110
        """
        return f"Order nubmer:{str(self.order_id)} from {self.user_name} to {self.location}. " +\
               f"with total price: {self.calculate_amount()}"

    def calculate_amount(self) -> int:
        """ Calculate number of total items
        >>> items = [Item('laptop',1000), Item('book',100), Item('pencil', 10)]
        >>> case_order = Order(order_id=0 ,user_name='Oleg', location=Location('Lviv', 73000), items=items)
        >>> case_order.calculate_amount()
        1110
        """
        return sum(item.price for item in self.items)


class LogisticSystem:
    """
    Class to run all logistic system, uses other class.

    >>> test_system = LogisticSystem(orders = {},\
        vehicles=[Vehicle(0, False), Vehicle(1, True)])
    >>> items = [Item('laptop',1000), Item('book',100), Item('pencil', 10)]
    >>> case_order = Order(order_id=0 ,user_name='Oleg',\
                        location=Location('Lviv', 73000), items=items)
    >>> test_system.place_order(case_order)
    Order was send on vehicle: 1
    >>> test_system.track_order(0)
    'Order nubmer:0 from Oleg to City: Lviv with post office number: 73000. \
with total price: 1110'
    >>> test_system.track_order(0)
    'Order nubmer:0 from Oleg to City: Lviv with post office number: 73000. with total price: 1110'
    >>> test_system.track_order(1)
    'No order on that order_id'

    # >>> test_system = LogisticSystem(orders = {},\
    #     vehicles=[Vehicle(0, False), Vehicle(1, False)])
    >>> items = [Item('laptop',1000), Item('book',100), Item('pencil', 10)]
    >>> case_order = Order(order_id=0 ,user_name='Paul',\
                        location=Location('Lviv', 73000), items=items)
    >>> test_system.place_order(case_order)
    There are no available vehicles. Please wait...
    """

    def __init__(self, orders: dict[int:Order], vehicles: list[Vehicle]) -> None:
        """
        Init Class values
        >>> test_system = LogisticSystem(orders = {},\
         vehicles=[Vehicle(0, False), Vehicle(1, True)])
        >>> test_system.vehicles[1].vehicle_no
        1
        >>> test_system.orders
        {}
        """
        self.vehicles = vehicles
        self.orders = orders

    def place_order(self, order: Order) -> None:
        """
        Add order in a row
        >>> test_system = LogisticSystem(orders = {},\
         vehicles=[Vehicle(0, False), Vehicle(1, True)])
        >>> items = [Item('laptop',1000), Item('book',100), Item('pencil', 10)]
        >>> case_order = Order(order_id=0 ,user_name='Oleg',\
                         location=Location('Lviv', 73000), items=items)
        >>> test_system.place_order(case_order)
        Order was send on vehicle: 1

        """
        for vehicle in self.vehicles:
            if vehicle.is_available:
                order.vehicle = vehicle
                vehicle.is_available = False
                self.orders[order.order_id] = order
                return print(f'Order was send on vehicle: {vehicle.vehicle_no}')
        return print('There are no available vehicles. Please wait...')

    def track_order(self, order_id: int) -> str:
        """Return information about order
        >>> test_system = LogisticSystem(orders = {},\
         vehicles=[Vehicle(0, False), Vehicle(1, True)])
        >>> items = [Item('laptop',1000), Item('book',100), Item('pencil', 10)]
        >>> case_order = Order(order_id=0 ,user_name='Oleg',\
                         location=Location('Lviv', 73000), items=items)
        >>> test_system.place_order(case_order)
        Order was send on vehicle: 1
        >>> test_system.track_order(0)
        'Order nubmer:0 from Oleg to City: Lviv with post office number: 73000. \
with total price: 1110'
        >>> test_system.track_order(1)
        'No order on that order_id'
        """
        if order_id in self.orders:
            return str(self.orders[order_id])
        return 'No order on that order_id'
