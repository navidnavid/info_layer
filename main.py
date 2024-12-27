import numpy as np
from exe_calc_info import info_layer_content

import math

def generate_sin_series(A = 100, start=0, end=2*math.pi, num_samples=10):
  arr=[]
  step_size = (end - start) / (num_samples - 1)
  x_values = [start + i * step_size for i in range(num_samples)]
  sin_values = [A*math.sin(x) for x in x_values]
  return sin_values



# Defining main function
def main():

    arr = generate_sin_series()
    signal = np.array(arr)
    info_layer_content_obj = info_layer_content(2)
    info_layer_content_obj.exe_devide_n_layer_info_content(signal)
    print( info_layer_content_obj.info_list)


# Using the special variable 
# __name__
if __name__=="__main__":
    main()