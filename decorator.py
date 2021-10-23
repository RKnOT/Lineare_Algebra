
from datetime import datetime
datetime.now().strftime('%Y-%m-%d %H:%M:%S')

import time
def dec_test(func):
    def wrapper(*args, **kwargs):
        
        dat_name = kwargs.get('filename')
        debugnr = kwargs.get('debug_nr')
        c_time = datetime.now().strftime('%H:%M:%S')
        print(c_time)
        with open(dat_name, 'a+') as f:
            f.write('--- time:  ' + c_time + ' debug nr : ' + debugnr + ' record start ----')
            f.write('\n')
            for item in list(*args):
                f.write(str(item))
                f.write('\n')
                #print(item, '\n')
            f.write('--- record end ----')
            f.write('\n')
        print('dec_test')
        return func
    return wrapper

@dec_test
def pr(*args, **kwargs):
    print('')
    #print(list(*args))

datum = datetime.now().strftime('%Y_%m_%d')


li = []
for i in range(0,10):
    li.append(i)
tu =tuple(li)
print(li)
print(tu)

debugnr = 1
pr(tu, filename = 'debug_'+ datum+'.txt', debug_nr = str(debugnr))    
time.sleep(2)
debugnr = 2
pr(('test', 'jjj','hhh', 'ghjkl'), filename = 'debug_'+ datum+'.txt', debug_nr = str(debugnr))    
time.sleep(3)
debugnr = 3
pr(('debug','test', 'jjj','hhh', 'ghjkl'), filename = 'debug_'+ datum+'.txt', debug_nr = str(debugnr))    


#-------------------
