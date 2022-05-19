from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

# set window size
Window.size = (400, 500)
# link to the design file
Builder.load_file('calculatorlayout.kv')


class CalLayout(Widget):
    # clear button function
    def clear(self):
        self.ids.cal_input.text = "0"

    # create function that remove the last digit
    def backward(self):
        prev = self.ids.cal_input.text
        prev = prev[:-1]
        self.ids.cal_input.text = prev

    # change sign function
    def pos_neg(self):
        prev = self.ids.cal_input.text
        if "-" in prev:
            self.ids.cal_input.text = f'{prev.replace("-","")}'
        else:
            self.ids.cal_input.text = f'-{prev}'

    # create percentage function
    # "120" --- > "1.2"
    def percentage(self):
        cur = self.ids.cal_input.text
        # eval the math from the string
        try:
            ans = eval(cur)/100
            self.ids.cal_input.text = str(ans)
        except:
            self.ids.cal_input.text = "error"

    # number pressing function
    def num_press(self, val):
        # need to obtain whatever is in the textbox first
        prev = self.ids.cal_input.text
        if "error" in prev:
            prev = ""
        if prev == '0':
            self.ids.cal_input.text = ""
            self.ids.cal_input.text = f"{val}"
        elif prev != '0':
            self.ids.cal_input.text = f"{prev}{val}"

    # decimal function
    def dot(self):
        prev = self.ids.cal_input.text
        if prev[-1] != ".":
            self.ids.cal_input.text = f'{prev}.'

    # math_sign function
    def math_sign(self, sign):
        prev = self.ids.cal_input.text
        self.ids.cal_input.text = f"{prev}{sign}"

    def equals(self):
        cur = self.ids.cal_input.text
        # eval the math from the string
        try:
            ans = eval(cur)
            self.ids.cal_input.text = str(ans)
        except:
            self.ids.cal_input.text = "error"


class CalculatorApp(App):
    def build(self):
        return CalLayout()


if __name__ == "__main__":
    CalculatorApp().run()
