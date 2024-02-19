class Animal:
    def __init__(self, name, age, width, height):
        self.__name = name
        self.__age = age
        self.__width = width
        self.__height = height

    # Métodos de acesso (getters e setters)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise TypeError("Nome do animal deve ser uma string.")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and new_age >= 0:
            self.__age = new_age
        else:
            raise ValueError("Idade do animal deve ser um número inteiro positivo.")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if isinstance(new_width, float) and new_width >= 0:
            self.__width = new_width
        else:
            raise ValueError("Largura do animal deve ser um número real positivo.")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if isinstance(new_height, float) and new_height >= 0:
            self.__height = new_height
        else:
            raise ValueError("Altura do animal deve ser um número real positivo.")

    # Métodos adicionais

    def __str__(self):
        return f"Animal: {self.name}, Idade: {self.age}, " \
               f"Largura: {self.width}, Altura: {self.height}"