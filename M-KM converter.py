

from kivy.app import App
from kivy.lang import Builder

KM_TO_MILE = 1/1.60934
MILES_TO_KM = 1.60934


class MilesConverterApp(App):


    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('M-KM converter.kv')
        self.milesToKM = True
        return self.root

    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.value_input.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 1/-1

    def handle_calculate(self):
        value = self.get_validated_KM()
        if self.milesToKM:
            result = value * MILES_TO_KM
        else:
            result = value * KM_TO_MILE
        self.root.ids.output_label.text = str(result)

    def convert_change(self):
        self.milesToKM = not bool(self.milesToKM)

        if self.milesToKM:
            self.root.ids.convert_change.text = "Miles to KM"
        else:
            self.root.ids.convert_change.text = "KM to Miles"

        self.root.ids.value_input.text = str(self.root.ids.output_label.text)
        self.handle_calculate()

    def handle_increment(self, change):
        value = self.get_validated_KM() + change
        self.root.ids.input_KM.text = str(value)
        self.handle_calculate()

    def get_validated_KM(self):
        try:
            value = float(self.root.ids.value_input.text)
            return value
        except ValueError:
            return 1/-1

MilesConverterApp().run()
