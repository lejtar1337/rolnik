'''zdefiniowanie klasy'''
class FieldManager:
    def __init__(self, filename="plik.txt"):
        self.filename = filename
    '''obliczanie powierzchni pola'''
    def calculate_field_area(self, length, width):
        
        return length * width
    '''formatuje dane działki do zapisu w pliku'''
    def format_fields_data(self, fields):
        
        fields_str = []
        for length, width in fields:
            fields_str.append(f"{length}X{width}")
        return ",".join(fields_str)
    '''zapisuje dane o działkach do pliku'''
    def write_fields_data_to_file(self, farmer, fields_data):
        
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f"{farmer}; {fields_data}\n")
    '''oblicza powierzchnie łączną działek'''
    def calculate_total_area(self, fields):
        
        total_area = 0.0
        for field in fields:
            length, width = map(float, field.split('X'))
            total_area += self.calculate_field_area(length, width)
        return total_area
    '''odczytuje dane o działkach i wyświetla je'''
    def read_and_display_fields_data(self):
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    farmer, fields_data = line.strip().split('; ')
                    fields = fields_data.split(',')
                    print(f"Rolnik: {farmer}")
                    print(f"Działki: {', '.join(fields)}")
                    total_area = self.calculate_total_area(fields)
                    print(f"Łączna powierzchnia: {total_area:.2f} m²")
                    print('-' * 40)
        except FileNotFoundError:
            print(f"Plik {self.filename} nie istnieje.")


'''przykładowe działanie pliku'''
field_manager = FieldManager()


farmer = "Jan Kowalski"
fields = [(50.0, 30.0), (20.0, 10.0), (40.0, 25.0)]  


formatted_fields_data = field_manager.format_fields_data(fields)


field_manager.write_fields_data_to_file(farmer, formatted_fields_data)


field_manager.read_and_display_fields_data()