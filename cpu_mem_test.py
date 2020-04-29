# -*- coding: UTF-8 -*-

import argparse
import psutil
from statistics import mean
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
# # 获取进程名位Python的进程对象列表
# process_lst = getProcess("firefox")
# # 获取内存利用率：
# print len(process_lst)
# for process_instance in process_lst:
#     print "----------------------mem------------------------------------\n"
#     print process_instance.memory_percent()
# # 获取cpu利用率：

#     print "---------------------cpu----------------------------------------\n"
# while True:
#     for process_instance in process_lst:
#         print process_instance.cpu_percent(interval=3)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('--process_name', nargs='+',help="process name,Support for multiple input processes")
    p.add_argument('--interval',default=0)
    args = p.parse_args()

    process_name_list = [] 
    process_name_pid_map = {}
    process_name_cpu_map = {}
    process_name_mem_map = {}

    print "process name:"
    for name in args.process_name:
        print name
        process_name_list.append(name)
    print "print process_name_list messages:"
    for name in process_name_list:
        print name
        process_name_pid_map[name] = getProcess(name)
        process_name_cpu_map[name] = []
        process_name_mem_map[name] = []
    i = 0
    while True :
        for name in process_name_list:
            for process_instance in process_name_pid_map[name]:
                #print name ,":--------mem------------"
                mem = process_instance.memory_percent()
               # print mem
                process_name_mem_map[name].append(mem)
               # print name ,":--------cpu------------"
                cpu =  process_instance.cpu_percent(interval=float(args.interval))
               # print cpu 
                process_name_cpu_map[name].append(cpu)
        for name in process_name_list:
            print name,"cpu_min(%):",min(process_name_cpu_map[name]),\
                " cpu _max(%):",max(process_name_cpu_map[name]),\
                    "  cpu_mean(%):",mean(process_name_cpu_map[name])
            print name,"mem_min(%):",min(process_name_mem_map[name]),\
                " mem _max(%):",max(process_name_mem_map[name]),\
                    "  mem_mean(%):",mean(process_name_mem_map[name])
            
          #  print(min(process_name_cpu_map[name]))
            #print name,"_max:",max(process_name_cpu_map[name])
           # print(max(process_name_cpu_map[name]))
           # print name,"_mean:",mean(process_name_cpu_map[name])
          #  print(mean(process_name_cpu_map[name]))


    
    


