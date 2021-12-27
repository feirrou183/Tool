#尝试通过打开一个测试文件来计算脚本运行耗时
#注意千万不要开启自己，会造成死机！！！！
import time
import os

path = 'test.py'  #要测试的当前文件夹文件名或文件绝对路径

def time_test(function):#计算文件用时函数
        def deco(path): 
                start_time = time.time()
                function(path)
                stop_time = time.time()
                print('该程序用时%f' %(stop_time-start_time))
                
        return deco 
	
	
@time_test	#time_test是open_py的装饰器  <==>  open_py = time_test(open_py)
def open_py(path):
	os.system(path)



open_py(path)




