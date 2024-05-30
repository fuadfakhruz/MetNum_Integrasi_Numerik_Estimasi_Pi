import numpy as np
import time
import math
from scipy.integrate import simps

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Metode 1: Integrasi Reimann
def reimann_integration(N):
    dx = 1.0 / N
    x = np.linspace(0, 1, N, endpoint=False)
    integral = np.sum(f(x)) * dx
    return integral

# Metode 2: Integrasi Trapezoid
def trapezoid_integration(N):
    x = np.linspace(0, 1, N+1)
    y = f(x)
    integral = np.trapz(y, x)
    return integral

# Metode 3: Integrasi Simpson 1/3
def simpson_integration(N):
    x = np.linspace(0, 1, N+1)
    y = f(x)
    integral = simps(y, x)
    return integral

# Fungsi untuk menghitung galat RMS
def calculate_rms_error(estimate, reference):
    return np.sqrt((estimate - reference)**2)

# Nilai referensi pi
pi_reference = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

def main():
    # Input NIM
    nim = input("Masukkan NIM Anda: ")
    if len(nim) < 2:
        print("NIM harus terdiri dari minimal dua digit.")
        return
    
    last_two_digits = int(nim[-2:])
    method = last_two_digits % 3

    if method == 0:
        method_name = "Reimann"
        integration_method = reimann_integration
    elif method == 1:
        method_name = "Trapezoid"
        integration_method = trapezoid_integration
    else:
        method_name = "Simpson"
        integration_method = simpson_integration

    print(f"Metode yang digunakan: {method_name}")
    
    # Pengujian dan pengukuran waktu eksekusi
    results = {
        'N': [],
        'Result': [],
        'Error': [],
        'Time': []
    }

    for N in N_values:
        results['N'].append(N)
        
        start_time = time.time()
        result = integration_method(N)
        exec_time = time.time() - start_time
        error = calculate_rms_error(result, pi_reference)
        
        results['Result'].append(result)
        results['Error'].append(error)
        results['Time'].append(exec_time)

    # Menampilkan hasil
    for i in range(len(N_values)):
        print(f"N = {N_values[i]}")
        print(f"Result = {results['Result'][i]}, Error = {results['Error'][i]}, Time = {results['Time'][i]}")
        print()

if __name__ == "__main__":
    main()
