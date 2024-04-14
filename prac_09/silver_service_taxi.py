from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialized version of Taxi"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0):
        """Initialize Silver Service Taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness
        
    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
        
    def get_fare(self):
        """Get the current fare"""
        return self.flagfall + super().get_fare()
