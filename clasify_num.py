import numpy as np


class clasify:
    def classify_numbers_by_dis(self,numbers):
        """
        Classifies a set of numbers into two classes based on their proximity to the mean.
        Args:
            numbers: A list of numbers.
        Returns:
            A list of tuples, where each tuple contains a number and its assigned class (0 or 1).
        """
        mean = sum(numbers) / len(numbers)

        classesH =[]
        classesL =[]
        for num in numbers:
            if num >= mean:
                classesH.append(num)
            else:
                classesL.append(num)
        return (np.array(classesH), np.array(classesL))

