import streamlit as st
import numpy as np
import random

# Data
matakuliah = {
    1: {"Kode": "MII225201", "Nama": "Analisis Algoritme", "Dosen": ["Drs. Suprapto, M.I.Kom.", "Dr. Nur Rokhman, S.Si., M.Kom."]},
    2: {"Kode": "MII225202", "Nama": "Matematika untuk Ilmu Komputer", "Dosen": ["Prof. Dr.-Ing. Mhd. Reza M. I. Pulungan, S.Si., M.Sc.", "Drs. Sri Mulyana, M.Kom."]},
    3: {"Kode": "MII226001", "Nama": "Metodologi Riset Ilmu Komputer", "Dosen": ["Dr. Dyah Aruming Tyas, S.Si.", "Aina Musdholifah, S.Kom., M.Kom., Ph.D."]},
    4: {"Kode": "MII225201", "Nama": "Pengolahan dan Analisis Citra Digital","Dosen":"1. Moh. Edi Wibowo, S.Kom., M.Kom., Ph.D.\n\n2. Dr.techn. Aufaclav Zatu Kusuma Frisky S.Si., M.Sc."},
    5: {"Kode": "MII226502", "Nama": "Sistem Temu Balik Informasi","Dosen":"1. Yunita Sari, S.Kom., M.Sc., Ph.D."},
    6: {"Kode": "MII226503", "Nama": "Data Warehouse dan Inteligensi Bisnis","Dosen":"1. Drs. Edi Winarko, M.Sc.,Ph.D."},
    7: {"Kode": "MII226504", "Nama": "Pengembangan Perangkat Lunak","Dosen":"1. Dr. Lukman Heryawan, S.T., M.T."},
    8: {"Kode": "MII226505", "Nama": "Kecerdasan Digital dan Informatika Sosial","Dosen":"1. Prof. Dr. Tri Kuntoro Priyambodo, M.Sc.\n\n2. Faizal Makhrus, S.Kom., M.Sc., Ph.D."},
    9: {"Kode": "MII226506", "Nama": "Manajemen dan Audit Sistem Informasi", "Dosen":"1. Dr. Mardhani Riasetiawan, SE Ak, M.T."},
    10: {"Kode": "MII226203", "Nama": "Teori Komputasi","Dosen":"1. Moh. Edi Wibowo, S.Kom., M.Kom., Ph.D.\n\n2. Faizal Makhrus, S.Kom., M.Sc., Ph.D."},
    11: {"Kode": "MII226401", "Nama": "Kecerdasan Komputasional dan Pembelajaran Mesin","Dosen":"1. Aina Musdholifah, S.Kom., M.Kom., Ph.D.\n\n2. Dr. Dyah Aruming Tyas, S.Si."},
    12: {"Kode": "MII226402", "Nama": "Prinsip Kecerdasan Artifisial","Dosen":"1. Prof. Dra. Sri Hartati, M.Sc., Ph.D.\n\n2. Afiahayati, S.Kom., M.Cs., Ph.D"},
    13: {"Kode": "MII226402", "Nama": "Rekayasa Fitur dan Pengenalan Pola","Dosen":"1. Wahyono, S.Kom., Ph.D."},
    14: {"Kode": "MII226404", "Nama": "Sistem Pendukung Pembuatan Keputusan","Dosen":"1. Prof. Drs. Retantyo Wardoyo, M.Sc., Ph.D."},
    15: {"Kode": "MII226501", "Nama": "Data Science","Dosen":"1. Dr. Sigit Priyanta, S.Si., M.Kom.\n\n2. Arif Nurwidyantoro, S.Kom., M.Cs., Ph.D."},
    16: {"Kode": "MII226601", "Nama": "Komputasi Awan dan Keamanan Siber","Dosen":"1. Prof. Dr.techn. Ahmad Ashari, M.I.Kom.\n\n2. Prof. Dr. Ir. Jazi Eko Istiyanto, M.Sc."},
    17: {"Kode": "MII226602", "Nama": "Jaringan Komputer Lanjut","Dosen":"1. Muhammad Alfian Amrizal, B.Eng., M.I.S., Ph.D.\n\n2. Drs. Yohanes Suyanto, M.I.Kom."},
    18: {"Kode": "MII226603", "Nama": "Platform dan Arsitektur Big Data","Dosen":"1. Dr. techn. Khabib Mustofa, S.Si., M.Kom.\n\n2. Muhammad Alfian Amrizal, B.Eng., M.I.S., Ph.D."},

}


kode_ruang = {1: 419, 2: 420, 3: 421, 4: 422}

kode_jam = {1: " 7.30 - 10.00", 2: "10.30 - 13.00", 3: "13.30 - 16.00"}

