import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Baca data dari file Excel
data = pd.read_excel("data.xlsx")

# Menyiapkan variabel input dan output
kualitas = ctrl.Antecedent(np.arange(0, 11, 1), 'kualitas')
harga = ctrl.Antecedent(np.arange(0, 11, 1), 'harga')
pelayanan = ctrl.Antecedent(np.arange(0, 11, 1), 'pelayanan')
rating = ctrl.Consequent(np.arange(0, 11, 1), 'rating')

# Fungsi keanggotaan untuk variabel input dan output
kualitas['rendah'] = fuzz.trimf(kualitas.universe, [0, 0, 5])
kualitas['sedang'] = fuzz.trimf(kualitas.universe, [0, 5, 10])
kualitas['tinggi'] = fuzz.trimf(kualitas.universe, [5, 10, 10])

harga['mahal'] = fuzz.trimf(harga.universe, [0, 0, 5])
harga['sedang'] = fuzz.trimf(harga.universe, [0, 5, 10])
harga['murah'] = fuzz.trimf(harga.universe, [5, 10, 10])

pelayanan['buruk'] = fuzz.trimf(pelayanan.universe, [0, 0, 5])
pelayanan['cukup'] = fuzz.trimf(pelayanan.universe, [0, 5, 10])
pelayanan['baik'] = fuzz.trimf(pelayanan.universe, [5, 10, 10])

rating['rendah'] = fuzz.trimf(rating.universe, [0, 0, 5])
rating['sedang'] = fuzz.trimf(rating.universe, [0, 5, 10])
rating['tinggi'] = fuzz.trimf(rating.universe, [5, 10, 10])

# Rule base
rule1 = ctrl.Rule(kualitas['rendah'] & harga['murah'] & pelayanan['buruk'], rating['rendah'])
rule2 = ctrl.Rule(kualitas['rendah'] & harga['murah'] & pelayanan['cukup'], rating['rendah'])
rule3 = ctrl.Rule(kualitas['rendah'] & harga['murah'] & pelayanan['baik'], rating['sedang'])
rule4 = ctrl.Rule(kualitas['rendah'] & harga['sedang'] & pelayanan['buruk'], rating['rendah'])
rule5 = ctrl.Rule(kualitas['rendah'] & harga['sedang'] & pelayanan['cukup'], rating['sedang'])
rule6 = ctrl.Rule(kualitas['rendah'] & harga['sedang'] & pelayanan['baik'], rating['sedang'])
rule7 = ctrl.Rule(kualitas['rendah'] & harga['mahal'] & pelayanan['buruk'], rating['sedang'])
rule8 = ctrl.Rule(kualitas['rendah'] & harga['mahal'] & pelayanan['cukup'], rating['sedang'])
rule9 = ctrl.Rule(kualitas['rendah'] & harga['mahal'] & pelayanan['baik'], rating['tinggi'])

rule10 = ctrl.Rule(kualitas['sedang'] & harga['murah'] & pelayanan['buruk'], rating['rendah'])
rule11 = ctrl.Rule(kualitas['sedang'] & harga['murah'] & pelayanan['cukup'], rating['rendah'])
rule12 = ctrl.Rule(kualitas['sedang'] & harga['murah'] & pelayanan['baik'], rating['sedang'])
rule13 = ctrl.Rule(kualitas['sedang'] & harga['sedang'] & pelayanan['buruk'], rating['rendah'])
rule14 = ctrl.Rule(kualitas['sedang'] & harga['sedang'] & pelayanan['cukup'], rating['sedang'])
rule15 = ctrl.Rule(kualitas['sedang'] & harga['sedang'] & pelayanan['baik'], rating['sedang'])
rule16 = ctrl.Rule(kualitas['sedang'] & harga['mahal'] & pelayanan['buruk'], rating['sedang'])
rule17 = ctrl.Rule(kualitas['sedang'] & harga['mahal'] & pelayanan['cukup'], rating['sedang'])
rule18 = ctrl.Rule(kualitas['sedang'] & harga['mahal'] & pelayanan['baik'], rating['tinggi'])

rule19 = ctrl.Rule(kualitas['tinggi'] & harga['murah'] & pelayanan['buruk'], rating['sedang'])
rule20 = ctrl.Rule(kualitas['tinggi'] & harga['murah'] & pelayanan['cukup'], rating['sedang'])
rule21 = ctrl.Rule(kualitas['tinggi'] & harga['murah'] & pelayanan['baik'], rating['tinggi'])
rule22 = ctrl.Rule(kualitas['tinggi'] & harga['sedang'] & pelayanan['buruk'], rating['sedang'])
rule23 = ctrl.Rule(kualitas['tinggi'] & harga['sedang'] & pelayanan['cukup'], rating['tinggi'])
rule24 = ctrl.Rule(kualitas['tinggi'] & harga['sedang'] & pelayanan['baik'], rating['tinggi'])
rule25 = ctrl.Rule(kualitas['tinggi'] & harga['mahal'] & pelayanan['buruk'], rating['tinggi'])
rule26 = ctrl.Rule(kualitas['tinggi'] & harga['mahal'] & pelayanan['cukup'], rating['tinggi'])
rule27 = ctrl.Rule(kualitas['tinggi'] & harga['mahal'] & pelayanan['baik'], rating['tinggi'])

# Membuat sistem kontrol
system = ctrl.ControlSystem([rule1, rule2, rule3, rule4,  rule5,  rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27])
simulator = ctrl.ControlSystemSimulation(system)

# Proses inferensi dan defuzzifikasi
for i, row in data.iterrows():
    simulator.input['kualitas'] = row['kualitas']
    simulator.input['harga'] = row['harga']
    simulator.input['pelayanan'] = row['pelayanan']
    simulator.compute()
    output_value = simulator.output['rating']
    print(f"Sample {i+1}: Rating = {output_value}")

# Plot fungsi keanggotaan
kualitas.view()
harga.view()
pelayanan.view()
rating.view()

# Menampilkan plot
import matplotlib.pyplot as plt
plt.show()