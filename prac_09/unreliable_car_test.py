from prac_09.unreliable_car import UnreliableCar


def main():
    """UnreliableCar test program"""
    car = UnreliableCar("car", 100, 50)
    car.drive(20)
    print(car)


main()
