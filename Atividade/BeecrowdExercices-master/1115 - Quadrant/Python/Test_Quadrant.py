from Coordinate import Coordinate
from Quadrant import Quadrant


def test_should_get_quadrant_coordinate():

    a = 10
    b = 20

    quadrant = Quadrant(Coordinate(10, 20))
    quadrant2 = Quadrant(Coordinate(-8, 15))
    quadrant3 = Quadrant(Coordinate(-22, -16))
    quadrant4 = Quadrant(Coordinate(6, -15))

    # Act / Action
    result = quadrant.get_quadrant_coordinate()
    result2 = quadrant2.get_quadrant_coordinate()
    result3 = quadrant3.get_quadrant_coordinate()
    result4 = quadrant4.get_quadrant_coordinate()

    # Assert
    assert result == "First"
    assert result2 == "Second"
    assert result3 == "Third"
    assert result4 == "Fourth"



