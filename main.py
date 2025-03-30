import random

class DynamicArray:
    def __init__(self):
        self.size = 0  # Поточна кількість елементів
        self.capacity = 1  # Початкова місткість масиву
        self.array = [None] * self.capacity  # Масив з початковим розміром 1

    def __resize(self, new_capacity):
        """Змінює розмір масиву"""
        new_array = [None] * new_capacity  # Створюємо новий масив з більшою місткістю
        for i in range(self.size):
            new_array[i] = self.array[i]  # Копіюємо всі елементи старого масиву в новий
        self.array = new_array  # Заміщуємо старий масив новим
        self.capacity = new_capacity  # Оновлюємо місткість

    def add(self, value):
        """Додає елемент до кінця масиву"""
        if self.size == self.capacity:
            self.__resize(self.capacity * 2)  # Подвоюємо розмір, якщо масив переповнений
        self.array[self.size] = value  # Додаємо елемент в кінець масиву
        self.size += 1  # Збільшуємо розмір масиву

    def add_at_index(self, value, index):
        """Додає елемент на вказану позицію"""
        if index < 0 or index > self.size:
            raise IndexError("Індекс знаходиться за межами масиву")
    
        if self.size == self.capacity:
            self.__resize(self.capacity * 2)  # Якщо масив переповнений, збільшуємо його розмір
    
        # Переміщаємо елементи вправо, щоб звільнити місце для нового елемента
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
    
        self.array[index] = value  # Вставляємо новий елемент
        self.size += 1


    def remove(self, index):
        """Видаляє елемент за індексом"""
        if 0 <= index < self.size:
            # Переміщаємо всі елементи після видаленого на одну позицію вліво
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = None  # Очищаємо останній елемент
            self.size -= 1
        else:
            raise IndexError("Індекс знаходиться за межами масиву")

    def remove_by_key(self, key):
        """Видаляє елемент за значенням (ключем)"""
        for i in range(self.size):
            if self.array[i] == key:
                # Переміщаємо всі елементи після видаленого на одну позицію вліво
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.array[self.size - 1] = None  # Очищаємо останній елемент
                self.size -= 1
                return
        raise ValueError("Елемент з таким значенням не знайдено")

    def find_by_index(self, index):
        """Пошук елемента за індексом"""
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("Індекс знаходиться за межами масиву")

    def find_by_key(self, key):
        """Шукає елемент за значенням (лінійний пошук)"""
        for i in range(self.size):
            if self.array[i] == key:
                return i  # Повертає індекс знайденого елемента
        raise ValueError("Елемент з таким значенням не знайдено")

    def find_min_abs(self):
        """Знаходить мінімальний за модулем елемент"""
        if self.size == 0:
            raise ValueError("Масив порожній")
        return min(self.array[:self.size], key=abs)

    def sum_after_zero(self):
        """Підсумовує абсолютні значення елементів після першого нульового елемента"""
        print("Масив на момент виклику: ", self.array)  # Лог для перевірки стану масиву
    
        # Перетворюємо всі елементи на числа, щоб у разі наявності рядка '0' ми могли його обробити
        self.array = [int(x) if isinstance(x, str) and x.isdigit() else x for x in self.array]
    
        if 0 not in self.array:
            return "Немає нульового елемента в масиві"
    
        zero_index = self.array.index(0)  # Знаходимо індекс першого нульового елемента
        print("Індекс нулевого елемента: ", zero_index)  # Лог для перевірки індексу
    
        return sum(abs(x) for x in self.array[zero_index + 1:])

    def transform_array(self):
        """Перетворює масив (парні/непарні позиції)"""
        if self.size % 2 != 0:
            raise ValueError("Масив має бути парної довжини")
        even_pos = [self.array[i] for i in range(1, self.size, 2)]
        odd_pos = [self.array[i] for i in range(0, self.size, 2)]
        self.array = even_pos + odd_pos
        return self.array

    def fill_random(self, num_elements):
        """Заповнює масив випадковими числами"""
        for _ in range(num_elements):
            value = random.randint(-100, 100)
            self.add(value)  # Додаємо елемент через метод add

    def display(self):
        """Показує елементи масиву"""
        return str(self.array[:self.size])  # Повертає тільки заповнені елементи
