#Class For the rectangle
class Rectangle:
  width = 0
  height = 0
  area = 0
  perimeter = 0
  diagonal = 0
  picture = None
  
  #Init 
  def __init__(self, width, height):
    self.width = width
    self.height = height

  #Get area
  def get_area(self):
    self.area = self.width * self.height
    return self.area

  #change width or height
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  #Get perimeter
  def get_perimeter(self):
    self.perimeter = 2 * self.width + 2 * self.height
    return self.perimeter

  #Get diagonal
  def get_diagonal(self):
    self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return self.diagonal

  #Get "picture" of the polygon
  def get_picture(self):
    Iteration = 0
    lines = []
    line = '*' * self.width

    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      #Loop to append a list for width length
      while(self.height > Iteration):
        lines.append(line)
        Iteration = Iteration + 1 
  
      #Join the list in a string
      self.picture = '\n'.join(lines) + '\n'
      return self.picture

  #Function to get how many figures fit in our figure
  def get_amount_inside(self,figure):
    self_area = self.get_area()
    other_area = figure.get_area()

    return int(self_area/other_area)

  #String to return when printing the object
  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    
#Class For the square
class Square(Rectangle):

  #Init
  def __init__(self, width):
    self.width = width
    self.height = width
    print(self.height)

  #Functin to set side on square
  def set_side(self,side):
    self.width = side
    self.height = side

  #Rewrite functions
  def set_width(self, width):
    self.set_side(width)

  def set_height(self, height):
    self.set_side(height)

  #String to return when printing the object
  def __str__(self):
    return "Square(side=" + str(self.width) + ")" 