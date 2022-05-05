# -*- coding: utf-8 -*-
'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "

中间部分作答，作答行数自由调整


题目
将两个升序列表合并为一个新的升序列表并返回。

示例：
输入：lst_1 = [1,2,4], lst_2 = [1,3,4]
输出：[1,1,2,3,4,4]

输入：lst_1 = [], lst_2 = [0]
输出：[0]

'''

def TEST_DO_NOT_CHANGE( lst_1, lst_2):
    print(lst_1, lst_2)
    lst_rlt = None
    ##########start下面可以改动
    lst_1.extend(lst_2)
    lst_a = lst_1
    if lst_a == []:
        lst_rlt = lst_a    
    else:
        lst_a.sort()
        lst_rlt = lst_a


    ##########end 上面可以改动 "
    return lst_rlt

if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE( [1,2,4],[1,3,4]))
    print(TEST_DO_NOT_CHANGE([],[]))
    print(TEST_DO_NOT_CHANGE([],[0]))
