

from kivy.app import App
from kivy.lang import Builder


MILES_TO_KM = 1.60934


class MKMConverter(App):
    def build(self):
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('M to KM convertor.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

MKMConverter().run()
