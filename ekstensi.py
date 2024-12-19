# Hasby Ashidiq
# F55123010

import random
import time
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan array dengan n elemen
def generate_array(n, max_value):
    random.seed(0)
    return [random.randint(1, max_value) for _ in range(n)]

# Fungsi untuk memeriksa apakah elemen dalam array bersifat unik
def is_unique(arr):
    return len(arr) == len(set(arr))

# Fungsi untuk menghitung worst case dan average case
def calculate_cases(n_values, max_value):
    worst_cases = []
    average_cases = []

    for n in n_values:
        times = []
        for _ in range(10):
            arr = generate_array(n, max_value)
            start_time = time.time()
            is_unique(arr)
            end_time = time.time()
            times.append(end_time - start_time)
        
        worst_cases.append(max(times))
        average_cases.append(sum(times) / len(times))
    
    return worst_cases, average_cases

# Fungsi untuk menggambar grafik
def plot_graph(n_values, worst_cases, average_cases):
    plt.plot(n_values, worst_cases, label='Worst Case')
    plt.plot(n_values, average_cases, label='Average Case')
    plt.xlabel('Jumlah elemen (n)')
    plt.ylabel('Waktu (Seconds)')
    plt.title('Worst Case dan Average Case Time Complexity')
    plt.legend()
    plt.savefig('worst_avg_plot.jpg')
    plt.show()

# Eksekusi utama
n_values = [100, 150, 200, 250, 300, 350, 400, 500]
max_value = 240  # 250 - 010 (stambuk saya)

worst_cases, average_cases = calculate_cases(n_values, max_value)

# Simpan hasilnya ke file
with open('worst_avg.txt', 'w') as f:
    f.write('n_values: ' + str(n_values) + '\n')
    f.write('worst_cases: ' + str(worst_cases) + '\n')
    f.write('average_cases: ' + str(average_cases) + '\n')

# Gambar grafik
plot_graph(n_values, worst_cases, average_cases)