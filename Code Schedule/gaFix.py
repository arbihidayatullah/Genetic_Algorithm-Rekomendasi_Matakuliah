import streamlit as st
import random
import matplotlib.pyplot as plt

# Data Matakuliah
matakuliah = {
    1: {"Kode": "MII225201", "Nama": "Analisis Algoritme","Dosen":"1. Drs. Suprapto, M.I.Kom.\n2. Dr. Nur Rokhman, S.Si., M.Kom.", "hari": 2, "jam": 2},
    2: {"Kode": "MII225202", "Nama": "Matematika untuk Ilmu Komputer","Dosen":"1. Prof. Dr.-Ing. Mhd. Reza M. I. Pulungan, S.Si., M.Sc.\n2. Drs. Sri Mulyana, M.Kom.", "hari": 4, "jam": 3},
    3: {"Kode": "MII226001", "Nama": "Metodologi Riset Ilmu Komputer","Dosen":"1. Dr. Dyah Aruming Tyas, S.Si.\n2. Aina Musdholifah, S.Kom., M.Kom., Ph.D." ,"hari": 5, "jam": 3},
    4: {"Kode": "MII225201", "Nama": "Pengolahan dan Analisis Citra Digital","Dosen":"1. Moh. Edi Wibowo, S.Kom., M.Kom., Ph.D.\n2. Dr.techn. Aufaclav Zatu Kusuma Frisky S.Si., M.Sc." ,"hari": 4, "jam": 3},
    5: {"Kode": "MII226502", "Nama": "Sistem Temu Balik Informasi","Dosen":"1. Yunita Sari, S.Kom., M.Sc., Ph.D." ,"hari": 4, "jam": 1},
    6: {"Kode": "MII226503", "Nama": "Data Warehouse dan Inteligensi Bisnis","Dosen":"1. Drs. Edi Winarko, M.Sc.,Ph.D." ,"hari": 2, "jam": 1},
    7: {"Kode": "MII226504", "Nama": "Pengembangan Perangkat Lunak","Dosen":"1. Dr. Lukman Heryawan, S.T., M.T." ,"hari": 3, "jam": 3},
    8: {"Kode": "MII226505", "Nama": "Kecerdasan Digital dan Informatika Sosial","Dosen":"1. Prof. Dr. Tri Kuntoro Priyambodo, M.Sc.\n2. Faizal Makhrus, S.Kom., M.Sc., Ph.D." ,"hari": 1, "jam": 3},
    9: {"Kode": "MII226506", "Nama": "Manajemen dan Audit Sistem Informasi", "Dosen":"1. Dr. Mardhani Riasetiawan, SE Ak, M.T.","hari": 1, "jam": 3},
    10: {"Kode": "MII226203", "Nama": "Teori Komputasi","Dosen":"1. Moh. Edi Wibowo, S.Kom., M.Kom., Ph.D.\n2. Faizal Makhrus, S.Kom., M.Sc., Ph.D." ,"hari": 4, "jam": 2},
    11: {"Kode": "MII226401", "Nama": "Kecerdasan Komputasional dan Pembelajaran Mesin","Dosen":"1. Aina Musdholifah, S.Kom., M.Kom., Ph.D.\n2. Dr. Dyah Aruming Tyas, S.Si." ,"hari": 2, "jam": 3},
    12: {"Kode": "MII226402", "Nama": "Prinsip Kecerdasan Artifisial","Dosen":"1. Prof. Dra. Sri Hartati, M.Sc., Ph.D.\n2. Afiahayati, S.Kom., M.Cs., Ph.D" ,"hari": 3, "jam": 1},
    13: {"Kode": "MII226402", "Nama": "Rekayasa Fitur dan Pengenalan Pola","Dosen":"1. Wahyono, S.Kom., Ph.D." ,"hari": 2, "jam": 2},
    14: {"Kode": "MII226404", "Nama": "Sistem Pendukung Pembuatan Keputusan","Dosen":"1. Prof. Drs. Retantyo Wardoyo, M.Sc., Ph.D." ,"hari": 4, "jam": 2},
    15: {"Kode": "MII226501", "Nama": "Data Science","Dosen":"1. Dr. Sigit Priyanta, S.Si., M.Kom.\n2. Arif Nurwidyantoro, S.Kom., M.Cs., Ph.D." , "hari": 3, "jam": 2},
    16: {"Kode": "MII226601", "Nama": "Komputasi Awan dan Keamanan Siber","Dosen":"1. Prof. Dr.techn. Ahmad Ashari, M.I.Kom.\n2. Prof. Dr. Ir. Jazi Eko Istiyanto, M.Sc." , "hari": 2, "jam": 3},
    17: {"Kode": "MII226602", "Nama": "Jaringan Komputer Lanjut","Dosen":"1. Muhammad Alfian Amrizal, B.Eng., M.I.S., Ph.D.\n2. Drs. Yohanes Suyanto, M.I.Kom." , "hari": 3, "jam": 2},
    18: {"Kode": "MII226603", "Nama": "Platform dan Arsitektur Big Data","Dosen":"1. Dr. techn. Khabib Mustofa, S.Si., M.Kom.\n2. Muhammad Alfian Amrizal, B.Eng., M.I.S., Ph.D." , "hari": 2, "jam": 2},
}

