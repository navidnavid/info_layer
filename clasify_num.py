def classify_numbers_by_dis(numbers):
  """
  Classifies a set of numbers into two classes based on their proximity to the mean.

  Args:
    numbers: A list of numbers.

  Returns:
    A list of tuples, where each tuple contains a number and its assigned class (0 or 1).
  """

  mean = sum(numbers) / len(numbers)
  classes = [(num, 1) if num >= mean else (num, 0) for num in numbers]
  return classes

