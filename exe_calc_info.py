from clasify_num import clasify
from calc_info import info

def exe_calss_info_deff(arr):
    info_obj = info()
    c_org_info = info_obj.info_content(arr)
   # print(c_org_info)
    # cal fo devided arr
    clasify_obj =clasify()
    class_H_L= clasify_obj.classify_numbers_by_dis(arr)
    c1_info = info_obj.info_content(class_H_L[0])
    c2_info = info_obj.info_content(class_H_L[1])
    return ((c_org_info,c1_info,c2_info))