kode_hari = {1: "Senin", 2: "Selasa", 3: "Rabu", 4: "Kamis", 5: "Jumat"}

# Inisialisasi parameter algoritma genetika
pop_size = 10
max_generations = 100
mutation_rate = 0.1

# Fungsi fitness
def fitness(individual):
    penalty = 0
    for day in range(1, 6):
        day_courses = [individual[course] for course in individual if individual[course]["hari"] == day]
        unique_courses = set()
        unique_rooms = set()
        for course in day_courses:
            if course["kode"] in unique_courses:
                penalty += 1
            else:
                unique_courses.add(course["kode"])
                
            if course["ruang"] in unique_rooms:
                penalty += 1
            else:
                unique_rooms.add(course["ruang"])

        for slot in range(1, 4):
            slot_courses = [course for course in day_courses if course["jam"] == slot]
            unique_teachers = set()
            for course in slot_courses:
                for teacher in course["dosen"]:
                    if teacher in unique_teachers:
                        penalty += 1
                    else:
                        unique_teachers.add(teacher)

    return 1 / (1 + penalty)

def crossover(parent1, parent2):
    crossover_point = random.choice(list(parent1.keys()))
    child1 = {}
    child2 = {}
    for key in parent1.keys():
        if key < crossover_point:
            child1[key] = parent1[key]
            child2[key] = parent2[key]
        else:
            child1[key] = parent2[key]
            child2[key] = parent1[key]
    
    # Check if crossover results in conflicts
    if has_conflict(child1) or has_conflict(child2):
        # If conflicts exist, perform mutation
        child1 = mutation(child1)
        child2 = mutation(child2)
        
    return child1, child2

def mutation(individual):
    max_attempts = 10  # Maximum mutation attempts
    attempts = 0
    
    while attempts < max_attempts:
        mutated_individual = individual.copy()
        for course in mutated_individual:
            if random.random() < mutation_rate:
                mutated_individual[course]["hari"] = random.randint(1, 5)
                mutated_individual[course]["jam"] = random.randint(1, 3)

        if not has_conflict(mutated_individual):
            return mutated_individual  # If mutation successful without conflicts, return mutated result

        attempts += 1

    return individual  # If all mutation attempts fail, return the original individual

def has_conflict(schedule):
    # Check for conflicts in schedule
    courses = list(schedule.values())
    for i, course1 in enumerate(courses):
        for j, course2 in enumerate(courses):
            if i != j and (course1["hari"] == course2["hari"] and course1["jam"] == course2["jam"] and course1["ruang"] == course2["ruang"]):
                return True
    return False

def initialize_population():
    population = []
    for _ in range(pop_size):
        schedule = {}
        for key, value in matakuliah.items():
            schedule[key] = {"kode": value["Kode"], "nama": value["Nama"], "dosen": value["Dosen"],
                              "hari": random.randint(1, 5), "jam": random.randint(1, 3), "ruang": random.randint(1, 4)}
        population.append(schedule)
    return population

def genetic_algorithm():
    population = initialize_population()

    for generation in range(max_generations):
        fitness_scores = [fitness(individual) for individual in population]

        # Roulette wheel selection
        total_fitness = sum(fitness_scores)
        probabilities = [score / total_fitness for score in fitness_scores]

        # Crossover
        new_population = []
        for _ in range(pop_size // 2):
            parent1, parent2 = random.choices(population, weights=probabilities, k=2)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([child1, child2])

        # Mutation
        mutated_population = [mutation(individual) for individual in new_population]

        # Elitism: Select the best individuals from the previous population
        population = sorted(population, key=lambda x: fitness(x), reverse=True)[:pop_size // 2]
        population.extend(mutated_population)

    best_individual = max(population, key=fitness)
    return best_individual

# Streamlit UI
def display_schedule(schedule):
    table_data = []
    for day in range(1, 6):
        for slot in range(1, 4):
            courses = [course for course in schedule.values() if course["hari"] == day and course["jam"] == slot]
            for course in courses:
                table_data.append([kode_hari[day], kode_jam[slot], course["kode"], course["nama"], "".join(course["dosen"]), kode_ruang[course["ruang"]]])

    st.table(table_data)

def main():
    st.title("Penjadwalan Matakuliah dengan Algoritma Genetika")
    
    # Menampilkan data matakuliah
    st.subheader("Data Matakuliah")
    st.table(matakuliah)

    st.title("Penjadwalan Matakuliah")
    st.write("Hasil Penjadwalan Matakuliah Optimal:")
    best_schedule = genetic_algorithm()
    display_schedule(best_schedule)

if __name__ == "__main__":
    main()