# Kode Ruang
kode_ruang = {419: 1, 420: 2, 421: 3, 422: 4}

# Parameter Algoritma Genetika
POPULATION_SIZE = 10
MAX_GENERATIONS = 100
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
NUM_MATKUL = 6

# Fungsi untuk menghitung nilai fitness
def calculate_fitness(individual):
    # Hitung penalti untuk setiap individu
    penalty = 0
    hari_jam_pairs = set([(matakuliah[matkul]["hari"], matakuliah[matkul]["jam"]) for matkul in individual])
    for hari, jam in hari_jam_pairs:
        count_matkul_hari_jam = sum(1 for matkul in individual if matakuliah[matkul]["hari"] == hari and matakuliah[matkul]["jam"] == jam)
        if count_matkul_hari_jam > 1:  # Soft Constraint: Mahasiswa mengikuti maksimal 1 mata kuliah dalam 1 hari dan jam yang sama
            penalty += count_matkul_hari_jam - 1
    
    for sesi in set([matakuliah[matkul]["jam"] for matkul in individual]):
        if sesi:
            count_dosen_sesi = sum(1 for matkul in individual if matakuliah[matkul]["jam"] == jam)
            if count_dosen_sesi > 2:  # Soft Constraint: Dosen mengajar 2 Matakuliah dalam 1 sesi
                penalty += count_dosen_sesi - 2
    
    # Hitung fitness
    fitness = 1 / (1 + penalty)
    return fitness

# Fungsi untuk menghasilkan populasi awal
def generate_initial_population():
    population = []
    for _ in range(POPULATION_SIZE):
        individual = random.sample(list(matakuliah.keys()), NUM_MATKUL)
        population.append(individual)
    return population

# Fungsi seleksi menggunakan metode roulette wheel
def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    r = random.uniform(0, total_fitness)
    cumulative_fitness = 0
    for i, fitness in enumerate(fitness_values):
        cumulative_fitness += fitness
        if cumulative_fitness >= r:
            return population[i]

# Fungsi crossover menggunakan 1-point crossover
def one_point_crossover(parent1, parent2):
    # crossover_point = random.randint(1, len(parent1) - 1)
    # crossover_point = randint(1, len(parent1) - 1)
    child1 = parent1[:1] + parent2[1:]
    child2 = parent2[:1] + parent1[1:]
    # child1= parent
    return child1, child2

# Fungsi mutasi menggunakan pemilihan nilai acak
def mutate(individual):
    if random.random() < MUTATION_RATE:
        # Pilih dua matakuliah secara acak untuk ditukar
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# Algoritma Genetika
def genetic_algorithm():
    # Inisialisasi populasi awal
    population = generate_initial_population()
    fitness_history = []

    for generation in range(MAX_GENERATIONS):
        # Menghitung fitness untuk setiap individu dalam populasi
        fitness_values = [calculate_fitness(individual) for individual in population]

        # Memilih individu untuk reproduksi (seleksi)
        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1 = roulette_wheel_selection(population, fitness_values)
            parent2 = roulette_wheel_selection(population, fitness_values)
            child1, child2 = one_point_crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population

        # Mengambil individu dengan nilai fitness tertinggi pada setiap generasi
        best_individual = max(population, key=calculate_fitness)
        best_fitness = calculate_fitness(best_individual)

    return best_individual, best_fitness

if __name__ == "__main__":
    st.title("Penjadwalan Mata Kuliah Menggunakan Algoritma Genetika")

    # Menampilkan data matakuliah
    st.subheader("Data Matakuliah")
    st.table(matakuliah)

    # Menampilkan data kode ruang
    st.subheader("Data Kode Ruang")
    st.table(kode_ruang)

    # Menambahkan tombol untuk memulai proses algoritma genetika
    if st.button("Proses Penjadwalan"):
        # Panggil algoritma genetika di sini dan tampilkan hasilnya
        best_solution, best_fitness = genetic_algorithm()
        st.subheader("Jadwal Optimal")
        jadwal_optimal = []
        for matkul in best_solution:
            jadwal_optimal.append({
                "Kode Matakuliah": matakuliah[matkul]["Kode"],
                "Matakuliah": matakuliah[matkul]["Nama"],
                "Dosen": matakuliah[matkul]["Dosen"],
                "Hari": matakuliah[matkul]["hari"],
                "Jam": matakuliah[matkul]["jam"],
                "Ruang": kode_ruang[random.choice(list(kode_ruang.keys()))]
            })
        st.table(jadwal_optimal)
        st.write("Fitness Terbaik:", best_fitness)
