from pymonad.tools import curry
from pymonad.maybe import Just, Nothing, Maybe


@curry(4)
def systolic_bp(bmi, age, gender, treatment):
    return (68.15 + 0.58 * bmi + 0.65 * age + 0.94 * gender + 6.44 * treatment)


if __name__ == '__main__':
    temp = systolic_bp(25, 50, 1)
    print(temp(0))
    print(temp(1))
    # print(systolic_bp(25, 50, 1, 0))

    # pymonad VERSION 1.0 is Error
    # temp1 = systolic_bp * Just(25) & Just(50) & Just(1) & Just(0)
    # temp2 = systolic_bp * Just(25) & Just(50) & Just(1) & Nothing

    temp1 = Maybe.apply(systolic_bp).to_arguments(Just(25), Just(50), Just(1),
                                                  Just(0))
    temp2 = Maybe.apply(systolic_bp).to_arguments(Just(25), Just(50), Just(1),
                                                  Nothing)
    print(temp1)
    print(type(temp2))
