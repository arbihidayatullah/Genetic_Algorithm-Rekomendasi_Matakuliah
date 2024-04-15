import streamlit as st
import random

# Data Matakuliah
matakuliah_mkom = {
    1: {"Kode": "MII225201", "Nama": "Pengolahan dan Analisis Citra Digital","Dosen":"1. Moh. Edi Wibowo, S.Kom., M.Kom., Ph.D.\n\n2. Dr.techn. Aufaclav Zatu Kusuma Frisky S.Si., M.Sc." ,"hari": 4, "jam": 3},
    2: {"Kode": "MII226502", "Nama": "Sistem Temu Balik Informasi","Dosen":"1. Yunita Sari, S.Kom., M.Sc., Ph.D." ,"hari": 4, "jam": 1},
    3: {"Kode": "MII226503", "Nama": "Data Warehouse dan Inteligensi Bisnis","Dosen":"1. Drs. Edi Winarko, M.Sc.,Ph.D." ,"hari": 2, "jam": 1},
    4: {"Kode": "MII226505", "Nama": "Kecerdasan Digital dan Informatika Sosial","Dosen":"1. Prof. Dr. Tri Kuntoro Priyambodo, M.Sc.\n\n2. Faizal Makhrus, S.Kom., M.Sc., Ph.D." ,"hari": 1, "jam": 3},
    5: {"Kode": "MII226506", "Nama": "Manajemen dan Audit Sistem Informasi", "Dosen":"1. Dr. Mardhani Riasetiawan, SE Ak, M.T.","hari": 1, "jam": 3},
    6: {"Kode": "MII226402", "Nama": "Prinsip Kecerdasan Artifisial","Dosen":"1. Prof. Dra. Sri Hartati, M.Sc., Ph.D.\n\n2. Afiahayati, S.Kom., M.Cs., Ph.D" ,"hari": 3, "jam": 1},
    7: {"Kode": "MII226402", "Nama": "Rekayasa Fitur dan Pengenalan Pola","Dosen":"1. Wahyono, S.Kom., Ph.D." ,"hari": 2, "jam": 2},
    8: {"Kode": "MII226603", "Nama": "Platform dan Arsitektur Big Data","Dosen":"1. Dr. techn. Khabib Mustofa, S.Si., M.Kom.\n\n2. Muhammad Alfian Amrizal, B.Eng., M.I.S., Ph.D." , "hari": 2, "jam": 2},
    9: {
        "Kode": "MII226401", 
        "Nama": "Kecerdasan Komputasional dan Pembelajaran Mesin",
        "Dosen": "1. Aina Musdholifah, S.Kom., M.Kom., Ph.D.\n\n2. Dr. Dyah Aruming Tyas, S.Si.",
        "hari": 2, 
        "jam": 3
    },
    10: {
        "Kode": "MII226601", 
        "Nama": "Komputasi Awan dan Keamanan Siber",
        "Dosen": "1. Prof. Dr.techn. Ahmad Ashari, M.I.Kom.\n\n2. Prof. Dr. Ir. Jazi Eko Istiyanto, M.Sc.",
        "hari": 2, 
        "jam": 3
    },
    11: {
        "Kode": "MII226404",
        "Nama": "Sistem Pendukung Pembuatan Keputusan",
        "Dosen": "1. Prof. Drs. Retantyo Wardoyo, M.Sc., Ph.D.",
        "hari": 4,
        "jam": 2
    },
}

