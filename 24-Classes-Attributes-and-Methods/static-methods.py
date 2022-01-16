class WeatherForecast():
    def __init__(self, temperatures):
        self.temperatures = temperatures


    @staticmethod
    def convert_from_fahrenheit_to_celsius(fahrenheit):
        calculation = (fahrenheit - 32) * 5 / 9
        return round(calculation, 2)

    def in_celsius(self):
        return [self.convert_from_fahrenheit_to_celsius(temp) for temp in self.temperatures]

wf = WeatherForecast([100, 90, 80, 70, 60])
print(wf.in_celsius()) # [37.78, 32.22, 26.67, 21.11, 15.56]

# can be called on the class, not just self as above:
print(WeatherForecast.convert_from_fahrenheit_to_celsius(100)) # 37.78