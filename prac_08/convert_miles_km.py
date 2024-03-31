from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

KILOMETRE_EQUIVALENT = 1.60934


class KmConversionApp(App):
    """KmConversionApp is a Kivy app to convert miles to Km"""
    message = StringProperty()

    def build(self):
        """Build the app"""
        self.title = "Convert Miles To Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.message = ''
        return self.root

    def handle_calculation(self, value):
        """Calculates the conversion of miles to kilometres"""
        try:
            result = float(value) * KILOMETRE_EQUIVALENT
            self.message = str(result)
        except ValueError:
            self.root.ids.user_input.text = "0.0"

    def handle_increment(self, increment):
        """Increase or decrease the input value"""
        try:
            if self.root.ids.user_input.text == '':
                self.root.ids.user_input.text = str(increment)
            else:
                new_value = float(self.root.ids.user_input.text) + increment
                self.root.ids.user_input.text = str(new_value)
        except ValueError:
            self.root.ids.user_input.text = "0.0"


KmConversionApp().run()
