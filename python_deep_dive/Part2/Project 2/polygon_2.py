import math


class Polygon:
    def __init__(self, n: int, r: int):
        if n < 3:
            raise ValueError(f'Polygon must have at least 3 sides. Now have: {n}')
        self._n = n
        self._r = r

        self._interior_angle = None
        self._side_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def vertices(self):
        return self._n

    @property
    def edges(self):
        return self._n

    @property
    def circumradius(self):
        return self._r

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            self._interior_angle = (self._n - 2) * (180 / self._n)
        return self._interior_angle

    @property
    def side_length(self):
        if self._side_length is None:
            self._side_length = 2 * self._r * math.sin(math.pi / self._n)
        return self._side_length

    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self._r * math.cos(math.pi / self._n)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            self._area = self._n / 2 * self.side_length * self.apothem
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self._n * self.side_length
        return self._perimeter

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.edges == other.edges and
                    self.circumradius == other.circumradius)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.vertices > other.vertices
        else:
            return NotImplemented

    def __repr__(self):
        return f'Polygon(n={self._n}, r={self._r})'

class PolygonIterator:
    def __init__(self, m, r):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._r = r
        self._i = 3

    def __iter__(self):
        return self

    def __next__(self):
        if self._i > self._m:
            raise StopIteration
        else:
            result = Polygon(self._i, self._r)
            self._i += 1
            return result

class Polygons:
    def __init__(self, m, r):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._r = r
        # self._polygons = [Polygon(i, r) for i in range(3, m+1)]

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f'Polygons(m={self._m}, r={self._r})'

    # def __getitem__(self, item):
    #     return self._polygons[item]

    def __iter__(self):
        return PolygonIterator(self._m, self._r)

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(PolygonIterator(self._m, self._r),
                                 key=lambda p: p.area/p.perimeter,
                                 reverse=True)
        return sorted_polygons[0]



def test_polygon():
    rel_tol = 0.001
    abs_tol = 0.001

    try:
        p = Polygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not recieved')
    except ValueError:
        pass

    n = 3
    r = 1
    p = Polygon(n, r)

    assert str(p) == f'Polygon(n=3, r=1)', f'actual: {str(p)}'
    assert p.vertices == n, f'actual: {p.vertices}'
    assert p.edges == n
    assert p.circumradius == r
    assert p.interior_angle == 60

    n = 4
    r = 1
    p = Polygon(n, r)

    assert p.interior_angle == 90
    assert math.isclose(p.area, 2.0, rel_tol=rel_tol, abs_tol=abs_tol), (
        f'actual: {p.area}, expected: {2.0}'
    )
    assert math.isclose(p.side_length, math.sqrt(2), rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 4 * math.sqrt(2), rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 0.707, rel_tol=rel_tol, abs_tol=abs_tol)

    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 15)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5


if __name__ == '__main__':
    test_polygon()