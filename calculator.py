import kivy

kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalcGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                return str(eval(calculation))
            except Exception:
                self.display.text = "Error"

    def decimal(self, equation):
        plus = equation.rfind("+")
        sub = equation.rfind("-")
        mult = equation.rfind("*")
        div = equation.rfind("/")
        maximum = max(plus, sub, mult, div)
        substr = equation[maximum+1:]
        if "." not in substr:
            return str(equation+".")
        else:
            return str(equation)



class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()

if __name__ == '__main__':
    CalculatorApp().run()
