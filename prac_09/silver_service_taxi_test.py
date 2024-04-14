from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    silver_taxi = SilverServiceTaxi("Test", 100, 2)
    silver_taxi.drive(18)
    print(silver_taxi.get_fare())


main()
