class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  # Set Width & Height 

  def set_width(self, width):
    self.width = width
    
  def set_height(self, height):
    self.height = height

  # Get Area 
  def get_area(self):
    return self.width * self.height

  # Get Perimeter
  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  # Get Diagonal 
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
    
  # Get Picture 
  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    picture = ('*' * self.width + "\n") * self.height
    return picture
    
  # Get Amount Inside - how many times another shape provided can fit inside the original shape with no rotations.
  def get_amount_inside(self, shape):
    # m = self.width // shape.width
    # n = self.height // shape.height
    # return m * n 
    return self.get_area() // shape.get_area()

  # String Representation
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  # Store the length of the sides in both the width and height attributes from the Rectangle class. 
  def __init__(self, side):
    super().__init__(width=side, height=side)

  # Set Sides
  def set_side(self, side_length):
    self.width = side_length
    self.height = side_length

  # String Representation
  def __str__(self):
    return f"Square(side={self.width})"
    
    
