from math import sqrt
from structures.PointsVector import PointsVector


class MaxMovingEuclidean:

    def __init__(self):
        self.windowsize = 3

    def dist(self, value1, value2):
        diff = value1 - value2
        return diff * diff

    def calculate(self,  dense_vector1, dense_vector2):
        vector1 = dense_vector1.values
        vector2 = dense_vector2.values
        assert len(vector1) == len(vector2), "vectors must be of equal sizes"
        distance = 0
        prev = 0
        for i in range(0, len(vector1)):
            max_value = float("-inf")
            begin_value = max(prev, i - self.windowsize)
            end_value = min(len(vector2) - 1, i + self.windowsize)

            for j in range(begin_value, end_value + 1):
                value = self.dist(vector1[i], vector2[j]);
                if max_value < value:
                    max_value = value
                    prev = j
            distance += max_value

        return sqrt(distance)


def main():
    abstract_dissimilarity = MaxMovingEuclidean()
    vector1 = [7876206.000000, 2.721705, 2.482324, 510.317183, 1310.820459, 907.367521, 594.858896]
    vector2 = [7537091.000000, 3.262750, 3.004038, 518.909965, 1310.309662, 1107.230769, 733.423313]
    vector3 = [7421256.000000, 3.462628, 3.211842, 524.057260, 1306.746288, 1179.025641, 786.895706]
    vector4 = [7284190.000000, 3.630403, 3.402637, 523.408172, 1303.025129, 1241.683761, 837.233129]
    dense_vector1 = PointsVector(vector1, 1, "")
    dense_vector2 = PointsVector(vector2, 2, "")
    dense_vector3 = PointsVector(vector3, 3, "")
    dense_vector4 = PointsVector(vector4, 4, "")
    print(abstract_dissimilarity.calculate(dense_vector1, dense_vector2))
    print(abstract_dissimilarity.calculate(dense_vector1, dense_vector3))
    print(abstract_dissimilarity.calculate(dense_vector1, dense_vector4))
    print(abstract_dissimilarity.calculate(dense_vector2, dense_vector3))
    print(abstract_dissimilarity.calculate(dense_vector2, dense_vector4))
    print(abstract_dissimilarity.calculate(dense_vector3, dense_vector4))


if __name__ == "__main__":
    main()
