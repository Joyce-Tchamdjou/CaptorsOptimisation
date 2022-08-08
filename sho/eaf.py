import csv, os
import numpy as np
import matplotlib.pyplot as plt

def val_for_run(solver):
    cmd = "python snp_run.py -m " + solver
    fichier_csv = solver + ".csv"
    val = []
    os.system(cmd)
    with open(fichier_csv, 'r') as f:
        myReader = csv.reader(f, delimiter = ';')
        linecount = 0
        for row in myReader:
            if (linecount != 0):
                val.append(float(row[1]))
            linecount +=1
    return val, linecount

def prepa_eaf(solver, run):
    vals = []
    vals_lim = []
    timer = []
    for i in range(run):
        val, lcount = val_for_run(solver)
        vals_lim.append(np.amin(val))
        vals_lim.append(np.amax(val))
        timer.append(lcount-1)
        vals.append(val)
        scale = np.arange(lcount-1)
        plt.plot(scale, val)
    plt.title("EAF")
    plt.show()
    return np.amin(vals_lim), np.amax(vals_lim), np.amax(timer), vals

def eaf(solver, run):
    seuil_min, seuil_max, time_max, vals = prepa_eaf(solver, run)
    scale = np.arange(time_max)
    for i in range(run):
        time = len(vals[i])
        if (time < time_max):
            for j in range(time, time_max, 1):
                vals[i].append(vals[i][time-1])
    for seuil in range(int(seuil_min), int(seuil_max)-10, 50):
        prob = []
        for j in range(time_max):
            nb = 0
            for k in range(run):
                if(vals[k][j] > seuil):
                    nb += 1
            prob.append(nb/run)
        plt.plot(scale, prob)
    plt.title("ECDF")
    plt.show()



eaf("num_simulated_annealing", 10)







