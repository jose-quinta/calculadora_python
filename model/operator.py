from Classmethods import classmethods

@classmethod
class Operator():
  first_number:int = int
  second_number:int = int
  operator:str = str
  result:float = float

  def __init__(self):
    first_number:float = float
    second_number:float = float
    operator:str = str
    result:float = float

  def get_first_number(self, first_number:float):
    self.first_number = first_number

  def set_first_number(self):
    return self.first_number

  def get_second_number(self, second_number:float):
    self.second_number = second_number

  def set_second_number(self):
    return self.second_number

  def get_operator(self, operator:str):
    self.operator = operator

  def set_operator(self):
    return self.operator

  def get_result(self, result:float):
    self.result = result

  def set_result(self):
    return self.result

  def sum_numbers(self):
    sum_result = self.first_number + self.second_number
    self.set_result(sum_result)
    return sum_result

  def subtract_numbers(self):
    subtract_result = self.first_number - self.second_number
    self.set_result(subtract_result)
    return subtract_result

  def multiply_numbers(self):
    multiply_result = self.first_number * self.second_number
    self.set_result(multiply_result)
    return multiply_result

  def split_numbers(self):
    split_result = self.first_number / self.second_number
    self.set_result(split_result)
    return split_result