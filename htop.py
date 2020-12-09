import psutil

CORE_LOAD_TEMPLATE = "core {0} -> {1}%\n\t"

TEMPLATES = {
    "cpu": {
        "loads": "CPU load: \n\t{}",
        "times": "Time of work -> \n\tsystem - {system} s\n\tuser - {user} s\n\t"
    }
}

def get_cpu():
    times = psutil.cpu_times(percpu=False)
    load = psutil.cpu_percent(interval=1, percpu=True)
    res = {
        "times": {"user": times.user, "system": times.system},
        "load": {"values": load}
    }
    return res
def show():
    cpu = get_cpu()
    template_load = ""
    for i, value in enumerate(cpu["load"]["values"]):
        template_load += CORE_LOAD_TEMPLATE.format(i, value)
    cpu_load_info = TEMPLATES["cpu"]["loads"].format(
        template_load
    )
    print(cpu_load_info)
    cpu_work_info = TEMPLATES["cpu"]["times"].format(**cpu["times"])
    print(cpu_work_info)


if __name__ == "__main__":
    show()

TEMPLATES1 = {
    "mem": "Virtual memory -> \n\ttotals memory - {total_memory} bytes\n\tavailable memory - {available_memory} bytes\n\tpercent - {percent}%\n\t"
    }

def get_mem():
    memo = psutil.virtual_memory()
    res1 = {'total_memory': memo.total, 'available_memory': memo.available, 'percent': memo.percent}
    return res1

def show():
    mem = get_mem()
    mem_info = TEMPLATES1["mem"].format(**mem)
    print(mem_info)

if __name__ == "__main__":
    show()

TEMPLATES2 = {
    "pros": "Process -> \n\tprocess pid - {pid}\n\tprocess name - {name}\n\tprocess status - {status}\n\tusername - {username}\n\tcpu - {cpucount}\n\tuser cpu - {cpu} s\n\t"
    }

def get_proc():
    proc = psutil.Process()
    res2 = {'pid': proc.pid, 'name': proc.name(), 'status': proc.status(), 'username': proc.username(), 'cpucount': proc.cpu_num(), 'cpu': proc.cpu_times().user}
    return res2

def show():
    pross = get_proc()
    proc_info = TEMPLATES2["pros"].format(**pross)
    print(proc_info)

if __name__ == "__main__":
    show()    
    
TEMPLATE3 = {'batter': 'Device battery ->\n\tbattery percent - {bat_perc:.3}%\n\t'}

def get_bat():
    batter=psutil.sensors_battery()
    res4={'bat_perc': batter.percent}
    return res4

def show():
    perc = get_bat()
    bat_info = TEMPLATE3['batter'].format(**perc)
    print(bat_info)

if __name__ == "__main__":
    show()    