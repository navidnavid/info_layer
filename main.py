import numpy as np
from exe_calc_info import info_layer_content

# Defining main function
def main():
    arr = [1,2,3,4,5,6,7,8,9,11,12, 1,-2,-3,-4,5,6,7,-8,-9,11,-12]
    signal = np.array(arr)
    info_layer_content_obj = info_layer_content(3)
    info_layer_content_obj.exe_devide_n_layer_info_content(signal)
    print( info_layer_content_obj.info_list)


# Using the special variable 
# __name__
if __name__=="__main__":
    main()