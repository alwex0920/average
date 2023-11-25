from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class AverageCalculator(App):
    def build(self):
        self.numbers_input = TextInput(hint_text='Enter numbers example 3 4 5', multiline=False)
        self.result_label = Label(text='Average: ')

        # Кнопка для вычисления среднего арифметического
        calculate_button = Button(text='Calculate', on_press=self.calculate_average)

        # Основной макет
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(self.numbers_input)
        layout.add_widget(calculate_button)
        layout.add_widget(self.result_label)

        return layout

    def calculate_average(self, instance):
        try:
            # Получаем введенные числа и вычисляем среднее арифметическое
            numbers = [float(x) for x in self.numbers_input.text.split()]
            average = sum(numbers) / len(numbers)

            # Выводим результат
            self.result_label.text = f'Average: {average:.2f}'
        except ValueError:
            self.result_label.text = 'Error.'

if __name__ == '__main__':
    AverageCalculator().run()