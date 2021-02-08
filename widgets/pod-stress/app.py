from flask import Flask, request
from subprocess import Popen

app = Flask(__name__)

CPU_WORKERS = 0
MEM_WORKERS = 0
STRESS_P = None

@app.route("/")
def home():
    return "cpu_workers: %d, mem_workers: %d Mi" % (CPU_WORKERS, MEM_WORKERS)

def run_stress(cpu_workers=None, mem_workers=None):
    global CPU_WORKERS
    global MEM_WORKERS
    global STRESS_P

    if STRESS_P:
        killall = Popen(['/usr/bin/killall', '/usr/bin/stress'])
        out, err = killall.communicate()
        killall.terminate()
        STRESS_P = None

    # update global values if input is a real number.
    if cpu_workers != None and cpu_workers >= 0:
        CPU_WORKERS = cpu_workers
    if mem_workers != None and mem_workers >= 0:
        MEM_WORKERS = mem_workers

    # assemble the stress command and only execute if we have something to do.
    stress_cmd = ['/usr/bin/stress']
    if CPU_WORKERS > 0:
        stress_cmd += ['-c', str(CPU_WORKERS)]
    if MEM_WORKERS > 0:
        stress_cmd += ['-m', str(MEM_WORKERS)]
    if len(stress_cmd) > 1:
        STRESS_P = Popen(stress_cmd)
        return stress_cmd

    return "Nothing to run"

@app.route("/cpu_workers", methods=["POST"])
def set_cpu_workers():
    new_cpu_workers = int(request.args.get("value", 0))
    stress_cmd = run_stress(cpu_workers=new_cpu_workers)
    return "ok: %s" % stress_cmd

@app.route("/mem_workers", methods=["POST"])
def set_mem_workers():
    new_mem_workers = int(request.args.get("value", 0))
    stress_cmd = run_stress(mem_workers=new_mem_workers)
    return "ok: %s" % stress_cmd

@app.route("/livez")
def liveness():
    return "ok"

@app.route("/readyz")
def readiness():
    return "ok"