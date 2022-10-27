class CustomArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = []

    def add_element(self, element):
        """
        Adds element to the array if its size is not reached.
        """

        if self.capacity > len(self.array):
            self.array += [element]

        else:
            print('Array is full!')

    def del_element(self, index):
        """
        Removes an element from the array if its size is not reached.
        """

        self.array = self.array[:index] + self.array[index+1:]

    def get_array_data(self):
        """
        Gets an array with data.
        """

        return self.array

    def insert_element(self, index, element):
        """
        Adds an element to the array at a specific position.
        """

        if self.capacity > len(self.array):
            self.array = self.array[:index] + [element] + self.array[index:]

        else:
            print('Array is full!')


if __name__ == '__main__':

    array = CustomArray(3)

    array.add_element(1)
    array.add_element(2)
    array.add_element(1)
    array.add_element(1)

    print(array.get_array_data())

    array.del_element(1)
    print(array.get_array_data())

    array.insert_element(2, 15)
    print(array.get_array_data())

    array.add_element(22)
    print(array.get_array_data())