matakuliah_wajib = {
    11: {"Kode": "MII225201", "Nama": "Analisis Algoritme","Dosen":"1. Drs. Suprapto, M.I.Kom.\n\n2. Dr. Nur Rokhman, S.Si., M.Kom.", "hari": 2, "jam": 2},
    12: {"Kode": "MII225202", "Nama": "Matematika untuk Ilmu Komputer","Dosen":"1. Prof. Dr.-Ing. Mhd. Reza M. I. Pulungan, S.Si., M.Sc.\n\n2. Drs. Sri Mulyana, M.Kom.", "hari": 4, "jam": 3},
    13: {"Kode": "MII226001", "Nama": "Metodologi Riset Ilmu Komputer","Dosen":"1. Dr. Dyah Aruming Tyas, S.Si.\n\n     2. Aina Musdholifah, S.Kom., M.Kom., Ph.D." ,"hari": 5, "jam": 3},
    14: {"Kode": "MII226002", "Nama": "Proposal Tesis","Dosen":"", "hari": 0, "jam": 0},
    15: {"Kode": "MII226010", "Nama": "Seminar Tesis","Dosen":"", "hari": 0, "jam": 0},
    16: {"Kode": "MII226011", "Nama": "Tesis","Dosen":"" ,"hari": 0, "jam": 0},
}

matakuliah_minat = {
    17: {
        "Kode": "MII226501",
        "Nama": "Data Science",
        "Dosen": "1. Dr. Sigit Priyanta, S.Si., M.Kom.\n\n2. Arif Nurwidyantoro, S.Kom., M.Cs., Ph.D.",
        "hari": 3,
        "jam": 2
    },
    18: {
        "Kode": "MII226203",
        "Nama": "Teori Komputasi",
        "Dosen": "1. Moh. Edi Wibowo, S.Kom., M.Kom., Ph.D.\n\n2. Faizal Makhrus, S.Kom., M.Sc., Ph.D.",
        "hari": 4,
        "jam": 2
    },
    19: {
        "Kode": "MII226602",
        "Nama": "Jaringan Komputer Lanjut",
        "Dosen": "1. Muhammad Alfian Amrizal, B.Eng., M.I.S., Ph.D.\n\n2. Drs. Yohanes Suyanto, M.I.Kom.",
        "hari": 3,
        "jam": 2
    },
    20: {
        "Kode": "MII226504", 
        "Nama": "Pengembangan Perangkat Lunak",
        "Dosen": "1. Dr. Lukman Heryawan, S.T., M.T.",
        "hari": 3, 
        "jam": 3
    }
}


# Kode Ruang
kode_ruang = {1: 419, 2: 420, 3: 421, 4: 422}

# Konversi nilai jam
konversi_jam = {0:"",1: "7.30 - 10.00", 2: "10.30 - 13.00", 3: "13.30 - 16.00"}

# Konversi nilai hari
konversi_hari = {0:"",1: "Senin", 2: "Selasa", 3: "Rabu", 4: "Kamis", 5: "Jumat"}

# Kode matakuliah yang sudah diambil pada semester sebelumnya
matakuliah_sebelumnya = []


matakuliah = {**matakuliah_mkom, **matakuliah_wajib, **{k: v for k, v in matakuliah_minat.items()}}


# Parameter Algoritma Genetika
POPULATION_SIZE = 10
MAX_GENERATIONS = 10
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
NUM_MATKUL = 6

def calculate_fitness(individual):
    aturan_1 = 0  # Penalty for schedule conflict
    aturan_2 = 0  # Penalty for exceeding maximum courses per day
    aturan_3 = 0  # Penalty for exceeding maximum courses per hour
    penalty_1 = 0  # Penalty for schedule conflict
    penalty_2 = 0  # Penalty for exceeding maximum courses per day
    penalty_3 = 0  # Penalty for exceeding maximum courses per hour
    used_rooms = set()
    used_dosen = set()

    for hari in set([matakuliah[matkul]["hari"] for matkul in individual]):
        if hari:
            count_matkul_hari = sum(1 for matkul in individual if matakuliah[matkul]["hari"] == hari)
            if count_matkul_hari > 3:  # Soft Constraint: Mahasiswa mengikuti maksimal 3 mata kuliah dalam 1 hari
                aturan_1 += 1
                penalty_1 += 1

            for matkul in individual:
                if matakuliah[matkul]["hari"] == hari:
                    used_rooms.add(kode_ruang[random.choice(list(kode_ruang.keys()))])
                    for dosen in matakuliah[matkul]["Dosen"].split('\n'):
                        used_dosen.add(dosen.split(',')[0])  # Get dosen's name and add to set

    for jam in set([matakuliah[matkul]["jam"] for matkul in individual]):
        if jam:
            count_dosen_jam = sum(1 for matkul in individual if matakuliah[matkul]["jam"] == jam)
            if count_dosen_jam > 2:  # Hard Constraint: Dosen mengajar 2 Matakuliah dalam 1 jam
                aturan_2 +=1
                penalty_2 += 2

    # Check for room and dosen conflicts
    # if len(used_rooms) < len(individual) or len(used_dosen) < len(individual):
    #     aturan_1 +=1
    #     penalty_1 += 1

    # Hitung fitness
    fitness = 1 / (1 + ((aturan_1*penalty_1) +(aturan_2 * penalty_2)))
    return fitness


