""" module to with AcademicBuilding Class"""
from typing import List
import classroom

class AcademicBuilding:
    """Class Academ Buildings. It has method total_equipment. Uses Classroom class
    >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
    >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
    >>> classrooms = [classroom_016, classroom_007, classroom_008]
    >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
    >>> building.address
    'Kozelnytska st. 2a'
    >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
    >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
    >>> classrooms = [classroom_016, classroom_007, classroom_008]
    >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
    >>> building.address
    'Kozelnytska st. 2a'
    >>> print(building)
    Kozelnytska st. 2a
    Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
    Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
    Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
    """
    def __init__(self, address:str, classrooms:List[classroom.Classroom]) -> None:
        """
        Init class values function
        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.address
        'Kozelnytska st. 2a'
        >>> for room in building.classrooms:    print(room)
        Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector,\
 mic.
        Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
        """
        self.address = address
        self.classrooms = classrooms
    def total_equipment(self):
        """Return total equipments in academic building
        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.total_equipment()
        [('PC', 2), ('TV', 1), ('mic', 1), ('projector', 2)]
        """
        equipment_dict = {}
        for class_room in self.classrooms:
            for eqp in class_room.equipment:
                equipment_dict[eqp] = equipment_dict.get(eqp, 0) + 1
        return sorted(list(equipment_dict.items()))
    def __str__(self) -> str:
        """ Return string to be printed on request """
        result = self.address
        for room in self.classrooms:
            result+= f'\nClassroom {room.number} has a capacity of {room.capacity} persons ' +\
            'and has the following equipment: ' + ', '.join(room.equipment)+'.'
        return result
