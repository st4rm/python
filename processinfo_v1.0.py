import psutil

#define variables
process_name="cherrytree"


b_proc=0
for proc in psutil.process_iter(['pid','name']):
    if process_name in proc.info['name']:
        pid=proc.info['pid']
        print(pid)
        b_proc=1
if(b_proc == 0):
    print(process_name,'is not running')
