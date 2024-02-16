# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# animal_1 = Animal("Dog", 10)
# animal_2 = Animal("Cat", 10)

# # animal_1.name = "Dog"
# # animal_2.name = "Cat"

# # animal_1.age = 10
# # animal_2.age = 10

# a_list = [animal_1, animal_2]

# for i in range(0,2):
#     print(str(a_list[i].name)+":"+str(a_list[i].age)+" yo")

def p_rect(rect):
    print(f'Altura: {rect.height}')
    print(f'Largura: {rect.width}')
    print(f'Area = {rect.area}')

class Retangulo:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.area = width * height
        self.perimeter = width * 2 + height * 2
        
    def delta_area(self, rect_outro):
        area = self.area
        area_outro  = rect_outro.area
        delta = abs(area - area_outro)
        return delta


rect1 = Retangulo(5, 10)
rect2 = Retangulo(3, 7)


print(f'Diferença de área = {rect1.delta_area(rect2)}')