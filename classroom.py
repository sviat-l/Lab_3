"""MODULE WITH CLASSROOM CLASS"""
from typing import List

class Classroom:
    """
    Class that has 2 modules is_larger, equipment_differences
    >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> classroom_007 = Classroom('007', 12, ['TV'])
    >>> classroom_016.number
    '016'
    >>> classroom_016.capacity
    80
    >>> classroom_016.equipment
    ['PC', 'projector', 'mic']
    >>> print(classroom_016)
    Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
    >>> classroom_016.equipment_differences(classroom_007)
    ['PC', 'mic', 'projector']
    >>> classroom_016.is_larger(classroom_007)
    True
    >>> classroom_016
    Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> [classroom_016]
    [Classroom('016', 80, ['PC', 'projector', 'mic'])]
    """

    def __init__(self, number: str, capacity: int, equipment: List[str]) -> None:
        """
        Init class values
        """
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __str__(self) -> str:
        """ Return str from text in which print class object information """
        return f'Classroom {self.number} has a capacity of {self.capacity} persons ' +\
            'and has the following equipment: ' + ', '.join(self.equipment)+'.'

    def __repr__(self) -> None:
        """ Return string in which represent the class object """
        return 'Classroom' + str(tuple([self.number, self.capacity, self.equipment]))

    def is_larger(self, other_classroom_object) -> bool:
        """Return bool value True if capacity of self classroom is more then of other
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.is_larger(classroom_007)
        True
        >>> classroom_000 = Classroom('000', 20, ['PC'])
        >>> classroom_007 = Classroom('007', 20, ['TV'])
        >>> classroom_000.is_larger(classroom_007)
        False
        """
        return self.capacity > other_classroom_object.capacity

    def equipment_differences(self, other_classroom) -> List[str]:
        """Return equipment which is in self auditory but is not in other in alphabetic order
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.equipment_differences(classroom_007)
        ['PC', 'mic', 'projector']
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['PC', 'projector'])
        >>> classroom_016.equipment_differences(classroom_007)
        ['mic']
        """
        return sorted(list(set(self.equipment) - set(other_classroom.equipment)))

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
