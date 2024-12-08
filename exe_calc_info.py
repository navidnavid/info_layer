from clasify_num import clasify
from calc_info import info

class info_layer_content:
    #todo move inof list and ar list as class memebr , n become calss member, then make iteartio over  exe...
    def __init__(self, layer_num):
        self.info_list = []
        self.arr_list =[]
        self.loop=layer_num

    def calc_info_content(self, arr) ->float:
        info_obj = info()
        c_org_info = info_obj.info_content(arr) # cal max etp - etp 
        return c_org_info
    

    def populate_lits(self, arr_dvided_H_L):
        info_obj = info()
        clasify_obj =clasify()
        self.info_list.append(info_obj.info_content(arr_dvided_H_L[0]))
        self.info_list.append(info_obj.info_content(arr_dvided_H_L[1]))
        self.arr_list.append(clasify_obj.classify_numbers_by_dis(arr_dvided_H_L[0]))
        self.arr_list.append( clasify_obj.classify_numbers_by_dis(arr_dvided_H_L[1]))


    def exe_devide_n_layer_info_content(self, arr) ->list[float]:
    # print(c_org_info)
        # cal fo devided arr
        info_obj = info()
        clasify_obj =clasify()
        
        self.info_list.append(f'layer: {0} ')
        self.info_list.append(self.calc_info_content(arr))
        arr_dvided_H_L_inti = clasify_obj.classify_numbers_by_dis(arr)
        
        for i in range(self.loop):
            if(len(self.arr_list) == 0):
                print(f"info-----> in init if .arr_list size is {len(self.arr_list)}")
                self.info_list.append(f'layer: {1} ')
                self.populate_lits(arr_dvided_H_L_inti)
            else:
                print(f"info-----> in loop .arr_list size is {len(self.arr_list)}")
                items=self.arr_list
                self.arr_list = []
                self.info_list.append(f'layer: {i+1} ')
                for item in items:
                    self.populate_lits(item)
                    
            





