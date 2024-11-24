import numpy as np
from exe_calc_info import exe_calss_info_deff

# Defining main function
def main():
    arr = [1,2,3,4,5,6,7,8,9,11,12]
    signal = np.array(arr)
    info_diff_org_vs_divided_org = exe_calss_info_deff(signal)


# Using the special variable 
# __name__
if __name__=="__main__":
    main()