# ADVANCED ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

"""
CUBE CLASS

1. CREATE an abstract class "Cube" with the functions:
   translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
   All functions store and print out the data in the cube (translate, rotate, scale and color).

2. ADD an __init__(name) and create 3 cube objects.

3. ADD the function print_status() which prints all the variables nicely formatted.

4. ADD the function update_transform(ttype, value).
   "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats.
   This function should trigger either the translate, rotate or scale function.

   BONUS: Can you do it without using ifs?

5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
   Use Object as the parent for your Cube class.
   Update the Cube class to not repeat the content of Object.

"""
# ***********************************************************************
# CLASS

# Master class
class Object():
    def __init__(self, name, translate, rotate, scale):
        self.name = name
        self.translate = translate
        self.rotate = rotate
        self.scale = scale

# Subclass
class Cube(Object):
    def __init__(self, name, translate, rotate, scale, color):
        super().__init__(name, translate, rotate, scale)
        self.color = color
      
    def cube_translate(self):
       translate_value = self.translate
       return translate_value
   
    def cube_rotate(self):
       rotate_value = self.rotate
       return rotate_value
   
    def cube_scale(self):
       scale_value = self.scale
       return scale_value
   
    def cube_color(self):
       color_value = self.color
       return color_value
   
    def print_status(self):
       print(f"name      : {self.name}")
       print(f"translate : {self.translate}")
       print(f"rotate    : {self.rotate}")
       print(f"scale     : {self.scale}")
       print(f"color     : {self.color}")
    
    def update_transform(self, ttype, value):
        setattr(self, ttype, value)


# ***********************************************************************
# TESTS

test = Cube(name = "cube01", translate = [0,0,0], rotate = [1,1,1], scale = [2,2,2], color = [3,3,3])
test.cube_translate()
test.cube_rotate()
test.cube_scale()
test.cube_color()
test.print_status()
test.update_transform("name" , "booyah")
test.update_transform("color" , [255,255,255])
test.print_status()