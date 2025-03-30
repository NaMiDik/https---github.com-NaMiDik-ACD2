import tkinter as tk
from main import DynamicArray

class App:
    def __init__(self, root):
        self.array = DynamicArray()  # Створюємо динамічний масив
        self.root = root
        self.root.title("Взаємодія з динамічним масивом")
        self.root.geometry("1200x700")  # Збільшуємо розмір вікна

        # Створюємо елементи інтерфейсу
        self.label = tk.Label(root, text="Елементи масиву: []")
        self.label.pack(pady=10)

        # Поле для вводу ключа (значення)
        self.key_label = tk.Label(root, text="Введіть ключ (значення):")
        self.key_label.pack(pady=5)
        self.key_entry = tk.Entry(root, width=30)
        self.key_entry.pack(pady=5)

        # Поле для вводу індексу
        self.index_label = tk.Label(root, text="Введіть індекс (кількість елементів для рандомного заповнення):")
        self.index_label.pack(pady=5)
        self.index_entry = tk.Entry(root, width=30)
        self.index_entry.pack(pady=5)

        # Кнопки для взаємодії
        self.add_button = tk.Button(root, text="Додати елемент в кінець", command=self.add_element)
        self.add_button.pack(pady=5)

        self.add_at_index_button = tk.Button(root, text="Додати елемент за індексом", command=self.add_element_at_index)
        self.add_at_index_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Видалити елемент за індексом", command=self.remove_element)
        self.remove_button.pack(pady=5)

        self.remove_by_key_button = tk.Button(root, text="Видалити елемент за ключем", command=self.remove_by_key)
        self.remove_by_key_button.pack(pady=5)

        self.find_index_button = tk.Button(root, text="Пошук за індексом", command=self.find_by_index)
        self.find_index_button.pack(pady=5)

        self.find_key_button = tk.Button(root, text="Пошук за значенням", command=self.find_by_key)
        self.find_key_button.pack(pady=5)

        # Кнопки для додаткових операцій
        self.min_abs_button = tk.Button(root, text="Мінімум за модулем", command=self.find_min_abs)
        self.min_abs_button.pack(pady=5)

        self.sum_after_zero_button = tk.Button(root, text="Сума після нуля", command=self.calculate_sum_after_zero)
        self.sum_after_zero_button.pack(pady=5)

        self.transform_button = tk.Button(root, text="Перетворити масив", command=self.transform_array)
        self.transform_button.pack(pady=5)

        # Кнопка для заповнення масиву випадковими значеннями
        self.fill_random_button = tk.Button(root, text="Заповнити рандомними значеннями", command=self.fill_random)
        self.fill_random_button.pack(pady=5)

        # Поле для результатів пошуку або помилок
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def update_label(self):
        """Оновлює мітку з елементами масиву та забезпечує автоматичне перенесення тексту."""
        # Отримуємо ширину вікна
        window_width = self.root.winfo_width()
    
        # Встановлюємо wraplength для мітки, щоб текст не виходив за межі вікна
        # wraplength буде обчислюватися залежно від ширини вікна, віднімаючи відступи
        self.label.config(
            text=f"Елементи масиву: {self.array.display()}",
            wraplength=window_width - 40,  # Віднімаємо відступи для краю вікна
            anchor='center',  # Вирівнювання по центру
            font=('Arial', 10),  # Шрифт
            padx=10, pady=10  # Відступи
        )


    def add_element(self):
        """Викликає метод додавання елемента в кінець масиву"""
        value = self.key_entry.get()
        if value:
            self.array.add(value)
            self.update_label()

    def add_element_at_index(self):
        """Викликає метод додавання елемента на вказаний індекс"""
        value = self.key_entry.get()  # Отримуємо значення елемента
        index = self.get_index_from_input()  # Отримуємо індекс із введеного значення
        if value and index is not None:
            if 0 <= index <= self.array.size:  # Перевіряємо, чи індекс в межах масиву
                self.array.add_at_index(value, index)  # Викликаємо метод для додавання
                self.update_label()
            else:
                self.result_label.config(text="Помилка: Індекс знаходиться за межами масиву")


    def remove_element(self):
        """Викликає метод видалення елемента за індексом"""
        index = self.get_index_from_input()
        if index is not None:
            try:
                self.array.remove(index)
                self.update_label()
            except IndexError as e:
                self.result_label.config(text=f"Помилка: {e}")

    def remove_by_key(self):
        """Викликає метод видалення елемента за ключем"""
        key = self.key_entry.get()
        if key:
            try:
                self.array.remove_by_key(key)
                self.update_label()
            except ValueError as e:
                self.result_label.config(text=f"Помилка: {e}")

    def find_by_index(self):
        """Викликає метод пошуку елемента за індексом"""
        index = self.get_index_from_input()
        if index is not None:
            try:
                result = self.array.find_by_index(index)
                self.result_label.config(text=f"Знайдено елемент: {result}")
            except IndexError as e:
                self.result_label.config(text=f"Помилка: {e}")

    def find_by_key(self):
        """Викликає метод пошуку елемента за значенням"""
        key = self.key_entry.get()
        if key:
            try:
                index = self.array.find_by_key(key)
                self.result_label.config(text=f"Знайдено на індексі: {index}")
            except ValueError as e:
                self.result_label.config(text=f"Помилка: {e}")

    def find_min_abs(self):
        """Знаходить мінімальний за модулем елемент"""
        try:
            min_abs_element = self.array.find_min_abs()
            self.result_label.config(text=f"Мінімальний за модулем елемент: {min_abs_element}")
        except ValueError as e:
            self.result_label.config(text=f"Помилка: {e}")

    def calculate_sum_after_zero(self):
        """Обчислює суму абсолютних значень елементів після нульового елемента"""
        sum_after_zero = self.array.sum_after_zero()
        if isinstance(sum_after_zero, str):  # Перевіряємо, чи це повідомлення про помилку
            self.result_label.config(text=sum_after_zero)
        else:
            self.result_label.config(text=f"Сума після нуля: {sum_after_zero}")


    def transform_array(self):
        """Перетворює масив (парні/непарні позиції)"""
        try:
            transformed_array = self.array.transform_array()
            self.result_label.config(text=f"Перетворений масив: {transformed_array}")
        except ValueError as e:
            self.result_label.config(text=f"Помилка: {e}")

    def fill_random(self):
        """Заповнює масив випадковими значеннями, кількість елементів з поля індексу"""
        num_elements = self.get_index_from_input()
        if num_elements is not None:
            self.array.fill_random(num_elements)
            self.update_label()

    def get_index_from_input(self):
        """Отримує кількість елементів для генерації з поля індексу"""
        try:
            return int(self.index_entry.get())
        except ValueError:
            self.result_label.config(text="Будь ласка, введіть кількість елементів (ціле число)")
            return None

# Створюємо вікно Tkinter
root = tk.Tk()
app = App(root)
root.mainloop()
