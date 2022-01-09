
import os
import time
import json

# import datetime module
from datetime import datetime

# Получение значения Load Average из /proc
def get_la():
    loadavg_handler = open('/proc/loadavg', 'rt')
    # reading loadavg data    
    for line in loadavg_handler:
        line_lst = line.split()
        la_data = {'load_average': line_lst[0]+' '+line_lst[1]+' '+line_lst[2]}
        loadavg_handler.close()
        return la_data

# Получение установленного и свободного объёмов оперативной памяти 
def get_mem():
    mem_strings = 2
    mem_counter = 0
    mem_handler = open('/proc/meminfo', 'rt')
    stats = []

    while mem_counter < mem_strings:
        mem_counter = mem_counter + 1
        mem_lst = mem_handler.readline().split()
        stats.append(mem_lst[1])

    mem_total = stats[0]
    mem_free = stats[1]
 
    mem_data = {'mem_total': mem_total+' kb', 'mem_free': mem_free+' kb'}
    mem_handler.close()

    return mem_data

# Получение доступного дискового пространства и Inodes
def get_disk():
    df_output = os.popen('/usr/bin/df -h --output=source,ipcent,pcent | grep /dev/sd')
    disk_data = df_output.readline().split()
    
    return {'disk_name': disk_data[0], 'disk_space_used': disk_data[1], 'disk_inodes_used': disk_data[2]}


la = get_la()
mem = get_mem()
disk = get_disk()

timestamp = int(time.time())

metrics = {
    'timestamp': timestamp,
    'load_average': la['load_average'],
    'mem_total': mem['mem_total'],
    'mem_free': mem['mem_free'],
    'disk_name': disk['disk_name'],
    'disk_space_used': disk['disk_space_used'],
    'disk_inodes_used': disk['disk_inodes_used'],
}

#print(metrics)
dt_obj = datetime.fromtimestamp(timestamp).strftime('%d-%m-%y')


with open('/var/log/'+dt_obj+'_awesome_monitoring.json', 'a') as log_handler:
    json.dump(metrics, log_handler)
    log_handler.write("\n")

log_handler.close()

#f.close()
