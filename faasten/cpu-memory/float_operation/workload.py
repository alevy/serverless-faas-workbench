import math
from time import time


def float_operations(n):
    start = time()
    for i in range(0, n):
        sin_i = math.sin(i)
        cos_i = math.cos(i)
        sqrt_i = math.sqrt(i)
    latency = time() - start
    return latency


def main(event):
    latencies = {}
    timestamps = {}
    timestamps["starting_time"] = time()
    n = int(event['n'])
    metadata = event['metadata']
    latency = float_operations(n)
    latencies["function_execution"] = latency
    timestamps["finishing_time"] = time()
    ret = sc.fs_createfile(":~:test", (123).to_bytes(4, 'big'))
    ret = sc.fs_write(":~:test", (123).to_bytes(4, 'big'))
    files = sc.fs_list(":~").names
    return {"ret": ret, "file": list(files), "latencies": latencies, "timestamps": timestamps, "metadata": metadata}

def handle(args, syscall):
    global sc
    sc = syscall
    return main(args)

if __name__ == "__main__":
    print(main({'n': 100, 'metadata': 1}))