# Fungsi untuk menghasilkan populasi awal
def generate_initial_population(matakuliah_sebelumnya_id, minat=None, wajib=None):
    population = set()  # Menggunakan set untuk memastikan setiap individu unik
    while len(population) < POPULATION_SIZE:
        remaining_matakuliah = set(matakuliah_mkom.keys()) - set(matakuliah_sebelumnya_id)
        
        individual = []
        # individual = random.sample(list(matakuliah_mkom.keys()), NUM_MATKUL-2)
        # individual = [matkul for matkul in individual if matkul not in matakuliah_sebelumnya_id]
        
        # Jika ada minat, pastikan matakuliah minat tersebut dimasukkan ke dalam individu
        if minat:
            minat_id = next((key for key, value in matakuliah_minat.items() if value["Nama"] == minat["Nama"]), None)
            if minat_id:
                individual.append(minat_id)
                remaining_matakuliah.discard(minat_id)
        
        # Jika ada matakuliah wajib, pastikan matakuliah wajib tersebut dimasukkan ke dalam individu
        if wajib:
            wajib_id = next((key for key, value in matakuliah_wajib.items() if value["Nama"] == wajib["Nama"]), None)
            if wajib_id:
                individual.append(wajib_id)
                remaining_matakuliah.discard(wajib_id)
        
        # Tambahkan matakuliah lainnya dari sisa matakuliah yang tersedia
        while len(individual) < NUM_MATKUL:
            matkul_id = random.choice(list(remaining_matakuliah))
            individual.append(matkul_id)
            remaining_matakuliah.discard(matkul_id)

        # Pastikan individu memiliki jumlah matakuliah yang sesuai
        if len(individual) == NUM_MATKUL:
            # Menggunakan tuple untuk menyimpan individu karena list tidak hashable dan tidak dapat digunakan dalam set
            population.add(tuple(individual))

    # Mengonversi set kembali ke list sebelum mengembalikannya
    return [list(individual) for individual in population]



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
    child1 = parent1[:1] + parent2[1:]
    child2 = parent2[:1] + parent1[1:]
    return child1, child2

#crossover_point = random.randint(1, len(parent1) - 1)

# Fungsi mutasi menggunakan pemilihan nilai acak
def mutate(individual):
    if random.random() < MUTATION_RATE:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# Update Algoritma Genetika
def genetic_algorithm(matakuliah_sebelumnya_id, minat=None,wajib=None):
    print(matakuliah_sebelumnya_id)
    population = generate_initial_population(matakuliah_sebelumnya_id, minat,wajib)
    print(population)
    best_individual = None
    best_fitness = 0

    for generation in range(MAX_GENERATIONS):
        fitness_values = [calculate_fitness(individual) for individual in population]

        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1 = roulette_wheel_selection(population, fitness_values)
            parent2 = roulette_wheel_selection(population, fitness_values)
            child1, child2 = one_point_crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])

        population = new_population

        # Find the best individual in the current population
        current_best_individual = max(population, key=calculate_fitness)
        current_best_fitness = calculate_fitness(current_best_individual)

        # Update the best individual and fitness if necessary
        if current_best_fitness > best_fitness:
            best_individual = current_best_individual
            best_fitness = current_best_fitness
            
    return best_individual, best_fitness

