# -*- coding: UTF-8 -*-


import psutil
process_lst = []
def getProcess(pName):
    # 获取当前系统所有进程id列表
    all_pids  = psutil.pids()

    # 遍历所有进程，名称匹配的加入process_lst
    for pid in all_pids:
        p = psutil.Process(pid)
    # print p.name()
        if (p.name() == pName):
            process_lst.append(p)
    return process_lst
# 获取进程名位Python的进程对象列表
process_lst = getProcess("firefox")
# 获取内存利用率：
print len(process_lst)
for process_instance in process_lst:
    print "----------------------mem------------------------------------\n"
    print process_instance.memory_percent()
# 获取cpu利用率：

    print "---------------------cpu----------------------------------------\n"
while True:
    for process_instance in process_lst:
        print process_instance.cpu_percent(interval=3)