def main():
    st.title("Penjadwalan Matakuliah dengan Algoritma Genetika")

    minat_chosen = False
    best_solution = []
    
    # Menampilkan data matakuliah
    st.subheader("Data Matakuliah")
    st.write("Matakuliah yang ditawarkan:")
    all_courses = {**matakuliah_mkom, **matakuliah_wajib, **matakuliah_minat}
    st.table(all_courses)

    nama_ke_id = {course["Nama"]: id for id, course in all_courses.items()}

    # Pilihan matakuliah yang sudah diambil pada semester sebelumnya
    matakuliah_sebelumnya.extend(st.multiselect("Pilih matakuliah yang telah diambil pada semester sebelumnya:", list(nama_ke_id.keys())))

    # Konversi matakuliah yang telah dipilih menjadi ID
    matakuliah_sebelumnya_id = [nama_ke_id[nama] for nama in matakuliah_sebelumnya]

    # Jika belum mengambil matakuliah minat, tampilkan selectbox untuk memilih minat
    if 17 not in matakuliah_sebelumnya_id and 18 not in matakuliah_sebelumnya_id and 19 not in matakuliah_sebelumnya_id and 20 not in matakuliah_sebelumnya_id:
        minat = st.selectbox("Pilih Minat:", ["", "Sains Data", "Sains Komputasional", "Sistem Komputer", "Manajemen Informasi"])
        if minat:
            minat_chosen = True
            st.write("Matakuliah Minat:")
            if minat == "Sains Data":
                st.table(matakuliah_minat[17])
                minat = matakuliah_minat[17]
            elif minat == "Sains Komputasional":
                st.table(matakuliah_minat[18])
                minat = matakuliah_minat[18]
            elif minat == "Sistem Komputer":
                st.table(matakuliah_minat[19])
                minat = matakuliah_minat[19]
            elif minat == "Manajemen Informasi":
                st.table(matakuliah_minat[20])
                minat = matakuliah_minat[20]
    
    # Jika telah mengambil matakuliah yang dibutuhkan untuk Tesis, tetapkan wajib
    if 11 in matakuliah_sebelumnya_id and 12 in matakuliah_sebelumnya_id and 13 in matakuliah_sebelumnya_id:
        wajib = matakuliah_wajib[14]
    elif 11 in matakuliah_sebelumnya_id and 12 in matakuliah_sebelumnya_id and 13 in matakuliah_sebelumnya_id and 14 in matakuliah_sebelumnya_id:
        wajib = matakuliah_wajib[15]
    elif 11 in matakuliah_sebelumnya_id and 12 in matakuliah_sebelumnya_id and 13 in matakuliah_sebelumnya_id and 14 in matakuliah_sebelumnya_id and 15 in matakuliah_sebelumnya_id:
        wajib = matakuliah_wajib[16]

    # Button untuk memproses penjadwalan
    if st.button("Proses Penjadwalan"):
        # Jalankan algoritma genetika
        best_solution, best_fitness = genetic_algorithm(matakuliah_sebelumnya_id, minat if minat_chosen else None, wajib if wajib else None)

        # best_solution = list(set(best_solution))

        print(len(best_solution))
        
        st.write("Fitness Terbaik:", best_fitness)
        st.write("Jadwal Optimal:")
        table_data = []
        for matkul in best_solution:
            kode_matkul = matakuliah[matkul]["Kode"]
            nama_matkul = matakuliah[matkul]["Nama"]
            dosen_matkul = matakuliah[matkul]["Dosen"]
            hari_matkul = konversi_hari[matakuliah[matkul]["hari"]]
            jam_matkul = konversi_jam[matakuliah[matkul]["jam"]]
            ruang_matkul = kode_ruang[random.choice(list(kode_ruang.keys()))]
            table_data.append([nama_matkul, kode_matkul, dosen_matkul, hari_matkul, jam_matkul, ruang_matkul])

        st.table(table_data)

if __name__ == "__main__":
    main()
