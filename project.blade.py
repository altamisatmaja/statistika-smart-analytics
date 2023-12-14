import csv
import pandas as pd

file = 'db.csv'
kolom = ['Responden','K1','K2','K3','K4','K5','K6','K7','K8','K9','K10','K11','K12','K13']
data_frame = pd.read_csv(file)
 
print("Original Data frame")
print(data_frame)
 
# print(data_frame.describe())
# print(f"Ini data max: \n{data_frame.max()}")
# print(f"Ini data min: \n{data_frame.min()}")


# get data min per kriteria
print("\nIni data min dari masing-masing kriteria\n")
data_min_k1 = data_frame.min()[1]
data_min_k2 = data_frame.min()[2]
data_min_k3 = data_frame.min()[3]
data_min_k4 = data_frame.min()[4]
data_min_k5 = data_frame.min()[5]
data_min_k6 = data_frame.min()[6]
data_min_k7 = data_frame.min()[7]
data_min_k8 = data_frame.min()[8]
data_min_k9 = data_frame.min()[9]
data_min_k10 = data_frame.min()[10]
data_min_k11 = data_frame.min()[11]
data_min_k12 = data_frame.min()[12]
data_min_k13 = data_frame.min()[13]

print(data_min_k1)
print(data_min_k2)
print(data_min_k3)
print(data_min_k4)
print(data_min_k5)
print(data_min_k6)
print(data_min_k7)
print(data_min_k8)
print(data_min_k9)
print(data_min_k10)
print(data_min_k11)
print(data_min_k12)
print(data_min_k13)


print("\nIni data max dari masing-masing kriteria\n")
# get data max per kriteria
data_max_k1 = data_frame.max()[1]
data_max_k2 = data_frame.max()[2]
data_max_k3 = data_frame.max()[3]
data_max_k4 = data_frame.max()[4]
data_max_k5 = data_frame.max()[5]
data_max_k6 = data_frame.max()[6]
data_max_k7 = data_frame.max()[7]
data_max_k8 = data_frame.max()[8]
data_max_k9 = data_frame.max()[9]
data_max_k10 = data_frame.max()[10]
data_max_k11 = data_frame.max()[11]
data_max_k12 = data_frame.max()[12]
data_max_k13 = data_frame.max()[13]

print(data_max_k1)
print(data_max_k2)
print(data_max_k3)
print(data_max_k4)
print(data_max_k5)
print(data_max_k6)
print(data_max_k7)
print(data_max_k8)
print(data_max_k9)
print(data_max_k10)
print(data_max_k11)
print(data_max_k12)
print(data_max_k13)

# data dari yanuario
yanuario = data_frame.iloc[0]
print(yanuario)
yanuario_k1 = yanuario.iloc[1]
yanuario_k2 = yanuario.iloc[2]
yanuario_k3 = yanuario.iloc[3]
yanuario_k4 = yanuario.iloc[4]
yanuario_k5 = yanuario.iloc[5]
yanuario_k6 = yanuario.iloc[6]
yanuario_k7 = yanuario.iloc[7]
yanuario_k8 = yanuario.iloc[8]
yanuario_k9 = yanuario.iloc[9]
yanuario_k10 = yanuario.iloc[10]
yanuario_k11 = yanuario.iloc[11]
yanuario_k12 = yanuario.iloc[12]
yanuario_k13 = yanuario.iloc[13]

# data dari alan
alan = data_frame.iloc[1]
print(alan)
alan_k1 = alan.iloc[1]
alan_k2 = alan.iloc[2]
alan_k3 = alan.iloc[3]
alan_k4 = alan.iloc[4]
alan_k5 = alan.iloc[5]
alan_k6 = alan.iloc[6]
alan_k7 = alan.iloc[7]
alan_k8 = alan.iloc[8]
alan_k9 = alan.iloc[9]
alan_k10 = alan.iloc[10]
alan_k11 = alan.iloc[11]
alan_k12 = alan.iloc[12]
alan_k13 = alan.iloc[13]

# data dari aqil
aqil = data_frame.iloc[2]
print(aqil)
aqil_k1 = aqil.iloc[1]
aqil_k2 = aqil.iloc[2]
aqil_k3 = aqil.iloc[3]
aqil_k4 = aqil.iloc[4]
aqil_k5 = aqil.iloc[5]
aqil_k6 = aqil.iloc[6]
aqil_k7 = aqil.iloc[7]
aqil_k8 = aqil.iloc[8]
aqil_k9 = aqil.iloc[9]
aqil_k10 = aqil.iloc[10]
aqil_k11 = aqil.iloc[11]
aqil_k12 = aqil.iloc[12]
aqil_k13 = aqil.iloc[13]

# data dari mahisa
mahisa = data_frame.iloc[3]
print(mahisa)
mahisa_k1 = mahisa.iloc[1]
mahisa_k2 = mahisa.iloc[2]
mahisa_k3 = mahisa.iloc[3]
mahisa_k4 = mahisa.iloc[4]
mahisa_k5 = mahisa.iloc[5]
mahisa_k6 = mahisa.iloc[6]
mahisa_k7 = mahisa.iloc[7]
mahisa_k8 = mahisa.iloc[8]
mahisa_k9 = mahisa.iloc[9]
mahisa_k10 = mahisa.iloc[10]
mahisa_k11 = mahisa.iloc[11]
mahisa_k12 = mahisa.iloc[12]
mahisa_k13 = mahisa.iloc[13]

# data dari tari
tari = data_frame.iloc[4]
print(tari)
tari_k1 = tari.iloc[1]
tari_k2 = tari.iloc[2]
tari_k3 = tari.iloc[3]
tari_k4 = tari.iloc[4]
tari_k5 = tari.iloc[5]
tari_k6 = tari.iloc[6]
tari_k7 = tari.iloc[7]
tari_k8 = tari.iloc[8]
tari_k9 = tari.iloc[9]
tari_k10 = tari.iloc[10]
tari_k11 = tari.iloc[11]
tari_k12 = tari.iloc[12]
tari_k13 = tari.iloc[13]

# data dari fanny
fanny = data_frame.iloc[5]
print(fanny)
fanny_k1 = fanny.iloc[1]
fanny_k2 = fanny.iloc[2]
fanny_k3 = fanny.iloc[3]
fanny_k4 = fanny.iloc[4]
fanny_k5 = fanny.iloc[5]
fanny_k6 = fanny.iloc[6]
fanny_k7 = fanny.iloc[7]
fanny_k8 = fanny.iloc[8]
fanny_k9 = fanny.iloc[9]
fanny_k10 = fanny.iloc[10]
fanny_k11 = fanny.iloc[11]
fanny_k12 = fanny.iloc[12]
fanny_k13 = fanny.iloc[13]

# data dari fathan
fathan = data_frame.iloc[6]
print(fathan)
fathan_k1 = fathan.iloc[1]
fathan_k2 = fathan.iloc[2]
fathan_k3 = fathan.iloc[3]
fathan_k4 = fathan.iloc[4]
fathan_k5 = fathan.iloc[5]
fathan_k6 = fathan.iloc[6]
fathan_k7 = fathan.iloc[7]
fathan_k8 = fathan.iloc[8]
fathan_k9 = fathan.iloc[9]
fathan_k10 = fathan.iloc[10]
fathan_k11 = fathan.iloc[11]
fathan_k12 = fathan.iloc[12]
fathan_k13 = fathan.iloc[13]

# data dari sindika
sindika = data_frame.iloc[7]
print(sindika)
sindika_k1 = sindika.iloc[1]
sindika_k2 = sindika.iloc[2]
sindika_k3 = sindika.iloc[3]
sindika_k4 = sindika.iloc[4]
sindika_k5 = sindika.iloc[5]
sindika_k6 = sindika.iloc[6]
sindika_k7 = sindika.iloc[7]
sindika_k8 = sindika.iloc[8]
sindika_k9 = sindika.iloc[9]
sindika_k10 = sindika.iloc[10]
sindika_k11 = sindika.iloc[11]
sindika_k12 = sindika.iloc[12]
sindika_k13 = sindika.iloc[13]

# data dari aryawildan
aryawildan = data_frame.iloc[8]
print(aryawildan)
aryawildan_k1 = aryawildan.iloc[1]
aryawildan_k2 = aryawildan.iloc[2]
aryawildan_k3 = aryawildan.iloc[3]
aryawildan_k4 = aryawildan.iloc[4]
aryawildan_k5 = aryawildan.iloc[5]
aryawildan_k6 = aryawildan.iloc[6]
aryawildan_k7 = aryawildan.iloc[7]
aryawildan_k8 = aryawildan.iloc[8]
aryawildan_k9 = aryawildan.iloc[9]
aryawildan_k10 = aryawildan.iloc[10]
aryawildan_k11 = aryawildan.iloc[11]
aryawildan_k12 = aryawildan.iloc[12]
aryawildan_k13 = aryawildan.iloc[13]

# data dari icha
icha = data_frame.iloc[9]
print(icha)
icha_k1 = icha.iloc[1]
icha_k2 = icha.iloc[2]
icha_k3 = icha.iloc[3]
icha_k4 = icha.iloc[4]
icha_k5 = icha.iloc[5]
icha_k6 = icha.iloc[6]
icha_k7 = icha.iloc[7]
icha_k8 = icha.iloc[8]
icha_k9 = icha.iloc[9]
icha_k10 = icha.iloc[10]
icha_k11 = icha.iloc[11]
icha_k12 = icha.iloc[12]
icha_k13 = icha.iloc[13]

# data dari nugroho
nugroho = data_frame.iloc[10]
print(nugroho)
nugroho_k1 = nugroho.iloc[1]
nugroho_k2 = nugroho.iloc[2]
nugroho_k3 = nugroho.iloc[3]
nugroho_k4 = nugroho.iloc[4]
nugroho_k5 = nugroho.iloc[5]
nugroho_k6 = nugroho.iloc[6]
nugroho_k7 = nugroho.iloc[7]
nugroho_k8 = nugroho.iloc[8]
nugroho_k9 = nugroho.iloc[9]
nugroho_k10 = nugroho.iloc[10]
nugroho_k11 = nugroho.iloc[11]
nugroho_k12 = nugroho.iloc[12]
nugroho_k13 = nugroho.iloc[13]

# data dari adit
adit = data_frame.iloc[11]
print(adit)
adit_k1 = adit.iloc[1]
adit_k2 = adit.iloc[2]
adit_k3 = adit.iloc[3]
adit_k4 = adit.iloc[4]
adit_k5 = adit.iloc[5]
adit_k6 = adit.iloc[6]
adit_k7 = adit.iloc[7]
adit_k8 = adit.iloc[8]
adit_k9 = adit.iloc[9]
adit_k10 = adit.iloc[10]
adit_k11 = adit.iloc[11]
adit_k12 = adit.iloc[12]
adit_k13 = adit.iloc[13]

# data dari umam
umam = data_frame.iloc[12]
print(umam)
umam_k1 = umam.iloc[1]
umam_k2 = umam.iloc[2]
umam_k3 = umam.iloc[3]
umam_k4 = umam.iloc[4]
umam_k5 = umam.iloc[5]
umam_k6 = umam.iloc[6]
umam_k7 = umam.iloc[7]
umam_k8 = umam.iloc[8]
umam_k9 = umam.iloc[9]
umam_k10 = umam.iloc[10]
umam_k11 = umam.iloc[11]
umam_k12 = umam.iloc[12]
umam_k13 = umam.iloc[13]

# data dari nana
nana = data_frame.iloc[13]
print(nana)
nana_k1 = nana.iloc[1]
nana_k2 = nana.iloc[2]
nana_k3 = nana.iloc[3]
nana_k4 = nana.iloc[4]
nana_k5 = nana.iloc[5]
nana_k6 = nana.iloc[6]
nana_k7 = nana.iloc[7]
nana_k8 = nana.iloc[8]
nana_k9 = nana.iloc[9]
nana_k10 = nana.iloc[10]
nana_k11 = nana.iloc[11]
nana_k12 = nana.iloc[12]
nana_k13 = nana.iloc[13]

# data dari syahrur
syahrur = data_frame.iloc[14]
print(syahrur)
syahrur_k1 = syahrur.iloc[1]
syahrur_k2 = syahrur.iloc[2]
syahrur_k3 = syahrur.iloc[3]
syahrur_k4 = syahrur.iloc[4]
syahrur_k5 = syahrur.iloc[5]
syahrur_k6 = syahrur.iloc[6]
syahrur_k7 = syahrur.iloc[7]
syahrur_k8 = syahrur.iloc[8]
syahrur_k9 = syahrur.iloc[9]
syahrur_k10 = syahrur.iloc[10]
syahrur_k11 = syahrur.iloc[11]
syahrur_k12 = syahrur.iloc[12]
syahrur_k13 = syahrur.iloc[13]

# data dari dewi
dewi = data_frame.iloc[15]
print(dewi)
dewi_k1 = dewi.iloc[1]
dewi_k2 = dewi.iloc[2]
dewi_k3 = dewi.iloc[3]
dewi_k4 = dewi.iloc[4]
dewi_k5 = dewi.iloc[5]
dewi_k6 = dewi.iloc[6]
dewi_k7 = dewi.iloc[7]
dewi_k8 = dewi.iloc[8]
dewi_k9 = dewi.iloc[9]
dewi_k10 = dewi.iloc[10]
dewi_k11 = dewi.iloc[11]
dewi_k12 = dewi.iloc[12]
dewi_k13 = dewi.iloc[13]

# data dari gerald
gerald = data_frame.iloc[16]
print(gerald)
gerald_k1 = gerald.iloc[1]
gerald_k2 = gerald.iloc[2]
gerald_k3 = gerald.iloc[3]
gerald_k4 = gerald.iloc[4]
gerald_k5 = gerald.iloc[5]
gerald_k6 = gerald.iloc[6]
gerald_k7 = gerald.iloc[7]
gerald_k8 = gerald.iloc[8]
gerald_k9 = gerald.iloc[9]
gerald_k10 = gerald.iloc[10]
gerald_k11 = gerald.iloc[11]
gerald_k12 = gerald.iloc[12]
gerald_k13 = gerald.iloc[13]

# data dari angga
angga = data_frame.iloc[17]
print(angga)
angga_k1 = angga.iloc[1]
angga_k2 = angga.iloc[2]
angga_k3 = angga.iloc[3]
angga_k4 = angga.iloc[4]
angga_k5 = angga.iloc[5]
angga_k6 = angga.iloc[6]
angga_k7 = angga.iloc[7]
angga_k8 = angga.iloc[8]
angga_k9 = angga.iloc[9]
angga_k10 = angga.iloc[10]
angga_k11 = angga.iloc[11]
angga_k12 = angga.iloc[12]
angga_k13 = angga.iloc[13]

# data dari fahmi
fahmi = data_frame.iloc[18]
print(fahmi)
fahmi_k1 = fahmi.iloc[1]
fahmi_k2 = fahmi.iloc[2]
fahmi_k3 = fahmi.iloc[3]
fahmi_k4 = fahmi.iloc[4]
fahmi_k5 = fahmi.iloc[5]
fahmi_k6 = fahmi.iloc[6]
fahmi_k7 = fahmi.iloc[7]
fahmi_k8 = fahmi.iloc[8]
fahmi_k9 = fahmi.iloc[9]
fahmi_k10 = fahmi.iloc[10]
fahmi_k11 = fahmi.iloc[11]
fahmi_k12 = fahmi.iloc[12]
fahmi_k13 = fahmi.iloc[13]

# data dari bima
bima = data_frame.iloc[19]
print(bima)
bima_k1 = bima.iloc[1]
bima_k2 = bima.iloc[2]
bima_k3 = bima.iloc[3]
bima_k4 = bima.iloc[4]
bima_k5 = bima.iloc[5]
bima_k6 = bima.iloc[6]
bima_k7 = bima.iloc[7]
bima_k8 = bima.iloc[8]
bima_k9 = bima.iloc[9]
bima_k10 = bima.iloc[10]
bima_k11 = bima.iloc[11]
bima_k12 = bima.iloc[12]
bima_k13 = bima.iloc[13]

# alternative utility
# based on rumus
# ui(ai) = (cout - cmin) / (cmax - cmin)

# rumus statistika untuk yanuario

# calculate for k1
def hitung_ui_k1_yanuario(data_max_k1, data_min_k1, yanuario_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_yanuario = yanuario_k1
    
    ui_k1 = int(100 * ((cout_k1_yanuario - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari Yanuario\t\t: {hitung_ui_k1_yanuario(data_max_k1, data_min_k1, yanuario_k1)}")

# calculate for k2
def hitung_ui_k2_yanuario(data_max_k2, data_min_k2, yanuario_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_yanuario = yanuario_k2
    
    ui_k2 = int(100 * ((cout_k2_yanuario - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari Yanuario\t\t: {hitung_ui_k2_yanuario(data_max_k2, data_min_k2, yanuario_k2)}")

# calculate for k3
def hitung_ui_k3_yanuario(data_max_k3, data_min_k3, yanuario_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_yanuario = yanuario_k3
    
    ui_k3 = int(100 * ((cout_k3_yanuario - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari Yanuario\t\t: {hitung_ui_k3_yanuario(data_max_k3, data_min_k3, yanuario_k3)}")

# calculate for k4
def hitung_ui_k4_yanuario(data_max_k4, data_min_k4, yanuario_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_yanuario = yanuario_k4
    
    ui_k4 = int(100 * ((cout_k4_yanuario - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari Yanuario\t\t: {hitung_ui_k4_yanuario(data_max_k4, data_min_k4, yanuario_k4)}")

# calculate for k5
def hitung_ui_k5_yanuario(data_max_k5, data_min_k5, yanuario_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_yanuario = yanuario_k5
    
    ui_k5 = int(100 * ((cout_k5_yanuario - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari Yanuario\t\t: {hitung_ui_k5_yanuario(data_max_k5, data_min_k5, yanuario_k5)}")

# calculate for k6
def hitung_ui_k6_yanuario(data_max_k6, data_min_k6, yanuario_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_yanuario = yanuario_k6
    
    ui_k6 = int(100 * ((cout_k6_yanuario - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari Yanuario\t\t: {hitung_ui_k6_yanuario(data_max_k6, data_min_k6, yanuario_k6)}")

# calculate for k7
def hitung_ui_k7_yanuario(data_max_k7, data_min_k7, yanuario_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_yanuario = yanuario_k7
    
    ui_k7 = int(100 * ((cout_k7_yanuario - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari Yanuario\t\t: {hitung_ui_k7_yanuario(data_max_k7, data_min_k7, yanuario_k7)}")

# calculate for k8
def hitung_ui_k8_yanuario(data_max_k8, data_min_k8, yanuario_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_yanuario = yanuario_k8
    
    ui_k8 = int(100 * ((cout_k8_yanuario - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari Yanuario\t\t: {hitung_ui_k8_yanuario(data_max_k8, data_min_k8, yanuario_k8)}")

# calculate for k9
def hitung_ui_k9_yanuario(data_max_k9, data_min_k9, yanuario_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_yanuario = yanuario_k9
    
    ui_k9 = int(100 * ((cout_k9_yanuario - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari Yanuario\t\t: {hitung_ui_k9_yanuario(data_max_k9, data_min_k9, yanuario_k9)}")

# calculate for k10
def hitung_ui_k10_yanuario(data_max_k10, data_min_k10, yanuario_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_yanuario = yanuario_k10
    
    ui_k10 = int(100 * ((cout_k10_yanuario - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari Yanuario\t\t: {hitung_ui_k10_yanuario(data_max_k10, data_min_k10, yanuario_k10)}")

# calculate for k11
def hitung_ui_k11_yanuario(data_max_k11, data_min_k11, yanuario_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_yanuario = yanuario_k11
    
    ui_k11 = int(100 * ((cout_k11_yanuario - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari Yanuario\t\t: {hitung_ui_k11_yanuario(data_max_k11, data_min_k11, yanuario_k11)}")

# calculate for k12
def hitung_ui_k12_yanuario(data_max_k12, data_min_k12, yanuario_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_yanuario = yanuario_k12
    
    ui_k12 = int(100 * ((cout_k12_yanuario - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari Yanuario\t\t: {hitung_ui_k12_yanuario(data_max_k12, data_min_k12, yanuario_k12)}")

# calculate for k13
def hitung_ui_k13_yanuario(data_max_k13, data_min_k13, yanuario_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_yanuario = yanuario_k13
    
    ui_k13 = int(100 * ((cout_k13_yanuario - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari Yanuario\t\t: {hitung_ui_k13_yanuario(data_max_k13, data_min_k13, yanuario_k13)}")


# rumus statistika untuk alan

# calculate for k1
def hitung_ui_k1_alan(data_max_k1, data_min_k1, alan_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_alan = alan_k1
    
    ui_k1 = int(100 * ((cout_k1_alan - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari alan\t\t: {hitung_ui_k1_alan(data_max_k1, data_min_k1, alan_k1)}")

# calculate for k2
def hitung_ui_k2_alan(data_max_k2, data_min_k2, alan_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_alan = alan_k2
    
    ui_k2 = int(100 * ((cout_k2_alan - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari alan\t\t: {hitung_ui_k2_alan(data_max_k2, data_min_k2, alan_k2)}")

# calculate for k3
def hitung_ui_k3_alan(data_max_k3, data_min_k3, alan_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_alan = alan_k3
    
    ui_k3 = int(100 * ((cout_k3_alan - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari alan\t\t: {hitung_ui_k3_alan(data_max_k3, data_min_k3, alan_k3)}")

# calculate for k4
def hitung_ui_k4_alan(data_max_k4, data_min_k4, alan_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_alan = alan_k4
    
    ui_k4 = int(100 * ((cout_k4_alan - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari alan\t\t: {hitung_ui_k4_alan(data_max_k4, data_min_k4, alan_k4)}")

# calculate for k5
def hitung_ui_k5_alan(data_max_k5, data_min_k5, alan_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_alan = alan_k5
    
    ui_k5 = int(100 * ((cout_k5_alan - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari alan\t\t: {hitung_ui_k5_alan(data_max_k5, data_min_k5, alan_k5)}")

# calculate for k6
def hitung_ui_k6_alan(data_max_k6, data_min_k6, alan_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_alan = alan_k6
    
    ui_k6 = int(100 * ((cout_k6_alan - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari alan\t\t: {hitung_ui_k6_alan(data_max_k6, data_min_k6, alan_k6)}")

# calculate for k7
def hitung_ui_k7_alan(data_max_k7, data_min_k7, alan_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_alan = alan_k7
    
    ui_k7 = int(100 * ((cout_k7_alan - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari alan\t\t: {hitung_ui_k7_alan(data_max_k7, data_min_k7, alan_k7)}")

# calculate for k8
def hitung_ui_k8_alan(data_max_k8, data_min_k8, alan_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_alan = alan_k8
    
    ui_k8 = int(100 * ((cout_k8_alan - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari alan\t\t: {hitung_ui_k8_alan(data_max_k8, data_min_k8, alan_k8)}")

# calculate for k9
def hitung_ui_k9_alan(data_max_k9, data_min_k9, alan_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_alan = alan_k9
    
    ui_k9 = int(100 * ((cout_k9_alan - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari alan\t\t: {hitung_ui_k9_alan(data_max_k9, data_min_k9, alan_k9)}")

# calculate for k10
def hitung_ui_k10_alan(data_max_k10, data_min_k10, alan_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_alan = alan_k10
    
    ui_k10 = int(100 * ((cout_k10_alan - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari alan\t\t: {hitung_ui_k10_alan(data_max_k10, data_min_k10, alan_k10)}")

# calculate for k11
def hitung_ui_k11_alan(data_max_k11, data_min_k11, alan_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_alan = alan_k11
    
    ui_k11 = int(100 * ((cout_k11_alan - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari alan\t\t: {hitung_ui_k11_alan(data_max_k11, data_min_k11, alan_k11)}")

# calculate for k12
def hitung_ui_k12_alan(data_max_k12, data_min_k12, alan_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_alan = alan_k12
    
    ui_k12 = int(100 * ((cout_k12_alan - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari alan\t\t: {hitung_ui_k12_alan(data_max_k12, data_min_k12, alan_k12)}")

# calculate for k13
def hitung_ui_k13_alan(data_max_k13, data_min_k13, alan_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_alan = alan_k13
    
    ui_k13 = int(100 * ((cout_k13_alan - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari alan\t\t: {hitung_ui_k13_alan(data_max_k13, data_min_k13, alan_k13)}")


# rumus statistika untuk aqil

# calculate for k1
def hitung_ui_k1_aqil(data_max_k1, data_min_k1, aqil_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_aqil = aqil_k1
    
    ui_k1 = int(100 * ((cout_k1_aqil - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari aqil\t\t: {hitung_ui_k1_aqil(data_max_k1, data_min_k1, aqil_k1)}")

# calculate for k2
def hitung_ui_k2_aqil(data_max_k2, data_min_k2, aqil_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_aqil = aqil_k2
    
    ui_k2 = int(100 * ((cout_k2_aqil - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari aqil\t\t: {hitung_ui_k2_aqil(data_max_k2, data_min_k2, aqil_k2)}")

# calculate for k3
def hitung_ui_k3_aqil(data_max_k3, data_min_k3, aqil_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_aqil = aqil_k3
    
    ui_k3 = int(100 * ((cout_k3_aqil - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari aqil\t\t: {hitung_ui_k3_aqil(data_max_k3, data_min_k3, aqil_k3)}")

# calculate for k4
def hitung_ui_k4_aqil(data_max_k4, data_min_k4, aqil_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_aqil = aqil_k4
    
    ui_k4 = int(100 * ((cout_k4_aqil - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari aqil\t\t: {hitung_ui_k4_aqil(data_max_k4, data_min_k4, aqil_k4)}")

# calculate for k5
def hitung_ui_k5_aqil(data_max_k5, data_min_k5, aqil_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_aqil = aqil_k5
    
    ui_k5 = int(100 * ((cout_k5_aqil - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari aqil\t\t: {hitung_ui_k5_aqil(data_max_k5, data_min_k5, aqil_k5)}")

# calculate for k6
def hitung_ui_k6_aqil(data_max_k6, data_min_k6, aqil_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_aqil = aqil_k6
    
    ui_k6 = int(100 * ((cout_k6_aqil - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari aqil\t\t: {hitung_ui_k6_aqil(data_max_k6, data_min_k6, aqil_k6)}")

# calculate for k7
def hitung_ui_k7_aqil(data_max_k7, data_min_k7, aqil_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_aqil = aqil_k7
    
    ui_k7 = int(100 * ((cout_k7_aqil - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari aqil\t\t: {hitung_ui_k7_aqil(data_max_k7, data_min_k7, aqil_k7)}")

# calculate for k8
def hitung_ui_k8_aqil(data_max_k8, data_min_k8, aqil_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_aqil = aqil_k8
    
    ui_k8 = int(100 * ((cout_k8_aqil - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari aqil\t\t: {hitung_ui_k8_aqil(data_max_k8, data_min_k8, aqil_k8)}")

# calculate for k9
def hitung_ui_k9_aqil(data_max_k9, data_min_k9, aqil_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_aqil = aqil_k9
    
    ui_k9 = int(100 * ((cout_k9_aqil - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari aqil\t\t: {hitung_ui_k9_aqil(data_max_k9, data_min_k9, aqil_k9)}")

# calculate for k10
def hitung_ui_k10_aqil(data_max_k10, data_min_k10, aqil_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_aqil = aqil_k10
    
    ui_k10 = int(100 * ((cout_k10_aqil - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari aqil\t\t: {hitung_ui_k10_aqil(data_max_k10, data_min_k10, aqil_k10)}")

# calculate for k11
def hitung_ui_k11_aqil(data_max_k11, data_min_k11, aqil_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_aqil = aqil_k11
    
    ui_k11 = int(100 * ((cout_k11_aqil - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari aqil\t\t: {hitung_ui_k11_aqil(data_max_k11, data_min_k11, aqil_k11)}")

# calculate for k12
def hitung_ui_k12_aqil(data_max_k12, data_min_k12, aqil_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_aqil = aqil_k12
    
    ui_k12 = int(100 * ((cout_k12_aqil - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari aqil\t\t: {hitung_ui_k12_aqil(data_max_k12, data_min_k12, aqil_k12)}")

# calculate for k13
def hitung_ui_k13_aqil(data_max_k13, data_min_k13, aqil_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_aqil = aqil_k13
    
    ui_k13 = int(100 * ((cout_k13_aqil - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari aqil\t\t: {hitung_ui_k13_aqil(data_max_k13, data_min_k13, aqil_k13)}")

# rumus statistika untuk mahisa

# calculate for k1
def hitung_ui_k1_mahisa(data_max_k1, data_min_k1, mahisa_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_mahisa = mahisa_k1
    
    ui_k1 = int(100 * ((cout_k1_mahisa - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari mahisa\t\t: {hitung_ui_k1_mahisa(data_max_k1, data_min_k1, mahisa_k1)}")

# calculate for k2
def hitung_ui_k2_mahisa(data_max_k2, data_min_k2, mahisa_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_mahisa = mahisa_k2
    
    ui_k2 = int(100 * ((cout_k2_mahisa - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari mahisa\t\t: {hitung_ui_k2_mahisa(data_max_k2, data_min_k2, mahisa_k2)}")

# calculate for k3
def hitung_ui_k3_mahisa(data_max_k3, data_min_k3, mahisa_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_mahisa = mahisa_k3
    
    ui_k3 = int(100 * ((cout_k3_mahisa - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari mahisa\t\t: {hitung_ui_k3_mahisa(data_max_k3, data_min_k3, mahisa_k3)}")

# calculate for k4
def hitung_ui_k4_mahisa(data_max_k4, data_min_k4, mahisa_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_mahisa = mahisa_k4
    
    ui_k4 = int(100 * ((cout_k4_mahisa - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari mahisa\t\t: {hitung_ui_k4_mahisa(data_max_k4, data_min_k4, mahisa_k4)}")

# calculate for k5
def hitung_ui_k5_mahisa(data_max_k5, data_min_k5, mahisa_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_mahisa = mahisa_k5
    
    ui_k5 = int(100 * ((cout_k5_mahisa - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari mahisa\t\t: {hitung_ui_k5_mahisa(data_max_k5, data_min_k5, mahisa_k5)}")

# calculate for k6
def hitung_ui_k6_mahisa(data_max_k6, data_min_k6, mahisa_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_mahisa = mahisa_k6
    
    ui_k6 = int(100 * ((cout_k6_mahisa - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari mahisa\t\t: {hitung_ui_k6_mahisa(data_max_k6, data_min_k6, mahisa_k6)}")

# calculate for k7
def hitung_ui_k7_mahisa(data_max_k7, data_min_k7, mahisa_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_mahisa = mahisa_k7
    
    ui_k7 = int(100 * ((cout_k7_mahisa - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari mahisa\t\t: {hitung_ui_k7_mahisa(data_max_k7, data_min_k7, mahisa_k7)}")

# calculate for k8
def hitung_ui_k8_mahisa(data_max_k8, data_min_k8, mahisa_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_mahisa = mahisa_k8
    
    ui_k8 = int(100 * ((cout_k8_mahisa - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari mahisa\t\t: {hitung_ui_k8_mahisa(data_max_k8, data_min_k8, mahisa_k8)}")

# calculate for k9
def hitung_ui_k9_mahisa(data_max_k9, data_min_k9, mahisa_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_mahisa = mahisa_k9
    
    ui_k9 = int(100 * ((cout_k9_mahisa - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari mahisa\t\t: {hitung_ui_k9_mahisa(data_max_k9, data_min_k9, mahisa_k9)}")

# calculate for k10
def hitung_ui_k10_mahisa(data_max_k10, data_min_k10, mahisa_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_mahisa = mahisa_k10
    
    ui_k10 = int(100 * ((cout_k10_mahisa - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari mahisa\t\t: {hitung_ui_k10_mahisa(data_max_k10, data_min_k10, mahisa_k10)}")

# calculate for k11
def hitung_ui_k11_mahisa(data_max_k11, data_min_k11, mahisa_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_mahisa = mahisa_k11
    
    ui_k11 = int(100 * ((cout_k11_mahisa - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari mahisa\t\t: {hitung_ui_k11_mahisa(data_max_k11, data_min_k11, mahisa_k11)}")

# calculate for k12
def hitung_ui_k12_mahisa(data_max_k12, data_min_k12, mahisa_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_mahisa = mahisa_k12
    
    ui_k12 = int(100 * ((cout_k12_mahisa - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari mahisa\t\t: {hitung_ui_k12_mahisa(data_max_k12, data_min_k12, mahisa_k12)}")

# calculate for k13
def hitung_ui_k13_mahisa(data_max_k13, data_min_k13, mahisa_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_mahisa = mahisa_k13
    
    ui_k13 = int(100 * ((cout_k13_mahisa - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari mahisa\t\t: {hitung_ui_k13_mahisa(data_max_k13, data_min_k13, mahisa_k13)}")

# rumus statistika untuk tari

# calculate for k1
def hitung_ui_k1_tari(data_max_k1, data_min_k1, tari_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_tari = tari_k1
    
    ui_k1 = int(100 * ((cout_k1_tari - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari tari\t\t: {hitung_ui_k1_tari(data_max_k1, data_min_k1, tari_k1)}")

# calculate for k2
def hitung_ui_k2_tari(data_max_k2, data_min_k2, tari_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_tari = tari_k2
    
    ui_k2 = int(100 * ((cout_k2_tari - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari tari\t\t: {hitung_ui_k2_tari(data_max_k2, data_min_k2, tari_k2)}")

# calculate for k3
def hitung_ui_k3_tari(data_max_k3, data_min_k3, tari_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_tari = tari_k3
    
    ui_k3 = int(100 * ((cout_k3_tari - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari tari\t\t: {hitung_ui_k3_tari(data_max_k3, data_min_k3, tari_k3)}")

# calculate for k4
def hitung_ui_k4_tari(data_max_k4, data_min_k4, tari_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_tari = tari_k4
    
    ui_k4 = int(100 * ((cout_k4_tari - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari tari\t\t: {hitung_ui_k4_tari(data_max_k4, data_min_k4, tari_k4)}")

# calculate for k5
def hitung_ui_k5_tari(data_max_k5, data_min_k5, tari_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_tari = tari_k5
    
    ui_k5 = int(100 * ((cout_k5_tari - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari tari\t\t: {hitung_ui_k5_tari(data_max_k5, data_min_k5, tari_k5)}")

# calculate for k6
def hitung_ui_k6_tari(data_max_k6, data_min_k6, tari_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_tari = tari_k6
    
    ui_k6 = int(100 * ((cout_k6_tari - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari tari\t\t: {hitung_ui_k6_tari(data_max_k6, data_min_k6, tari_k6)}")

# calculate for k7
def hitung_ui_k7_tari(data_max_k7, data_min_k7, tari_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_tari = tari_k7
    
    ui_k7 = int(100 * ((cout_k7_tari - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari tari\t\t: {hitung_ui_k7_tari(data_max_k7, data_min_k7, tari_k7)}")

# calculate for k8
def hitung_ui_k8_tari(data_max_k8, data_min_k8, tari_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_tari = tari_k8
    
    ui_k8 = int(100 * ((cout_k8_tari - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari tari\t\t: {hitung_ui_k8_tari(data_max_k8, data_min_k8, tari_k8)}")

# calculate for k9
def hitung_ui_k9_tari(data_max_k9, data_min_k9, tari_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_tari = tari_k9
    
    ui_k9 = int(100 * ((cout_k9_tari - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari tari\t\t: {hitung_ui_k9_tari(data_max_k9, data_min_k9, tari_k9)}")

# calculate for k10
def hitung_ui_k10_tari(data_max_k10, data_min_k10, tari_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_tari = tari_k10
    
    ui_k10 = int(100 * ((cout_k10_tari - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari tari\t\t: {hitung_ui_k10_tari(data_max_k10, data_min_k10, tari_k10)}")

# calculate for k11
def hitung_ui_k11_tari(data_max_k11, data_min_k11, tari_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_tari = tari_k11
    
    ui_k11 = int(100 * ((cout_k11_tari - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari tari\t\t: {hitung_ui_k11_tari(data_max_k11, data_min_k11, tari_k11)}")

# calculate for k12
def hitung_ui_k12_tari(data_max_k12, data_min_k12, tari_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_tari = tari_k12
    
    ui_k12 = int(100 * ((cout_k12_tari - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari tari\t\t: {hitung_ui_k12_tari(data_max_k12, data_min_k12, tari_k12)}")

# calculate for k13
def hitung_ui_k13_tari(data_max_k13, data_min_k13, tari_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_tari = tari_k13
    
    ui_k13 = int(100 * ((cout_k13_tari - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari tari\t\t: {hitung_ui_k13_tari(data_max_k13, data_min_k13, tari_k13)}")

# rumus statistika untuk fanny

# calculate for k1
def hitung_ui_k1_fanny(data_max_k1, data_min_k1, fanny_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_fanny = fanny_k1
    
    ui_k1 = int(100 * ((cout_k1_fanny - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari fanny\t\t: {hitung_ui_k1_fanny(data_max_k1, data_min_k1, fanny_k1)}")

# calculate for k2
def hitung_ui_k2_fanny(data_max_k2, data_min_k2, fanny_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_fanny = fanny_k2
    
    ui_k2 = int(100 * ((cout_k2_fanny - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari fanny\t\t: {hitung_ui_k2_fanny(data_max_k2, data_min_k2, fanny_k2)}")

# calculate for k3
def hitung_ui_k3_fanny(data_max_k3, data_min_k3, fanny_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_fanny = fanny_k3
    
    ui_k3 = int(100 * ((cout_k3_fanny - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari fanny\t\t: {hitung_ui_k3_fanny(data_max_k3, data_min_k3, fanny_k3)}")

# calculate for k4
def hitung_ui_k4_fanny(data_max_k4, data_min_k4, fanny_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_fanny = fanny_k4
    
    ui_k4 = int(100 * ((cout_k4_fanny - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari fanny\t\t: {hitung_ui_k4_fanny(data_max_k4, data_min_k4, fanny_k4)}")

# calculate for k5
def hitung_ui_k5_fanny(data_max_k5, data_min_k5, fanny_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_fanny = fanny_k5
    
    ui_k5 = int(100 * ((cout_k5_fanny - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari fanny\t\t: {hitung_ui_k5_fanny(data_max_k5, data_min_k5, fanny_k5)}")

# calculate for k6
def hitung_ui_k6_fanny(data_max_k6, data_min_k6, fanny_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_fanny = fanny_k6
    
    ui_k6 = int(100 * ((cout_k6_fanny - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari fanny\t\t: {hitung_ui_k6_fanny(data_max_k6, data_min_k6, fanny_k6)}")

# calculate for k7
def hitung_ui_k7_fanny(data_max_k7, data_min_k7, fanny_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_fanny = fanny_k7
    
    ui_k7 = int(100 * ((cout_k7_fanny - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari fanny\t\t: {hitung_ui_k7_fanny(data_max_k7, data_min_k7, fanny_k7)}")

# calculate for k8
def hitung_ui_k8_fanny(data_max_k8, data_min_k8, fanny_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_fanny = fanny_k8
    
    ui_k8 = int(100 * ((cout_k8_fanny - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari fanny\t\t: {hitung_ui_k8_fanny(data_max_k8, data_min_k8, fanny_k8)}")

# calculate for k9
def hitung_ui_k9_fanny(data_max_k9, data_min_k9, fanny_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_fanny = fanny_k9
    
    ui_k9 = int(100 * ((cout_k9_fanny - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari fanny\t\t: {hitung_ui_k9_fanny(data_max_k9, data_min_k9, fanny_k9)}")

# calculate for k10
def hitung_ui_k10_fanny(data_max_k10, data_min_k10, fanny_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_fanny = fanny_k10
    
    ui_k10 = int(100 * ((cout_k10_fanny - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari fanny\t\t: {hitung_ui_k10_fanny(data_max_k10, data_min_k10, fanny_k10)}")

# calculate for k11
def hitung_ui_k11_fanny(data_max_k11, data_min_k11, fanny_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_fanny = fanny_k11
    
    ui_k11 = int(100 * ((cout_k11_fanny - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari fanny\t\t: {hitung_ui_k11_fanny(data_max_k11, data_min_k11, fanny_k11)}")

# calculate for k12
def hitung_ui_k12_fanny(data_max_k12, data_min_k12, fanny_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_fanny = fanny_k12
    
    ui_k12 = int(100 * ((cout_k12_fanny - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari fanny\t\t: {hitung_ui_k12_fanny(data_max_k12, data_min_k12, fanny_k12)}")

# calculate for k13
def hitung_ui_k13_fanny(data_max_k13, data_min_k13, fanny_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_fanny = fanny_k13
    
    ui_k13 = int(100 * ((cout_k13_fanny - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari fanny\t\t: {hitung_ui_k13_fanny(data_max_k13, data_min_k13, fanny_k13)}")

# rumus statistika untuk fathan

# calculate for k1
def hitung_ui_k1_fathan(data_max_k1, data_min_k1, fathan_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_fathan = fathan_k1
    
    ui_k1 = int(100 * ((cout_k1_fathan - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari fathan\t\t: {hitung_ui_k1_fathan(data_max_k1, data_min_k1, fathan_k1)}")

# calculate for k2
def hitung_ui_k2_fathan(data_max_k2, data_min_k2, fathan_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_fathan = fathan_k2
    
    ui_k2 = int(100 * ((cout_k2_fathan - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari fathan\t\t: {hitung_ui_k2_fathan(data_max_k2, data_min_k2, fathan_k2)}")

# calculate for k3
def hitung_ui_k3_fathan(data_max_k3, data_min_k3, fathan_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_fathan = fathan_k3
    
    ui_k3 = int(100 * ((cout_k3_fathan - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari fathan\t\t: {hitung_ui_k3_fathan(data_max_k3, data_min_k3, fathan_k3)}")

# calculate for k4
def hitung_ui_k4_fathan(data_max_k4, data_min_k4, fathan_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_fathan = fathan_k4
    
    ui_k4 = int(100 * ((cout_k4_fathan - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari fathan\t\t: {hitung_ui_k4_fathan(data_max_k4, data_min_k4, fathan_k4)}")

# calculate for k5
def hitung_ui_k5_fathan(data_max_k5, data_min_k5, fathan_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_fathan = fathan_k5
    
    ui_k5 = int(100 * ((cout_k5_fathan - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari fathan\t\t: {hitung_ui_k5_fathan(data_max_k5, data_min_k5, fathan_k5)}")

# calculate for k6
def hitung_ui_k6_fathan(data_max_k6, data_min_k6, fathan_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_fathan = fathan_k6
    
    ui_k6 = int(100 * ((cout_k6_fathan - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari fathan\t\t: {hitung_ui_k6_fathan(data_max_k6, data_min_k6, fathan_k6)}")

# calculate for k7
def hitung_ui_k7_fathan(data_max_k7, data_min_k7, fathan_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_fathan = fathan_k7
    
    ui_k7 = int(100 * ((cout_k7_fathan - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari fathan\t\t: {hitung_ui_k7_fathan(data_max_k7, data_min_k7, fathan_k7)}")

# calculate for k8
def hitung_ui_k8_fathan(data_max_k8, data_min_k8, fathan_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_fathan = fathan_k8
    
    ui_k8 = int(100 * ((cout_k8_fathan - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari fathan\t\t: {hitung_ui_k8_fathan(data_max_k8, data_min_k8, fathan_k8)}")

# calculate for k9
def hitung_ui_k9_fathan(data_max_k9, data_min_k9, fathan_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_fathan = fathan_k9
    
    ui_k9 = int(100 * ((cout_k9_fathan - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari fathan\t\t: {hitung_ui_k9_fathan(data_max_k9, data_min_k9, fathan_k9)}")

# calculate for k10
def hitung_ui_k10_fathan(data_max_k10, data_min_k10, fathan_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_fathan = fathan_k10
    
    ui_k10 = int(100 * ((cout_k10_fathan - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari fathan\t\t: {hitung_ui_k10_fathan(data_max_k10, data_min_k10, fathan_k10)}")

# calculate for k11
def hitung_ui_k11_fathan(data_max_k11, data_min_k11, fathan_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_fathan = fathan_k11
    
    ui_k11 = int(100 * ((cout_k11_fathan - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari fathan\t\t: {hitung_ui_k11_fathan(data_max_k11, data_min_k11, fathan_k11)}")

# calculate for k12
def hitung_ui_k12_fathan(data_max_k12, data_min_k12, fathan_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_fathan = fathan_k12
    
    ui_k12 = int(100 * ((cout_k12_fathan - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari fathan\t\t: {hitung_ui_k12_fathan(data_max_k12, data_min_k12, fathan_k12)}")

# calculate for k13
def hitung_ui_k13_fathan(data_max_k13, data_min_k13, fathan_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_fathan = fathan_k13
    
    ui_k13 = int(100 * ((cout_k13_fathan - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari fathan\t\t: {hitung_ui_k13_fathan(data_max_k13, data_min_k13, fathan_k13)}")

# rumus statistika untuk sindika

# calculate for k1
def hitung_ui_k1_sindika(data_max_k1, data_min_k1, sindika_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_sindika = sindika_k1
    
    ui_k1 = int(100 * ((cout_k1_sindika - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari sindika\t\t: {hitung_ui_k1_sindika(data_max_k1, data_min_k1, sindika_k1)}")

# calculate for k2
def hitung_ui_k2_sindika(data_max_k2, data_min_k2, sindika_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_sindika = sindika_k2
    
    ui_k2 = int(100 * ((cout_k2_sindika - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari sindika\t\t: {hitung_ui_k2_sindika(data_max_k2, data_min_k2, sindika_k2)}")

# calculate for k3
def hitung_ui_k3_sindika(data_max_k3, data_min_k3, sindika_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_sindika = sindika_k3
    
    ui_k3 = int(100 * ((cout_k3_sindika - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari sindika\t\t: {hitung_ui_k3_sindika(data_max_k3, data_min_k3, sindika_k3)}")

# calculate for k4
def hitung_ui_k4_sindika(data_max_k4, data_min_k4, sindika_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_sindika = sindika_k4
    
    ui_k4 = int(100 * ((cout_k4_sindika - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari sindika\t\t: {hitung_ui_k4_sindika(data_max_k4, data_min_k4, sindika_k4)}")

# calculate for k5
def hitung_ui_k5_sindika(data_max_k5, data_min_k5, sindika_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_sindika = sindika_k5
    
    ui_k5 = int(100 * ((cout_k5_sindika - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari sindika\t\t: {hitung_ui_k5_sindika(data_max_k5, data_min_k5, sindika_k5)}")

# calculate for k6
def hitung_ui_k6_sindika(data_max_k6, data_min_k6, sindika_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_sindika = sindika_k6
    
    ui_k6 = int(100 * ((cout_k6_sindika - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari sindika\t\t: {hitung_ui_k6_sindika(data_max_k6, data_min_k6, sindika_k6)}")

# calculate for k7
def hitung_ui_k7_sindika(data_max_k7, data_min_k7, sindika_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_sindika = sindika_k7
    
    ui_k7 = int(100 * ((cout_k7_sindika - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari sindika\t\t: {hitung_ui_k7_sindika(data_max_k7, data_min_k7, sindika_k7)}")

# calculate for k8
def hitung_ui_k8_sindika(data_max_k8, data_min_k8, sindika_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_sindika = sindika_k8
    
    ui_k8 = int(100 * ((cout_k8_sindika - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari sindika\t\t: {hitung_ui_k8_sindika(data_max_k8, data_min_k8, sindika_k8)}")

# calculate for k9
def hitung_ui_k9_sindika(data_max_k9, data_min_k9, sindika_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_sindika = sindika_k9
    
    ui_k9 = int(100 * ((cout_k9_sindika - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari sindika\t\t: {hitung_ui_k9_sindika(data_max_k9, data_min_k9, sindika_k9)}")

# calculate for k10
def hitung_ui_k10_sindika(data_max_k10, data_min_k10, sindika_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_sindika = sindika_k10
    
    ui_k10 = int(100 * ((cout_k10_sindika - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari sindika\t\t: {hitung_ui_k10_sindika(data_max_k10, data_min_k10, sindika_k10)}")

# calculate for k11
def hitung_ui_k11_sindika(data_max_k11, data_min_k11, sindika_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_sindika = sindika_k11
    
    ui_k11 = int(100 * ((cout_k11_sindika - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari sindika\t\t: {hitung_ui_k11_sindika(data_max_k11, data_min_k11, sindika_k11)}")

# calculate for k12
def hitung_ui_k12_sindika(data_max_k12, data_min_k12, sindika_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_sindika = sindika_k12
    
    ui_k12 = int(100 * ((cout_k12_sindika - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari sindika\t\t: {hitung_ui_k12_sindika(data_max_k12, data_min_k12, sindika_k12)}")

# calculate for k13
def hitung_ui_k13_sindika(data_max_k13, data_min_k13, sindika_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_sindika = sindika_k13
    
    ui_k13 = int(100 * ((cout_k13_sindika - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari sindika\t\t: {hitung_ui_k13_sindika(data_max_k13, data_min_k13, sindika_k13)}")

# rumus statistika untuk aryawildan

# calculate for k1
def hitung_ui_k1_aryawildan(data_max_k1, data_min_k1, aryawildan_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_aryawildan = aryawildan_k1
    
    ui_k1 = int(100 * ((cout_k1_aryawildan - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari aryawildan\t\t: {hitung_ui_k1_aryawildan(data_max_k1, data_min_k1, aryawildan_k1)}")

# calculate for k2
def hitung_ui_k2_aryawildan(data_max_k2, data_min_k2, aryawildan_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_aryawildan = aryawildan_k2
    
    ui_k2 = int(100 * ((cout_k2_aryawildan - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari aryawildan\t\t: {hitung_ui_k2_aryawildan(data_max_k2, data_min_k2, aryawildan_k2)}")

# calculate for k3
def hitung_ui_k3_aryawildan(data_max_k3, data_min_k3, aryawildan_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_aryawildan = aryawildan_k3
    
    ui_k3 = int(100 * ((cout_k3_aryawildan - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari aryawildan\t\t: {hitung_ui_k3_aryawildan(data_max_k3, data_min_k3, aryawildan_k3)}")

# calculate for k4
def hitung_ui_k4_aryawildan(data_max_k4, data_min_k4, aryawildan_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_aryawildan = aryawildan_k4
    
    ui_k4 = int(100 * ((cout_k4_aryawildan - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari aryawildan\t\t: {hitung_ui_k4_aryawildan(data_max_k4, data_min_k4, aryawildan_k4)}")

# calculate for k5
def hitung_ui_k5_aryawildan(data_max_k5, data_min_k5, aryawildan_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_aryawildan = aryawildan_k5
    
    ui_k5 = int(100 * ((cout_k5_aryawildan - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari aryawildan\t\t: {hitung_ui_k5_aryawildan(data_max_k5, data_min_k5, aryawildan_k5)}")

# calculate for k6
def hitung_ui_k6_aryawildan(data_max_k6, data_min_k6, aryawildan_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_aryawildan = aryawildan_k6
    
    ui_k6 = int(100 * ((cout_k6_aryawildan - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari aryawildan\t\t: {hitung_ui_k6_aryawildan(data_max_k6, data_min_k6, aryawildan_k6)}")

# calculate for k7
def hitung_ui_k7_aryawildan(data_max_k7, data_min_k7, aryawildan_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_aryawildan = aryawildan_k7
    
    ui_k7 = int(100 * ((cout_k7_aryawildan - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari aryawildan\t\t: {hitung_ui_k7_aryawildan(data_max_k7, data_min_k7, aryawildan_k7)}")

# calculate for k8
def hitung_ui_k8_aryawildan(data_max_k8, data_min_k8, aryawildan_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_aryawildan = aryawildan_k8
    
    ui_k8 = int(100 * ((cout_k8_aryawildan - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari aryawildan\t\t: {hitung_ui_k8_aryawildan(data_max_k8, data_min_k8, aryawildan_k8)}")

# calculate for k9
def hitung_ui_k9_aryawildan(data_max_k9, data_min_k9, aryawildan_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_aryawildan = aryawildan_k9
    
    ui_k9 = int(100 * ((cout_k9_aryawildan - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari aryawildan\t\t: {hitung_ui_k9_aryawildan(data_max_k9, data_min_k9, aryawildan_k9)}")

# calculate for k10
def hitung_ui_k10_aryawildan(data_max_k10, data_min_k10, aryawildan_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_aryawildan = aryawildan_k10
    
    ui_k10 = int(100 * ((cout_k10_aryawildan - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari aryawildan\t\t: {hitung_ui_k10_aryawildan(data_max_k10, data_min_k10, aryawildan_k10)}")

# calculate for k11
def hitung_ui_k11_aryawildan(data_max_k11, data_min_k11, aryawildan_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_aryawildan = aryawildan_k11
    
    ui_k11 = int(100 * ((cout_k11_aryawildan - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari aryawildan\t\t: {hitung_ui_k11_aryawildan(data_max_k11, data_min_k11, aryawildan_k11)}")

# calculate for k12
def hitung_ui_k12_aryawildan(data_max_k12, data_min_k12, aryawildan_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_aryawildan = aryawildan_k12
    
    ui_k12 = int(100 * ((cout_k12_aryawildan - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari aryawildan\t\t: {hitung_ui_k12_aryawildan(data_max_k12, data_min_k12, aryawildan_k12)}")

# calculate for k13
def hitung_ui_k13_aryawildan(data_max_k13, data_min_k13, aryawildan_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_aryawildan = aryawildan_k13
    
    ui_k13 = int(100 * ((cout_k13_aryawildan - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari aryawildan\t\t: {hitung_ui_k13_aryawildan(data_max_k13, data_min_k13, aryawildan_k13)}")

# rumus statistika untuk icha

# calculate for k1
def hitung_ui_k1_icha(data_max_k1, data_min_k1, icha_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_icha = icha_k1
    
    ui_k1 = int(100 * ((cout_k1_icha - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari icha\t\t: {hitung_ui_k1_icha(data_max_k1, data_min_k1, icha_k1)}")

# calculate for k2
def hitung_ui_k2_icha(data_max_k2, data_min_k2, icha_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_icha = icha_k2
    
    ui_k2 = int(100 * ((cout_k2_icha - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari icha\t\t: {hitung_ui_k2_icha(data_max_k2, data_min_k2, icha_k2)}")

# calculate for k3
def hitung_ui_k3_icha(data_max_k3, data_min_k3, icha_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_icha = icha_k3
    
    ui_k3 = int(100 * ((cout_k3_icha - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari icha\t\t: {hitung_ui_k3_icha(data_max_k3, data_min_k3, icha_k3)}")

# calculate for k4
def hitung_ui_k4_icha(data_max_k4, data_min_k4, icha_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_icha = icha_k4
    
    ui_k4 = int(100 * ((cout_k4_icha - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari icha\t\t: {hitung_ui_k4_icha(data_max_k4, data_min_k4, icha_k4)}")

# calculate for k5
def hitung_ui_k5_icha(data_max_k5, data_min_k5, icha_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_icha = icha_k5
    
    ui_k5 = int(100 * ((cout_k5_icha - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari icha\t\t: {hitung_ui_k5_icha(data_max_k5, data_min_k5, icha_k5)}")

# calculate for k6
def hitung_ui_k6_icha(data_max_k6, data_min_k6, icha_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_icha = icha_k6
    
    ui_k6 = int(100 * ((cout_k6_icha - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari icha\t\t: {hitung_ui_k6_icha(data_max_k6, data_min_k6, icha_k6)}")

# calculate for k7
def hitung_ui_k7_icha(data_max_k7, data_min_k7, icha_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_icha = icha_k7
    
    ui_k7 = int(100 * ((cout_k7_icha - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari icha\t\t: {hitung_ui_k7_icha(data_max_k7, data_min_k7, icha_k7)}")

# calculate for k8
def hitung_ui_k8_icha(data_max_k8, data_min_k8, icha_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_icha = icha_k8
    
    ui_k8 = int(100 * ((cout_k8_icha - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari icha\t\t: {hitung_ui_k8_icha(data_max_k8, data_min_k8, icha_k8)}")

# calculate for k9
def hitung_ui_k9_icha(data_max_k9, data_min_k9, icha_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_icha = icha_k9
    
    ui_k9 = int(100 * ((cout_k9_icha - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari icha\t\t: {hitung_ui_k9_icha(data_max_k9, data_min_k9, icha_k9)}")

# calculate for k10
def hitung_ui_k10_icha(data_max_k10, data_min_k10, icha_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_icha = icha_k10
    
    ui_k10 = int(100 * ((cout_k10_icha - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari icha\t\t: {hitung_ui_k10_icha(data_max_k10, data_min_k10, icha_k10)}")

# calculate for k11
def hitung_ui_k11_icha(data_max_k11, data_min_k11, icha_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_icha = icha_k11
    
    ui_k11 = int(100 * ((cout_k11_icha - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari icha\t\t: {hitung_ui_k11_icha(data_max_k11, data_min_k11, icha_k11)}")

# calculate for k12
def hitung_ui_k12_icha(data_max_k12, data_min_k12, icha_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_icha = icha_k12
    
    ui_k12 = int(100 * ((cout_k12_icha - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari icha\t\t: {hitung_ui_k12_icha(data_max_k12, data_min_k12, icha_k12)}")

# calculate for k13
def hitung_ui_k13_icha(data_max_k13, data_min_k13, icha_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_icha = icha_k13
    
    ui_k13 = int(100 * ((cout_k13_icha - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari icha\t\t: {hitung_ui_k13_icha(data_max_k13, data_min_k13, icha_k13)}")

# rumus statistika untuk nugroho

# calculate for k1
def hitung_ui_k1_nugroho(data_max_k1, data_min_k1, nugroho_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_nugroho = nugroho_k1
    
    ui_k1 = int(100 * ((cout_k1_nugroho - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari nugroho\t\t: {hitung_ui_k1_nugroho(data_max_k1, data_min_k1, nugroho_k1)}")

# calculate for k2
def hitung_ui_k2_nugroho(data_max_k2, data_min_k2, nugroho_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_nugroho = nugroho_k2
    
    ui_k2 = int(100 * ((cout_k2_nugroho - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari nugroho\t\t: {hitung_ui_k2_nugroho(data_max_k2, data_min_k2, nugroho_k2)}")

# calculate for k3
def hitung_ui_k3_nugroho(data_max_k3, data_min_k3, nugroho_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_nugroho = nugroho_k3
    
    ui_k3 = int(100 * ((cout_k3_nugroho - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari nugroho\t\t: {hitung_ui_k3_nugroho(data_max_k3, data_min_k3, nugroho_k3)}")

# calculate for k4
def hitung_ui_k4_nugroho(data_max_k4, data_min_k4, nugroho_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_nugroho = nugroho_k4
    
    ui_k4 = int(100 * ((cout_k4_nugroho - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari nugroho\t\t: {hitung_ui_k4_nugroho(data_max_k4, data_min_k4, nugroho_k4)}")

# calculate for k5
def hitung_ui_k5_nugroho(data_max_k5, data_min_k5, nugroho_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_nugroho = nugroho_k5
    
    ui_k5 = int(100 * ((cout_k5_nugroho - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari nugroho\t\t: {hitung_ui_k5_nugroho(data_max_k5, data_min_k5, nugroho_k5)}")

# calculate for k6
def hitung_ui_k6_nugroho(data_max_k6, data_min_k6, nugroho_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_nugroho = nugroho_k6
    
    ui_k6 = int(100 * ((cout_k6_nugroho - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari nugroho\t\t: {hitung_ui_k6_nugroho(data_max_k6, data_min_k6, nugroho_k6)}")

# calculate for k7
def hitung_ui_k7_nugroho(data_max_k7, data_min_k7, nugroho_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_nugroho = nugroho_k7
    
    ui_k7 = int(100 * ((cout_k7_nugroho - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari nugroho\t\t: {hitung_ui_k7_nugroho(data_max_k7, data_min_k7, nugroho_k7)}")

# calculate for k8
def hitung_ui_k8_nugroho(data_max_k8, data_min_k8, nugroho_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_nugroho = nugroho_k8
    
    ui_k8 = int(100 * ((cout_k8_nugroho - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari nugroho\t\t: {hitung_ui_k8_nugroho(data_max_k8, data_min_k8, nugroho_k8)}")

# calculate for k9
def hitung_ui_k9_nugroho(data_max_k9, data_min_k9, nugroho_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_nugroho = nugroho_k9
    
    ui_k9 = int(100 * ((cout_k9_nugroho - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari nugroho\t\t: {hitung_ui_k9_nugroho(data_max_k9, data_min_k9, nugroho_k9)}")

# calculate for k10
def hitung_ui_k10_nugroho(data_max_k10, data_min_k10, nugroho_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_nugroho = nugroho_k10
    
    ui_k10 = int(100 * ((cout_k10_nugroho - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari nugroho\t\t: {hitung_ui_k10_nugroho(data_max_k10, data_min_k10, nugroho_k10)}")

# calculate for k11
def hitung_ui_k11_nugroho(data_max_k11, data_min_k11, nugroho_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_nugroho = nugroho_k11
    
    ui_k11 = int(100 * ((cout_k11_nugroho - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari nugroho\t\t: {hitung_ui_k11_nugroho(data_max_k11, data_min_k11, nugroho_k11)}")

# calculate for k12
def hitung_ui_k12_nugroho(data_max_k12, data_min_k12, nugroho_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_nugroho = nugroho_k12
    
    ui_k12 = int(100 * ((cout_k12_nugroho - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari nugroho\t\t: {hitung_ui_k12_nugroho(data_max_k12, data_min_k12, nugroho_k12)}")

# calculate for k13
def hitung_ui_k13_nugroho(data_max_k13, data_min_k13, nugroho_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_nugroho = nugroho_k13
    
    ui_k13 = int(100 * ((cout_k13_nugroho - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari nugroho\t\t: {hitung_ui_k13_nugroho(data_max_k13, data_min_k13, nugroho_k13)}")

# rumus statistika untuk adit

# calculate for k1
def hitung_ui_k1_adit(data_max_k1, data_min_k1, adit_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_adit = adit_k1
    
    ui_k1 = int(100 * ((cout_k1_adit - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari adit\t\t: {hitung_ui_k1_adit(data_max_k1, data_min_k1, adit_k1)}")

# calculate for k2
def hitung_ui_k2_adit(data_max_k2, data_min_k2, adit_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_adit = adit_k2
    
    ui_k2 = int(100 * ((cout_k2_adit - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari adit\t\t: {hitung_ui_k2_adit(data_max_k2, data_min_k2, adit_k2)}")

# calculate for k3
def hitung_ui_k3_adit(data_max_k3, data_min_k3, adit_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_adit = adit_k3
    
    ui_k3 = int(100 * ((cout_k3_adit - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari adit\t\t: {hitung_ui_k3_adit(data_max_k3, data_min_k3, adit_k3)}")

# calculate for k4
def hitung_ui_k4_adit(data_max_k4, data_min_k4, adit_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_adit = adit_k4
    
    ui_k4 = int(100 * ((cout_k4_adit - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari adit\t\t: {hitung_ui_k4_adit(data_max_k4, data_min_k4, adit_k4)}")

# calculate for k5
def hitung_ui_k5_adit(data_max_k5, data_min_k5, adit_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_adit = adit_k5
    
    ui_k5 = int(100 * ((cout_k5_adit - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari adit\t\t: {hitung_ui_k5_adit(data_max_k5, data_min_k5, adit_k5)}")

# calculate for k6
def hitung_ui_k6_adit(data_max_k6, data_min_k6, adit_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_adit = adit_k6
    
    ui_k6 = int(100 * ((cout_k6_adit - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari adit\t\t: {hitung_ui_k6_adit(data_max_k6, data_min_k6, adit_k6)}")

# calculate for k7
def hitung_ui_k7_adit(data_max_k7, data_min_k7, adit_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_adit = adit_k7
    
    ui_k7 = int(100 * ((cout_k7_adit - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari adit\t\t: {hitung_ui_k7_adit(data_max_k7, data_min_k7, adit_k7)}")

# calculate for k8
def hitung_ui_k8_adit(data_max_k8, data_min_k8, adit_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_adit = adit_k8
    
    ui_k8 = int(100 * ((cout_k8_adit - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari adit\t\t: {hitung_ui_k8_adit(data_max_k8, data_min_k8, adit_k8)}")

# calculate for k9
def hitung_ui_k9_adit(data_max_k9, data_min_k9, adit_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_adit = adit_k9
    
    ui_k9 = int(100 * ((cout_k9_adit - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari adit\t\t: {hitung_ui_k9_adit(data_max_k9, data_min_k9, adit_k9)}")

# calculate for k10
def hitung_ui_k10_adit(data_max_k10, data_min_k10, adit_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_adit = adit_k10
    
    ui_k10 = int(100 * ((cout_k10_adit - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari adit\t\t: {hitung_ui_k10_adit(data_max_k10, data_min_k10, adit_k10)}")

# calculate for k11
def hitung_ui_k11_adit(data_max_k11, data_min_k11, adit_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_adit = adit_k11
    
    ui_k11 = int(100 * ((cout_k11_adit - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari adit\t\t: {hitung_ui_k11_adit(data_max_k11, data_min_k11, adit_k11)}")

# calculate for k12
def hitung_ui_k12_adit(data_max_k12, data_min_k12, adit_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_adit = adit_k12
    
    ui_k12 = int(100 * ((cout_k12_adit - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari adit\t\t: {hitung_ui_k12_adit(data_max_k12, data_min_k12, adit_k12)}")

# calculate for k13
def hitung_ui_k13_adit(data_max_k13, data_min_k13, adit_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_adit = adit_k13
    
    ui_k13 = int(100 * ((cout_k13_adit - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari adit\t\t: {hitung_ui_k13_adit(data_max_k13, data_min_k13, adit_k13)}")

# rumus statistika untuk umam

# calculate for k1
def hitung_ui_k1_umam(data_max_k1, data_min_k1, umam_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_umam = umam_k1
    
    ui_k1 = int(100 * ((cout_k1_umam - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari umam\t\t: {hitung_ui_k1_umam(data_max_k1, data_min_k1, umam_k1)}")

# calculate for k2
def hitung_ui_k2_umam(data_max_k2, data_min_k2, umam_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_umam = umam_k2
    
    ui_k2 = int(100 * ((cout_k2_umam - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari umam\t\t: {hitung_ui_k2_umam(data_max_k2, data_min_k2, umam_k2)}")

# calculate for k3
def hitung_ui_k3_umam(data_max_k3, data_min_k3, umam_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_umam = umam_k3
    
    ui_k3 = int(100 * ((cout_k3_umam - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari umam\t\t: {hitung_ui_k3_umam(data_max_k3, data_min_k3, umam_k3)}")

# calculate for k4
def hitung_ui_k4_umam(data_max_k4, data_min_k4, umam_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_umam = umam_k4
    
    ui_k4 = int(100 * ((cout_k4_umam - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari umam\t\t: {hitung_ui_k4_umam(data_max_k4, data_min_k4, umam_k4)}")

# calculate for k5
def hitung_ui_k5_umam(data_max_k5, data_min_k5, umam_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_umam = umam_k5
    
    ui_k5 = int(100 * ((cout_k5_umam - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari umam\t\t: {hitung_ui_k5_umam(data_max_k5, data_min_k5, umam_k5)}")

# calculate for k6
def hitung_ui_k6_umam(data_max_k6, data_min_k6, umam_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_umam = umam_k6
    
    ui_k6 = int(100 * ((cout_k6_umam - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari umam\t\t: {hitung_ui_k6_umam(data_max_k6, data_min_k6, umam_k6)}")

# calculate for k7
def hitung_ui_k7_umam(data_max_k7, data_min_k7, umam_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_umam = umam_k7
    
    ui_k7 = int(100 * ((cout_k7_umam - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari umam\t\t: {hitung_ui_k7_umam(data_max_k7, data_min_k7, umam_k7)}")

# calculate for k8
def hitung_ui_k8_umam(data_max_k8, data_min_k8, umam_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_umam = umam_k8
    
    ui_k8 = int(100 * ((cout_k8_umam - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari umam\t\t: {hitung_ui_k8_umam(data_max_k8, data_min_k8, umam_k8)}")

# calculate for k9
def hitung_ui_k9_umam(data_max_k9, data_min_k9, umam_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_umam = umam_k9
    
    ui_k9 = int(100 * ((cout_k9_umam - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari umam\t\t: {hitung_ui_k9_umam(data_max_k9, data_min_k9, umam_k9)}")

# calculate for k10
def hitung_ui_k10_umam(data_max_k10, data_min_k10, umam_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_umam = umam_k10
    
    ui_k10 = int(100 * ((cout_k10_umam - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari umam\t\t: {hitung_ui_k10_umam(data_max_k10, data_min_k10, umam_k10)}")

# calculate for k11
def hitung_ui_k11_umam(data_max_k11, data_min_k11, umam_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_umam = umam_k11
    
    ui_k11 = int(100 * ((cout_k11_umam - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari umam\t\t: {hitung_ui_k11_umam(data_max_k11, data_min_k11, umam_k11)}")

# calculate for k12
def hitung_ui_k12_umam(data_max_k12, data_min_k12, umam_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_umam = umam_k12
    
    ui_k12 = int(100 * ((cout_k12_umam - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari umam\t\t: {hitung_ui_k12_umam(data_max_k12, data_min_k12, umam_k12)}")

# calculate for k13
def hitung_ui_k13_umam(data_max_k13, data_min_k13, umam_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_umam = umam_k13
    
    ui_k13 = int(100 * ((cout_k13_umam - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari umam\t\t: {hitung_ui_k13_umam(data_max_k13, data_min_k13, umam_k13)}")

# rumus statistika untuk nana

# calculate for k1
def hitung_ui_k1_nana(data_max_k1, data_min_k1, nana_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_nana = nana_k1
    
    ui_k1 = int(100 * ((cout_k1_nana - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari nana\t\t: {hitung_ui_k1_nana(data_max_k1, data_min_k1, nana_k1)}")

# calculate for k2
def hitung_ui_k2_nana(data_max_k2, data_min_k2, nana_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_nana = nana_k2
    
    ui_k2 = int(100 * ((cout_k2_nana - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari nana\t\t: {hitung_ui_k2_nana(data_max_k2, data_min_k2, nana_k2)}")

# calculate for k3
def hitung_ui_k3_nana(data_max_k3, data_min_k3, nana_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_nana = nana_k3
    
    ui_k3 = int(100 * ((cout_k3_nana - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari nana\t\t: {hitung_ui_k3_nana(data_max_k3, data_min_k3, nana_k3)}")

# calculate for k4
def hitung_ui_k4_nana(data_max_k4, data_min_k4, nana_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_nana = nana_k4
    
    ui_k4 = int(100 * ((cout_k4_nana - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari nana\t\t: {hitung_ui_k4_nana(data_max_k4, data_min_k4, nana_k4)}")

# calculate for k5
def hitung_ui_k5_nana(data_max_k5, data_min_k5, nana_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_nana = nana_k5
    
    ui_k5 = int(100 * ((cout_k5_nana - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari nana\t\t: {hitung_ui_k5_nana(data_max_k5, data_min_k5, nana_k5)}")

# calculate for k6
def hitung_ui_k6_nana(data_max_k6, data_min_k6, nana_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_nana = nana_k6
    
    ui_k6 = int(100 * ((cout_k6_nana - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari nana\t\t: {hitung_ui_k6_nana(data_max_k6, data_min_k6, nana_k6)}")

# calculate for k7
def hitung_ui_k7_nana(data_max_k7, data_min_k7, nana_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_nana = nana_k7
    
    ui_k7 = int(100 * ((cout_k7_nana - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari nana\t\t: {hitung_ui_k7_nana(data_max_k7, data_min_k7, nana_k7)}")

# calculate for k8
def hitung_ui_k8_nana(data_max_k8, data_min_k8, nana_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_nana = nana_k8
    
    ui_k8 = int(100 * ((cout_k8_nana - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari nana\t\t: {hitung_ui_k8_nana(data_max_k8, data_min_k8, nana_k8)}")

# calculate for k9
def hitung_ui_k9_nana(data_max_k9, data_min_k9, nana_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_nana = nana_k9
    
    ui_k9 = int(100 * ((cout_k9_nana - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari nana\t\t: {hitung_ui_k9_nana(data_max_k9, data_min_k9, nana_k9)}")

# calculate for k10
def hitung_ui_k10_nana(data_max_k10, data_min_k10, nana_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_nana = nana_k10
    
    ui_k10 = int(100 * ((cout_k10_nana - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari nana\t\t: {hitung_ui_k10_nana(data_max_k10, data_min_k10, nana_k10)}")

# calculate for k11
def hitung_ui_k11_nana(data_max_k11, data_min_k11, nana_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_nana = nana_k11
    
    ui_k11 = int(100 * ((cout_k11_nana - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari nana\t\t: {hitung_ui_k11_nana(data_max_k11, data_min_k11, nana_k11)}")

# calculate for k12
def hitung_ui_k12_nana(data_max_k12, data_min_k12, nana_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_nana = nana_k12
    
    ui_k12 = int(100 * ((cout_k12_nana - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari nana\t\t: {hitung_ui_k12_nana(data_max_k12, data_min_k12, nana_k12)}")

# calculate for k13
def hitung_ui_k13_nana(data_max_k13, data_min_k13, nana_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_nana = nana_k13
    
    ui_k13 = int(100 * ((cout_k13_nana - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari nana\t\t: {hitung_ui_k13_nana(data_max_k13, data_min_k13, nana_k13)}")

# rumus statistika untuk syahrur

# calculate for k1
def hitung_ui_k1_syahrur(data_max_k1, data_min_k1, syahrur_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_syahrur = syahrur_k1
    
    ui_k1 = int(100 * ((cout_k1_syahrur - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari syahrur\t\t: {hitung_ui_k1_syahrur(data_max_k1, data_min_k1, syahrur_k1)}")

# calculate for k2
def hitung_ui_k2_syahrur(data_max_k2, data_min_k2, syahrur_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_syahrur = syahrur_k2
    
    ui_k2 = int(100 * ((cout_k2_syahrur - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari syahrur\t\t: {hitung_ui_k2_syahrur(data_max_k2, data_min_k2, syahrur_k2)}")

# calculate for k3
def hitung_ui_k3_syahrur(data_max_k3, data_min_k3, syahrur_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_syahrur = syahrur_k3
    
    ui_k3 = int(100 * ((cout_k3_syahrur - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari syahrur\t\t: {hitung_ui_k3_syahrur(data_max_k3, data_min_k3, syahrur_k3)}")

# calculate for k4
def hitung_ui_k4_syahrur(data_max_k4, data_min_k4, syahrur_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_syahrur = syahrur_k4
    
    ui_k4 = int(100 * ((cout_k4_syahrur - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari syahrur\t\t: {hitung_ui_k4_syahrur(data_max_k4, data_min_k4, syahrur_k4)}")

# calculate for k5
def hitung_ui_k5_syahrur(data_max_k5, data_min_k5, syahrur_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_syahrur = syahrur_k5
    
    ui_k5 = int(100 * ((cout_k5_syahrur - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari syahrur\t\t: {hitung_ui_k5_syahrur(data_max_k5, data_min_k5, syahrur_k5)}")

# calculate for k6
def hitung_ui_k6_syahrur(data_max_k6, data_min_k6, syahrur_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_syahrur = syahrur_k6
    
    ui_k6 = int(100 * ((cout_k6_syahrur - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari syahrur\t\t: {hitung_ui_k6_syahrur(data_max_k6, data_min_k6, syahrur_k6)}")

# calculate for k7
def hitung_ui_k7_syahrur(data_max_k7, data_min_k7, syahrur_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_syahrur = syahrur_k7
    
    ui_k7 = int(100 * ((cout_k7_syahrur - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari syahrur\t\t: {hitung_ui_k7_syahrur(data_max_k7, data_min_k7, syahrur_k7)}")

# calculate for k8
def hitung_ui_k8_syahrur(data_max_k8, data_min_k8, syahrur_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_syahrur = syahrur_k8
    
    ui_k8 = int(100 * ((cout_k8_syahrur - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari syahrur\t\t: {hitung_ui_k8_syahrur(data_max_k8, data_min_k8, syahrur_k8)}")

# calculate for k9
def hitung_ui_k9_syahrur(data_max_k9, data_min_k9, syahrur_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_syahrur = syahrur_k9
    
    ui_k9 = int(100 * ((cout_k9_syahrur - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari syahrur\t\t: {hitung_ui_k9_syahrur(data_max_k9, data_min_k9, syahrur_k9)}")

# calculate for k10
def hitung_ui_k10_syahrur(data_max_k10, data_min_k10, syahrur_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_syahrur = syahrur_k10
    
    ui_k10 = int(100 * ((cout_k10_syahrur - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari syahrur\t\t: {hitung_ui_k10_syahrur(data_max_k10, data_min_k10, syahrur_k10)}")

# calculate for k11
def hitung_ui_k11_syahrur(data_max_k11, data_min_k11, syahrur_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_syahrur = syahrur_k11
    
    ui_k11 = int(100 * ((cout_k11_syahrur - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari syahrur\t\t: {hitung_ui_k11_syahrur(data_max_k11, data_min_k11, syahrur_k11)}")

# calculate for k12
def hitung_ui_k12_syahrur(data_max_k12, data_min_k12, syahrur_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_syahrur = syahrur_k12
    
    ui_k12 = int(100 * ((cout_k12_syahrur - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari syahrur\t\t: {hitung_ui_k12_syahrur(data_max_k12, data_min_k12, syahrur_k12)}")

# calculate for k13
def hitung_ui_k13_syahrur(data_max_k13, data_min_k13, syahrur_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_syahrur = syahrur_k13
    
    ui_k13 = int(100 * ((cout_k13_syahrur - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari syahrur\t\t: {hitung_ui_k13_syahrur(data_max_k13, data_min_k13, syahrur_k13)}")

# rumus statistika untuk dewi

# calculate for k1
def hitung_ui_k1_dewi(data_max_k1, data_min_k1, dewi_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_dewi = dewi_k1
    
    ui_k1 = int(100 * ((cout_k1_dewi - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari dewi\t\t: {hitung_ui_k1_dewi(data_max_k1, data_min_k1, dewi_k1)}")

# calculate for k2
def hitung_ui_k2_dewi(data_max_k2, data_min_k2, dewi_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_dewi = dewi_k2
    
    ui_k2 = int(100 * ((cout_k2_dewi - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari dewi\t\t: {hitung_ui_k2_dewi(data_max_k2, data_min_k2, dewi_k2)}")

# calculate for k3
def hitung_ui_k3_dewi(data_max_k3, data_min_k3, dewi_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_dewi = dewi_k3
    
    ui_k3 = int(100 * ((cout_k3_dewi - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari dewi\t\t: {hitung_ui_k3_dewi(data_max_k3, data_min_k3, dewi_k3)}")

# calculate for k4
def hitung_ui_k4_dewi(data_max_k4, data_min_k4, dewi_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_dewi = dewi_k4
    
    ui_k4 = int(100 * ((cout_k4_dewi - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari dewi\t\t: {hitung_ui_k4_dewi(data_max_k4, data_min_k4, dewi_k4)}")

# calculate for k5
def hitung_ui_k5_dewi(data_max_k5, data_min_k5, dewi_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_dewi = dewi_k5
    
    ui_k5 = int(100 * ((cout_k5_dewi - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari dewi\t\t: {hitung_ui_k5_dewi(data_max_k5, data_min_k5, dewi_k5)}")

# calculate for k6
def hitung_ui_k6_dewi(data_max_k6, data_min_k6, dewi_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_dewi = dewi_k6
    
    ui_k6 = int(100 * ((cout_k6_dewi - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari dewi\t\t: {hitung_ui_k6_dewi(data_max_k6, data_min_k6, dewi_k6)}")

# calculate for k7
def hitung_ui_k7_dewi(data_max_k7, data_min_k7, dewi_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_dewi = dewi_k7
    
    ui_k7 = int(100 * ((cout_k7_dewi - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari dewi\t\t: {hitung_ui_k7_dewi(data_max_k7, data_min_k7, dewi_k7)}")

# calculate for k8
def hitung_ui_k8_dewi(data_max_k8, data_min_k8, dewi_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_dewi = dewi_k8
    
    ui_k8 = int(100 * ((cout_k8_dewi - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari dewi\t\t: {hitung_ui_k8_dewi(data_max_k8, data_min_k8, dewi_k8)}")

# calculate for k9
def hitung_ui_k9_dewi(data_max_k9, data_min_k9, dewi_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_dewi = dewi_k9
    
    ui_k9 = int(100 * ((cout_k9_dewi - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari dewi\t\t: {hitung_ui_k9_dewi(data_max_k9, data_min_k9, dewi_k9)}")

# calculate for k10
def hitung_ui_k10_dewi(data_max_k10, data_min_k10, dewi_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_dewi = dewi_k10
    
    ui_k10 = int(100 * ((cout_k10_dewi - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari dewi\t\t: {hitung_ui_k10_dewi(data_max_k10, data_min_k10, dewi_k10)}")

# calculate for k11
def hitung_ui_k11_dewi(data_max_k11, data_min_k11, dewi_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_dewi = dewi_k11
    
    ui_k11 = int(100 * ((cout_k11_dewi - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari dewi\t\t: {hitung_ui_k11_dewi(data_max_k11, data_min_k11, dewi_k11)}")

# calculate for k12
def hitung_ui_k12_dewi(data_max_k12, data_min_k12, dewi_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_dewi = dewi_k12
    
    ui_k12 = int(100 * ((cout_k12_dewi - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari dewi\t\t: {hitung_ui_k12_dewi(data_max_k12, data_min_k12, dewi_k12)}")

# calculate for k13
def hitung_ui_k13_dewi(data_max_k13, data_min_k13, dewi_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_dewi = dewi_k13
    
    ui_k13 = int(100 * ((cout_k13_dewi - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari dewi\t\t: {hitung_ui_k13_dewi(data_max_k13, data_min_k13, dewi_k13)}")

# rumus statistika untuk gerald

# calculate for k1
def hitung_ui_k1_gerald(data_max_k1, data_min_k1, gerald_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_gerald = gerald_k1
    
    ui_k1 = int(100 * ((cout_k1_gerald - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari gerald\t\t: {hitung_ui_k1_gerald(data_max_k1, data_min_k1, gerald_k1)}")

# calculate for k2
def hitung_ui_k2_gerald(data_max_k2, data_min_k2, gerald_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_gerald = gerald_k2
    
    ui_k2 = int(100 * ((cout_k2_gerald - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari gerald\t\t: {hitung_ui_k2_gerald(data_max_k2, data_min_k2, gerald_k2)}")

# calculate for k3
def hitung_ui_k3_gerald(data_max_k3, data_min_k3, gerald_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_gerald = gerald_k3
    
    ui_k3 = int(100 * ((cout_k3_gerald - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari gerald\t\t: {hitung_ui_k3_gerald(data_max_k3, data_min_k3, gerald_k3)}")

# calculate for k4
def hitung_ui_k4_gerald(data_max_k4, data_min_k4, gerald_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_gerald = gerald_k4
    
    ui_k4 = int(100 * ((cout_k4_gerald - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari gerald\t\t: {hitung_ui_k4_gerald(data_max_k4, data_min_k4, gerald_k4)}")

# calculate for k5
def hitung_ui_k5_gerald(data_max_k5, data_min_k5, gerald_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_gerald = gerald_k5
    
    ui_k5 = int(100 * ((cout_k5_gerald - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari gerald\t\t: {hitung_ui_k5_gerald(data_max_k5, data_min_k5, gerald_k5)}")

# calculate for k6
def hitung_ui_k6_gerald(data_max_k6, data_min_k6, gerald_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_gerald = gerald_k6
    
    ui_k6 = int(100 * ((cout_k6_gerald - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari gerald\t\t: {hitung_ui_k6_gerald(data_max_k6, data_min_k6, gerald_k6)}")

# calculate for k7
def hitung_ui_k7_gerald(data_max_k7, data_min_k7, gerald_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_gerald = gerald_k7
    
    ui_k7 = int(100 * ((cout_k7_gerald - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari gerald\t\t: {hitung_ui_k7_gerald(data_max_k7, data_min_k7, gerald_k7)}")

# calculate for k8
def hitung_ui_k8_gerald(data_max_k8, data_min_k8, gerald_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_gerald = gerald_k8
    
    ui_k8 = int(100 * ((cout_k8_gerald - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari gerald\t\t: {hitung_ui_k8_gerald(data_max_k8, data_min_k8, gerald_k8)}")

# calculate for k9
def hitung_ui_k9_gerald(data_max_k9, data_min_k9, gerald_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_gerald = gerald_k9
    
    ui_k9 = int(100 * ((cout_k9_gerald - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari gerald\t\t: {hitung_ui_k9_gerald(data_max_k9, data_min_k9, gerald_k9)}")

# calculate for k10
def hitung_ui_k10_gerald(data_max_k10, data_min_k10, gerald_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_gerald = gerald_k10
    
    ui_k10 = int(100 * ((cout_k10_gerald - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari gerald\t\t: {hitung_ui_k10_gerald(data_max_k10, data_min_k10, gerald_k10)}")

# calculate for k11
def hitung_ui_k11_gerald(data_max_k11, data_min_k11, gerald_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_gerald = gerald_k11
    
    ui_k11 = int(100 * ((cout_k11_gerald - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari gerald\t\t: {hitung_ui_k11_gerald(data_max_k11, data_min_k11, gerald_k11)}")

# calculate for k12
def hitung_ui_k12_gerald(data_max_k12, data_min_k12, gerald_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_gerald = gerald_k12
    
    ui_k12 = int(100 * ((cout_k12_gerald - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari gerald\t\t: {hitung_ui_k12_gerald(data_max_k12, data_min_k12, gerald_k12)}")

# calculate for k13
def hitung_ui_k13_gerald(data_max_k13, data_min_k13, gerald_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_gerald = gerald_k13
    
    ui_k13 = int(100 * ((cout_k13_gerald - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari gerald\t\t: {hitung_ui_k13_gerald(data_max_k13, data_min_k13, gerald_k13)}")

# rumus statistika untuk angga

# calculate for k1
def hitung_ui_k1_angga(data_max_k1, data_min_k1, angga_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_angga = angga_k1
    
    ui_k1 = int(100 * ((cout_k1_angga - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari angga\t\t: {hitung_ui_k1_angga(data_max_k1, data_min_k1, angga_k1)}")

# calculate for k2
def hitung_ui_k2_angga(data_max_k2, data_min_k2, angga_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_angga = angga_k2
    
    ui_k2 = int(100 * ((cout_k2_angga - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari angga\t\t: {hitung_ui_k2_angga(data_max_k2, data_min_k2, angga_k2)}")

# calculate for k3
def hitung_ui_k3_angga(data_max_k3, data_min_k3, angga_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_angga = angga_k3
    
    ui_k3 = int(100 * ((cout_k3_angga - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari angga\t\t: {hitung_ui_k3_angga(data_max_k3, data_min_k3, angga_k3)}")

# calculate for k4
def hitung_ui_k4_angga(data_max_k4, data_min_k4, angga_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_angga = angga_k4
    
    ui_k4 = int(100 * ((cout_k4_angga - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari angga\t\t: {hitung_ui_k4_angga(data_max_k4, data_min_k4, angga_k4)}")

# calculate for k5
def hitung_ui_k5_angga(data_max_k5, data_min_k5, angga_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_angga = angga_k5
    
    ui_k5 = int(100 * ((cout_k5_angga - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari angga\t\t: {hitung_ui_k5_angga(data_max_k5, data_min_k5, angga_k5)}")

# calculate for k6
def hitung_ui_k6_angga(data_max_k6, data_min_k6, angga_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_angga = angga_k6
    
    ui_k6 = int(100 * ((cout_k6_angga - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari angga\t\t: {hitung_ui_k6_angga(data_max_k6, data_min_k6, angga_k6)}")

# calculate for k7
def hitung_ui_k7_angga(data_max_k7, data_min_k7, angga_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_angga = angga_k7
    
    ui_k7 = int(100 * ((cout_k7_angga - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari angga\t\t: {hitung_ui_k7_angga(data_max_k7, data_min_k7, angga_k7)}")

# calculate for k8
def hitung_ui_k8_angga(data_max_k8, data_min_k8, angga_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_angga = angga_k8
    
    ui_k8 = int(100 * ((cout_k8_angga - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari angga\t\t: {hitung_ui_k8_angga(data_max_k8, data_min_k8, angga_k8)}")

# calculate for k9
def hitung_ui_k9_angga(data_max_k9, data_min_k9, angga_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_angga = angga_k9
    
    ui_k9 = int(100 * ((cout_k9_angga - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari angga\t\t: {hitung_ui_k9_angga(data_max_k9, data_min_k9, angga_k9)}")

# calculate for k10
def hitung_ui_k10_angga(data_max_k10, data_min_k10, angga_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_angga = angga_k10
    
    ui_k10 = int(100 * ((cout_k10_angga - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari angga\t\t: {hitung_ui_k10_angga(data_max_k10, data_min_k10, angga_k10)}")

# calculate for k11
def hitung_ui_k11_angga(data_max_k11, data_min_k11, angga_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_angga = angga_k11
    
    ui_k11 = int(100 * ((cout_k11_angga - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari angga\t\t: {hitung_ui_k11_angga(data_max_k11, data_min_k11, angga_k11)}")

# calculate for k12
def hitung_ui_k12_angga(data_max_k12, data_min_k12, angga_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_angga = angga_k12
    
    ui_k12 = int(100 * ((cout_k12_angga - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari angga\t\t: {hitung_ui_k12_angga(data_max_k12, data_min_k12, angga_k12)}")

# calculate for k13
def hitung_ui_k13_angga(data_max_k13, data_min_k13, angga_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_angga = angga_k13
    
    ui_k13 = int(100 * ((cout_k13_angga - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari angga\t\t: {hitung_ui_k13_angga(data_max_k13, data_min_k13, angga_k13)}")

# rumus statistika untuk fahmi

# calculate for k1
def hitung_ui_k1_fahmi(data_max_k1, data_min_k1, fahmi_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_fahmi = fahmi_k1
    
    ui_k1 = int(100 * ((cout_k1_fahmi - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari fahmi\t\t: {hitung_ui_k1_fahmi(data_max_k1, data_min_k1, fahmi_k1)}")

# calculate for k2
def hitung_ui_k2_fahmi(data_max_k2, data_min_k2, fahmi_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_fahmi = fahmi_k2
    
    ui_k2 = int(100 * ((cout_k2_fahmi - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari fahmi\t\t: {hitung_ui_k2_fahmi(data_max_k2, data_min_k2, fahmi_k2)}")

# calculate for k3
def hitung_ui_k3_fahmi(data_max_k3, data_min_k3, fahmi_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_fahmi = fahmi_k3
    
    ui_k3 = int(100 * ((cout_k3_fahmi - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari fahmi\t\t: {hitung_ui_k3_fahmi(data_max_k3, data_min_k3, fahmi_k3)}")

# calculate for k4
def hitung_ui_k4_fahmi(data_max_k4, data_min_k4, fahmi_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_fahmi = fahmi_k4
    
    ui_k4 = int(100 * ((cout_k4_fahmi - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari fahmi\t\t: {hitung_ui_k4_fahmi(data_max_k4, data_min_k4, fahmi_k4)}")

# calculate for k5
def hitung_ui_k5_fahmi(data_max_k5, data_min_k5, fahmi_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_fahmi = fahmi_k5
    
    ui_k5 = int(100 * ((cout_k5_fahmi - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari fahmi\t\t: {hitung_ui_k5_fahmi(data_max_k5, data_min_k5, fahmi_k5)}")

# calculate for k6
def hitung_ui_k6_fahmi(data_max_k6, data_min_k6, fahmi_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_fahmi = fahmi_k6
    
    ui_k6 = int(100 * ((cout_k6_fahmi - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari fahmi\t\t: {hitung_ui_k6_fahmi(data_max_k6, data_min_k6, fahmi_k6)}")

# calculate for k7
def hitung_ui_k7_fahmi(data_max_k7, data_min_k7, fahmi_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_fahmi = fahmi_k7
    
    ui_k7 = int(100 * ((cout_k7_fahmi - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari fahmi\t\t: {hitung_ui_k7_fahmi(data_max_k7, data_min_k7, fahmi_k7)}")

# calculate for k8
def hitung_ui_k8_fahmi(data_max_k8, data_min_k8, fahmi_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_fahmi = fahmi_k8
    
    ui_k8 = int(100 * ((cout_k8_fahmi - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari fahmi\t\t: {hitung_ui_k8_fahmi(data_max_k8, data_min_k8, fahmi_k8)}")

# calculate for k9
def hitung_ui_k9_fahmi(data_max_k9, data_min_k9, fahmi_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_fahmi = fahmi_k9
    
    ui_k9 = int(100 * ((cout_k9_fahmi - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari fahmi\t\t: {hitung_ui_k9_fahmi(data_max_k9, data_min_k9, fahmi_k9)}")

# calculate for k10
def hitung_ui_k10_fahmi(data_max_k10, data_min_k10, fahmi_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_fahmi = fahmi_k10
    
    ui_k10 = int(100 * ((cout_k10_fahmi - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari fahmi\t\t: {hitung_ui_k10_fahmi(data_max_k10, data_min_k10, fahmi_k10)}")

# calculate for k11
def hitung_ui_k11_fahmi(data_max_k11, data_min_k11, fahmi_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_fahmi = fahmi_k11
    
    ui_k11 = int(100 * ((cout_k11_fahmi - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari fahmi\t\t: {hitung_ui_k11_fahmi(data_max_k11, data_min_k11, fahmi_k11)}")

# calculate for k12
def hitung_ui_k12_fahmi(data_max_k12, data_min_k12, fahmi_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_fahmi = fahmi_k12
    
    ui_k12 = int(100 * ((cout_k12_fahmi - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari fahmi\t\t: {hitung_ui_k12_fahmi(data_max_k12, data_min_k12, fahmi_k12)}")

# calculate for k13
def hitung_ui_k13_fahmi(data_max_k13, data_min_k13, fahmi_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_fahmi = fahmi_k13
    
    ui_k13 = int(100 * ((cout_k13_fahmi - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari fahmi\t\t: {hitung_ui_k13_fahmi(data_max_k13, data_min_k13, fahmi_k13)}")

# rumus statistika untuk bima

# calculate for k1
def hitung_ui_k1_bima(data_max_k1, data_min_k1, bima_k1):
    cmax_k1 = data_max_k1
    cmin_k1 = data_min_k1
    cout_k1_bima = bima_k1
    
    ui_k1 = int(100 * ((cout_k1_bima - cmin_k1) / (cmax_k1 - cmin_k1)))
    
    return ui_k1

print(f"\nNilai utility alternatif K1 dari bima\t\t: {hitung_ui_k1_bima(data_max_k1, data_min_k1, bima_k1)}")

# calculate for k2
def hitung_ui_k2_bima(data_max_k2, data_min_k2, bima_k2):
    cmax_k2 = data_max_k2
    cmin_k2 = data_min_k2
    cout_k2_bima = bima_k2
    
    ui_k2 = int(100 * ((cout_k2_bima - cmin_k2) / (cmax_k2 - cmin_k2)))
    
    return ui_k2

print(f"Nilai utility alternatif K2 dari bima\t\t: {hitung_ui_k2_bima(data_max_k2, data_min_k2, bima_k2)}")

# calculate for k3
def hitung_ui_k3_bima(data_max_k3, data_min_k3, bima_k3):
    cmax_k3 = data_max_k3
    cmin_k3 = data_min_k3
    cout_k3_bima = bima_k3
    
    ui_k3 = int(100 * ((cout_k3_bima - cmin_k3) / (cmax_k3 - cmin_k3)))
    
    return ui_k3

print(f"Nilai utility alternatif K3 dari bima\t\t: {hitung_ui_k3_bima(data_max_k3, data_min_k3, bima_k3)}")

# calculate for k4
def hitung_ui_k4_bima(data_max_k4, data_min_k4, bima_k4):
    cmax_k4 = data_max_k4
    cmin_k4 = data_min_k4
    cout_k4_bima = bima_k4
    
    ui_k4 = int(100 * ((cout_k4_bima - cmin_k4) / (cmax_k4 - cmin_k4)))
    
    return ui_k4

print(f"Nilai utility alternatif K4 dari bima\t\t: {hitung_ui_k4_bima(data_max_k4, data_min_k4, bima_k4)}")

# calculate for k5
def hitung_ui_k5_bima(data_max_k5, data_min_k5, bima_k5):
    cmax_k5 = data_max_k5
    cmin_k5 = data_min_k5
    cout_k5_bima = bima_k5
    
    ui_k5 = int(100 * ((cout_k5_bima - cmin_k5) / (cmax_k5 - cmin_k5)))
    
    return ui_k5

print(f"Nilai utility alternatif K5 dari bima\t\t: {hitung_ui_k5_bima(data_max_k5, data_min_k5, bima_k5)}")

# calculate for k6
def hitung_ui_k6_bima(data_max_k6, data_min_k6, bima_k6):
    cmax_k6 = data_max_k6
    cmin_k6 = data_min_k6
    cout_k6_bima = bima_k6
    
    ui_k6 = int(100 * ((cout_k6_bima - cmin_k6) / (cmax_k6 - cmin_k6)))
    
    return ui_k6

print(f"Nilai utility alternatif K6 dari bima\t\t: {hitung_ui_k6_bima(data_max_k6, data_min_k6, bima_k6)}")

# calculate for k7
def hitung_ui_k7_bima(data_max_k7, data_min_k7, bima_k7):
    cmax_k7 = data_max_k7
    cmin_k7 = data_min_k7
    cout_k7_bima = bima_k7
    
    ui_k7 = int(100 * ((cout_k7_bima - cmin_k7) / (cmax_k7 - cmin_k7)))
    
    return ui_k7

print(f"Nilai utility alternatif K7 dari bima\t\t: {hitung_ui_k7_bima(data_max_k7, data_min_k7, bima_k7)}")

# calculate for k8
def hitung_ui_k8_bima(data_max_k8, data_min_k8, bima_k8):
    cmax_k8 = data_max_k8
    cmin_k8 = data_min_k8
    cout_k8_bima = bima_k8
    
    ui_k8 = int(100 * ((cout_k8_bima - cmin_k8) / (cmax_k8 - cmin_k8)))
    
    return ui_k8

print(f"Nilai utility alternatif K8 dari bima\t\t: {hitung_ui_k8_bima(data_max_k8, data_min_k8, bima_k8)}")

# calculate for k9
def hitung_ui_k9_bima(data_max_k9, data_min_k9, bima_k9):
    cmax_k9 = data_max_k9
    cmin_k9 = data_min_k9
    cout_k9_bima = bima_k9
    
    ui_k9 = int(100 * ((cout_k9_bima - cmin_k9) / (cmax_k9 - cmin_k9)))
    
    return ui_k9

print(f"Nilai utility alternatif K9 dari bima\t\t: {hitung_ui_k9_bima(data_max_k9, data_min_k9, bima_k9)}")

# calculate for k10
def hitung_ui_k10_bima(data_max_k10, data_min_k10, bima_k10):
    cmax_k10 = data_max_k10
    cmin_k10 = data_min_k10
    cout_k10_bima = bima_k10
    
    ui_k10 = int(100 * ((cout_k10_bima - cmin_k10) / (cmax_k10 - cmin_k10)))
    
    return ui_k10

print(f"Nilai utility alternatif K10 dari bima\t\t: {hitung_ui_k10_bima(data_max_k10, data_min_k10, bima_k10)}")

# calculate for k11
def hitung_ui_k11_bima(data_max_k11, data_min_k11, bima_k11):
    cmax_k11 = data_max_k11
    cmin_k11 = data_min_k11
    cout_k11_bima = bima_k11
    
    ui_k11 = int(100 * ((cout_k11_bima - cmin_k11) / (cmax_k11 - cmin_k11)))
    
    return ui_k11

print(f"Nilai utility alternatif K11 dari bima\t\t: {hitung_ui_k11_bima(data_max_k11, data_min_k11, bima_k11)}")

# calculate for k12
def hitung_ui_k12_bima(data_max_k12, data_min_k12, bima_k12):
    cmax_k12 = data_max_k12
    cmin_k12 = data_min_k12
    cout_k12_bima = bima_k12
    
    ui_k12 = int(100 * ((cout_k12_bima - cmin_k12) / (cmax_k12 - cmin_k12)))
    
    return ui_k12

print(f"Nilai utility alternatif K12 dari bima\t\t: {hitung_ui_k12_bima(data_max_k12, data_min_k12, bima_k12)}")

# calculate for k13
def hitung_ui_k13_bima(data_max_k13, data_min_k13, bima_k13):
    cmax_k13 = data_max_k13
    cmin_k13 = data_min_k13
    cout_k13_bima = bima_k13
    
    ui_k13 = int(100 * ((cout_k13_bima - cmin_k13) / (cmax_k13 - cmin_k13)))
    
    return ui_k13

print(f"Nilai utility alternatif K13 dari bima\t\t: {hitung_ui_k13_bima(data_max_k13, data_min_k13, bima_k13)}")


# calculate hasil akhir

# rumus every k in responden must be * with bobot k & + every hasil

# hasil akhir yanuario
hasil_akhir_overall_yanuario = ((hitung_ui_k1_yanuario(data_max_k1, data_min_k1, yanuario_k1) * 0.05) +
                           (hitung_ui_k2_yanuario(data_max_k2, data_min_k2, yanuario_k2) * 0.05) +
                           (hitung_ui_k3_yanuario(data_max_k3, data_min_k3, yanuario_k3) * 0.05) +
                           (hitung_ui_k4_yanuario(data_max_k4, data_min_k4, yanuario_k4) * 0.05) +
                           (hitung_ui_k5_yanuario(data_max_k5, data_min_k5, yanuario_k5) * 0.1) +
                           (hitung_ui_k6_yanuario(data_max_k6, data_min_k6, yanuario_k6) * 0.1) +
                           (hitung_ui_k7_yanuario(data_max_k7, data_min_k7, yanuario_k7) * 0.1) +
                           (hitung_ui_k8_yanuario(data_max_k8, data_min_k8, yanuario_k8) * 0.1) +
                           (hitung_ui_k9_yanuario(data_max_k9, data_min_k9, yanuario_k9) * 0.1) +
                           (hitung_ui_k10_yanuario(data_max_k10, data_min_k10, yanuario_k10) * 0.05) +
                           (hitung_ui_k11_yanuario(data_max_k11, data_min_k11, yanuario_k11) * 0.05) +
                           (hitung_ui_k12_yanuario(data_max_k12, data_min_k12, yanuario_k12) * 0.1) +
                           (hitung_ui_k13_yanuario(data_max_k13, data_min_k13, yanuario_k13) * 0.1))

print(f"Hasil akhir yanuario\t:\t{hasil_akhir_overall_yanuario}")

# hasil akhir alan
hasil_akhir_overall_alan = ((hitung_ui_k1_alan(data_max_k1, data_min_k1, alan_k1) * 0.05) +
                           (hitung_ui_k2_alan(data_max_k2, data_min_k2, alan_k2) * 0.05) +
                           (hitung_ui_k3_alan(data_max_k3, data_min_k3, alan_k3) * 0.05) +
                           (hitung_ui_k4_alan(data_max_k4, data_min_k4, alan_k4) * 0.05) +
                           (hitung_ui_k5_alan(data_max_k5, data_min_k5, alan_k5) * 0.1) +
                           (hitung_ui_k6_alan(data_max_k6, data_min_k6, alan_k6) * 0.1) +
                           (hitung_ui_k7_alan(data_max_k7, data_min_k7, alan_k7) * 0.1) +
                           (hitung_ui_k8_alan(data_max_k8, data_min_k8, alan_k8) * 0.1) +
                           (hitung_ui_k9_alan(data_max_k9, data_min_k9, alan_k9) * 0.1) +
                           (hitung_ui_k10_alan(data_max_k10, data_min_k10, alan_k10) * 0.05) +
                           (hitung_ui_k11_alan(data_max_k11, data_min_k11, alan_k11) * 0.05) +
                           (hitung_ui_k12_alan(data_max_k12, data_min_k12, alan_k12) * 0.1) +
                           (hitung_ui_k13_alan(data_max_k13, data_min_k13, alan_k13) * 0.1))

print(f"Hasil akhir alan\t:\t{hasil_akhir_overall_alan}")

# hasil akhir aqil
hasil_akhir_overall_aqil = ((hitung_ui_k1_aqil(data_max_k1, data_min_k1, aqil_k1) * 0.05) +
                           (hitung_ui_k2_aqil(data_max_k2, data_min_k2, aqil_k2) * 0.05) +
                           (hitung_ui_k3_aqil(data_max_k3, data_min_k3, aqil_k3) * 0.05) +
                           (hitung_ui_k4_aqil(data_max_k4, data_min_k4, aqil_k4) * 0.05) +
                           (hitung_ui_k5_aqil(data_max_k5, data_min_k5, aqil_k5) * 0.1) +
                           (hitung_ui_k6_aqil(data_max_k6, data_min_k6, aqil_k6) * 0.1) +
                           (hitung_ui_k7_aqil(data_max_k7, data_min_k7, aqil_k7) * 0.1) +
                           (hitung_ui_k8_aqil(data_max_k8, data_min_k8, aqil_k8) * 0.1) +
                           (hitung_ui_k9_aqil(data_max_k9, data_min_k9, aqil_k9) * 0.1) +
                           (hitung_ui_k10_aqil(data_max_k10, data_min_k10, aqil_k10) * 0.05) +
                           (hitung_ui_k11_aqil(data_max_k11, data_min_k11, aqil_k11) * 0.05) +
                           (hitung_ui_k12_aqil(data_max_k12, data_min_k12, aqil_k12) * 0.1) +
                           (hitung_ui_k13_aqil(data_max_k13, data_min_k13, aqil_k13) * 0.1))

print(f"Hasil akhir aqil\t:\t{hasil_akhir_overall_aqil}")

# hasil akhir mahisa
hasil_akhir_overall_mahisa = ((hitung_ui_k1_mahisa(data_max_k1, data_min_k1, mahisa_k1) * 0.05) +
                           (hitung_ui_k2_mahisa(data_max_k2, data_min_k2, mahisa_k2) * 0.05) +
                           (hitung_ui_k3_mahisa(data_max_k3, data_min_k3, mahisa_k3) * 0.05) +
                           (hitung_ui_k4_mahisa(data_max_k4, data_min_k4, mahisa_k4) * 0.05) +
                           (hitung_ui_k5_mahisa(data_max_k5, data_min_k5, mahisa_k5) * 0.1) +
                           (hitung_ui_k6_mahisa(data_max_k6, data_min_k6, mahisa_k6) * 0.1) +
                           (hitung_ui_k7_mahisa(data_max_k7, data_min_k7, mahisa_k7) * 0.1) +
                           (hitung_ui_k8_mahisa(data_max_k8, data_min_k8, mahisa_k8) * 0.1) +
                           (hitung_ui_k9_mahisa(data_max_k9, data_min_k9, mahisa_k9) * 0.1) +
                           (hitung_ui_k10_mahisa(data_max_k10, data_min_k10, mahisa_k10) * 0.05) +
                           (hitung_ui_k11_mahisa(data_max_k11, data_min_k11, mahisa_k11) * 0.05) +
                           (hitung_ui_k12_mahisa(data_max_k12, data_min_k12, mahisa_k12) * 0.1) +
                           (hitung_ui_k13_mahisa(data_max_k13, data_min_k13, mahisa_k13) * 0.1))

print(f"Hasil akhir mahisa\t:\t{hasil_akhir_overall_mahisa}")

# hasil akhir tari
hasil_akhir_overall_tari = ((hitung_ui_k1_tari(data_max_k1, data_min_k1, tari_k1) * 0.05) +
                           (hitung_ui_k2_tari(data_max_k2, data_min_k2, tari_k2) * 0.05) +
                           (hitung_ui_k3_tari(data_max_k3, data_min_k3, tari_k3) * 0.05) +
                           (hitung_ui_k4_tari(data_max_k4, data_min_k4, tari_k4) * 0.05) +
                           (hitung_ui_k5_tari(data_max_k5, data_min_k5, tari_k5) * 0.1) +
                           (hitung_ui_k6_tari(data_max_k6, data_min_k6, tari_k6) * 0.1) +
                           (hitung_ui_k7_tari(data_max_k7, data_min_k7, tari_k7) * 0.1) +
                           (hitung_ui_k8_tari(data_max_k8, data_min_k8, tari_k8) * 0.1) +
                           (hitung_ui_k9_tari(data_max_k9, data_min_k9, tari_k9) * 0.1) +
                           (hitung_ui_k10_tari(data_max_k10, data_min_k10, tari_k10) * 0.05) +
                           (hitung_ui_k11_tari(data_max_k11, data_min_k11, tari_k11) * 0.05) +
                           (hitung_ui_k12_tari(data_max_k12, data_min_k12, tari_k12) * 0.1) +
                           (hitung_ui_k13_tari(data_max_k13, data_min_k13, tari_k13) * 0.1))

print(f"Hasil akhir tari\t:\t{hasil_akhir_overall_tari}")

# hasil akhir fanny
hasil_akhir_overall_fanny = ((hitung_ui_k1_fanny(data_max_k1, data_min_k1, fanny_k1) * 0.05) +
                           (hitung_ui_k2_fanny(data_max_k2, data_min_k2, fanny_k2) * 0.05) +
                           (hitung_ui_k3_fanny(data_max_k3, data_min_k3, fanny_k3) * 0.05) +
                           (hitung_ui_k4_fanny(data_max_k4, data_min_k4, fanny_k4) * 0.05) +
                           (hitung_ui_k5_fanny(data_max_k5, data_min_k5, fanny_k5) * 0.1) +
                           (hitung_ui_k6_fanny(data_max_k6, data_min_k6, fanny_k6) * 0.1) +
                           (hitung_ui_k7_fanny(data_max_k7, data_min_k7, fanny_k7) * 0.1) +
                           (hitung_ui_k8_fanny(data_max_k8, data_min_k8, fanny_k8) * 0.1) +
                           (hitung_ui_k9_fanny(data_max_k9, data_min_k9, fanny_k9) * 0.1) +
                           (hitung_ui_k10_fanny(data_max_k10, data_min_k10, fanny_k10) * 0.05) +
                           (hitung_ui_k11_fanny(data_max_k11, data_min_k11, fanny_k11) * 0.05) +
                           (hitung_ui_k12_fanny(data_max_k12, data_min_k12, fanny_k12) * 0.1) +
                           (hitung_ui_k13_fanny(data_max_k13, data_min_k13, fanny_k13) * 0.1))

print(f"Hasil akhir fanny\t:\t{hasil_akhir_overall_fanny}")

# hasil akhir fathan
hasil_akhir_overall_fathan = ((hitung_ui_k1_fathan(data_max_k1, data_min_k1, fathan_k1) * 0.05) +
                           (hitung_ui_k2_fathan(data_max_k2, data_min_k2, fathan_k2) * 0.05) +
                           (hitung_ui_k3_fathan(data_max_k3, data_min_k3, fathan_k3) * 0.05) +
                           (hitung_ui_k4_fathan(data_max_k4, data_min_k4, fathan_k4) * 0.05) +
                           (hitung_ui_k5_fathan(data_max_k5, data_min_k5, fathan_k5) * 0.1) +
                           (hitung_ui_k6_fathan(data_max_k6, data_min_k6, fathan_k6) * 0.1) +
                           (hitung_ui_k7_fathan(data_max_k7, data_min_k7, fathan_k7) * 0.1) +
                           (hitung_ui_k8_fathan(data_max_k8, data_min_k8, fathan_k8) * 0.1) +
                           (hitung_ui_k9_fathan(data_max_k9, data_min_k9, fathan_k9) * 0.1) +
                           (hitung_ui_k10_fathan(data_max_k10, data_min_k10, fathan_k10) * 0.05) +
                           (hitung_ui_k11_fathan(data_max_k11, data_min_k11, fathan_k11) * 0.05) +
                           (hitung_ui_k12_fathan(data_max_k12, data_min_k12, fathan_k12) * 0.1) +
                           (hitung_ui_k13_fathan(data_max_k13, data_min_k13, fathan_k13) * 0.1))

print(f"Hasil akhir fathan\t:\t{hasil_akhir_overall_fathan}")

# hasil akhir sindika
hasil_akhir_overall_sindika = ((hitung_ui_k1_sindika(data_max_k1, data_min_k1, sindika_k1) * 0.05) +
                           (hitung_ui_k2_sindika(data_max_k2, data_min_k2, sindika_k2) * 0.05) +
                           (hitung_ui_k3_sindika(data_max_k3, data_min_k3, sindika_k3) * 0.05) +
                           (hitung_ui_k4_sindika(data_max_k4, data_min_k4, sindika_k4) * 0.05) +
                           (hitung_ui_k5_sindika(data_max_k5, data_min_k5, sindika_k5) * 0.1) +
                           (hitung_ui_k6_sindika(data_max_k6, data_min_k6, sindika_k6) * 0.1) +
                           (hitung_ui_k7_sindika(data_max_k7, data_min_k7, sindika_k7) * 0.1) +
                           (hitung_ui_k8_sindika(data_max_k8, data_min_k8, sindika_k8) * 0.1) +
                           (hitung_ui_k9_sindika(data_max_k9, data_min_k9, sindika_k9) * 0.1) +
                           (hitung_ui_k10_sindika(data_max_k10, data_min_k10, sindika_k10) * 0.05) +
                           (hitung_ui_k11_sindika(data_max_k11, data_min_k11, sindika_k11) * 0.05) +
                           (hitung_ui_k12_sindika(data_max_k12, data_min_k12, sindika_k12) * 0.1) +
                           (hitung_ui_k13_sindika(data_max_k13, data_min_k13, sindika_k13) * 0.1))

print(f"Hasil akhir sindika\t:\t{hasil_akhir_overall_sindika}")

# hasil akhir aryawildan
hasil_akhir_overall_aryawildan = ((hitung_ui_k1_aryawildan(data_max_k1, data_min_k1, aryawildan_k1) * 0.05) +
                           (hitung_ui_k2_aryawildan(data_max_k2, data_min_k2, aryawildan_k2) * 0.05) +
                           (hitung_ui_k3_aryawildan(data_max_k3, data_min_k3, aryawildan_k3) * 0.05) +
                           (hitung_ui_k4_aryawildan(data_max_k4, data_min_k4, aryawildan_k4) * 0.05) +
                           (hitung_ui_k5_aryawildan(data_max_k5, data_min_k5, aryawildan_k5) * 0.1) +
                           (hitung_ui_k6_aryawildan(data_max_k6, data_min_k6, aryawildan_k6) * 0.1) +
                           (hitung_ui_k7_aryawildan(data_max_k7, data_min_k7, aryawildan_k7) * 0.1) +
                           (hitung_ui_k8_aryawildan(data_max_k8, data_min_k8, aryawildan_k8) * 0.1) +
                           (hitung_ui_k9_aryawildan(data_max_k9, data_min_k9, aryawildan_k9) * 0.1) +
                           (hitung_ui_k10_aryawildan(data_max_k10, data_min_k10, aryawildan_k10) * 0.05) +
                           (hitung_ui_k11_aryawildan(data_max_k11, data_min_k11, aryawildan_k11) * 0.05) +
                           (hitung_ui_k12_aryawildan(data_max_k12, data_min_k12, aryawildan_k12) * 0.1) +
                           (hitung_ui_k13_aryawildan(data_max_k13, data_min_k13, aryawildan_k13) * 0.1))

print(f"Hasil akhir aryawildan\t:\t{hasil_akhir_overall_aryawildan}")

# hasil akhir icha
hasil_akhir_overall_icha = ((hitung_ui_k1_icha(data_max_k1, data_min_k1, icha_k1) * 0.05) +
                           (hitung_ui_k2_icha(data_max_k2, data_min_k2, icha_k2) * 0.05) +
                           (hitung_ui_k3_icha(data_max_k3, data_min_k3, icha_k3) * 0.05) +
                           (hitung_ui_k4_icha(data_max_k4, data_min_k4, icha_k4) * 0.05) +
                           (hitung_ui_k5_icha(data_max_k5, data_min_k5, icha_k5) * 0.1) +
                           (hitung_ui_k6_icha(data_max_k6, data_min_k6, icha_k6) * 0.1) +
                           (hitung_ui_k7_icha(data_max_k7, data_min_k7, icha_k7) * 0.1) +
                           (hitung_ui_k8_icha(data_max_k8, data_min_k8, icha_k8) * 0.1) +
                           (hitung_ui_k9_icha(data_max_k9, data_min_k9, icha_k9) * 0.1) +
                           (hitung_ui_k10_icha(data_max_k10, data_min_k10, icha_k10) * 0.05) +
                           (hitung_ui_k11_icha(data_max_k11, data_min_k11, icha_k11) * 0.05) +
                           (hitung_ui_k12_icha(data_max_k12, data_min_k12, icha_k12) * 0.1) +
                           (hitung_ui_k13_icha(data_max_k13, data_min_k13, icha_k13) * 0.1))

print(f"Hasil akhir icha\t:\t{hasil_akhir_overall_icha}")

# hasil akhir nugroho
hasil_akhir_overall_nugroho = ((hitung_ui_k1_nugroho(data_max_k1, data_min_k1, nugroho_k1) * 0.05) +
                           (hitung_ui_k2_nugroho(data_max_k2, data_min_k2, nugroho_k2) * 0.05) +
                           (hitung_ui_k3_nugroho(data_max_k3, data_min_k3, nugroho_k3) * 0.05) +
                           (hitung_ui_k4_nugroho(data_max_k4, data_min_k4, nugroho_k4) * 0.05) +
                           (hitung_ui_k5_nugroho(data_max_k5, data_min_k5, nugroho_k5) * 0.1) +
                           (hitung_ui_k6_nugroho(data_max_k6, data_min_k6, nugroho_k6) * 0.1) +
                           (hitung_ui_k7_nugroho(data_max_k7, data_min_k7, nugroho_k7) * 0.1) +
                           (hitung_ui_k8_nugroho(data_max_k8, data_min_k8, nugroho_k8) * 0.1) +
                           (hitung_ui_k9_nugroho(data_max_k9, data_min_k9, nugroho_k9) * 0.1) +
                           (hitung_ui_k10_nugroho(data_max_k10, data_min_k10, nugroho_k10) * 0.05) +
                           (hitung_ui_k11_nugroho(data_max_k11, data_min_k11, nugroho_k11) * 0.05) +
                           (hitung_ui_k12_nugroho(data_max_k12, data_min_k12, nugroho_k12) * 0.1) +
                           (hitung_ui_k13_nugroho(data_max_k13, data_min_k13, nugroho_k13) * 0.1))

print(f"Hasil akhir nugroho\t:\t{hasil_akhir_overall_nugroho}")

# hasil akhir adit
hasil_akhir_overall_adit = ((hitung_ui_k1_adit(data_max_k1, data_min_k1, adit_k1) * 0.05) +
                           (hitung_ui_k2_adit(data_max_k2, data_min_k2, adit_k2) * 0.05) +
                           (hitung_ui_k3_adit(data_max_k3, data_min_k3, adit_k3) * 0.05) +
                           (hitung_ui_k4_adit(data_max_k4, data_min_k4, adit_k4) * 0.05) +
                           (hitung_ui_k5_adit(data_max_k5, data_min_k5, adit_k5) * 0.1) +
                           (hitung_ui_k6_adit(data_max_k6, data_min_k6, adit_k6) * 0.1) +
                           (hitung_ui_k7_adit(data_max_k7, data_min_k7, adit_k7) * 0.1) +
                           (hitung_ui_k8_adit(data_max_k8, data_min_k8, adit_k8) * 0.1) +
                           (hitung_ui_k9_adit(data_max_k9, data_min_k9, adit_k9) * 0.1) +
                           (hitung_ui_k10_adit(data_max_k10, data_min_k10, adit_k10) * 0.05) +
                           (hitung_ui_k11_adit(data_max_k11, data_min_k11, adit_k11) * 0.05) +
                           (hitung_ui_k12_adit(data_max_k12, data_min_k12, adit_k12) * 0.1) +
                           (hitung_ui_k13_adit(data_max_k13, data_min_k13, adit_k13) * 0.1))

print(f"Hasil akhir adit\t:\t{hasil_akhir_overall_adit}")

# hasil akhir umam
hasil_akhir_overall_umam = ((hitung_ui_k1_umam(data_max_k1, data_min_k1, umam_k1) * 0.05) +
                           (hitung_ui_k2_umam(data_max_k2, data_min_k2, umam_k2) * 0.05) +
                           (hitung_ui_k3_umam(data_max_k3, data_min_k3, umam_k3) * 0.05) +
                           (hitung_ui_k4_umam(data_max_k4, data_min_k4, umam_k4) * 0.05) +
                           (hitung_ui_k5_umam(data_max_k5, data_min_k5, umam_k5) * 0.1) +
                           (hitung_ui_k6_umam(data_max_k6, data_min_k6, umam_k6) * 0.1) +
                           (hitung_ui_k7_umam(data_max_k7, data_min_k7, umam_k7) * 0.1) +
                           (hitung_ui_k8_umam(data_max_k8, data_min_k8, umam_k8) * 0.1) +
                           (hitung_ui_k9_umam(data_max_k9, data_min_k9, umam_k9) * 0.1) +
                           (hitung_ui_k10_umam(data_max_k10, data_min_k10, umam_k10) * 0.05) +
                           (hitung_ui_k11_umam(data_max_k11, data_min_k11, umam_k11) * 0.05) +
                           (hitung_ui_k12_umam(data_max_k12, data_min_k12, umam_k12) * 0.1) +
                           (hitung_ui_k13_umam(data_max_k13, data_min_k13, umam_k13) * 0.1))

print(f"Hasil akhir umam\t:\t{hasil_akhir_overall_umam}")

# hasil akhir nana
hasil_akhir_overall_nana = ((hitung_ui_k1_nana(data_max_k1, data_min_k1, nana_k1) * 0.05) +
                           (hitung_ui_k2_nana(data_max_k2, data_min_k2, nana_k2) * 0.05) +
                           (hitung_ui_k3_nana(data_max_k3, data_min_k3, nana_k3) * 0.05) +
                           (hitung_ui_k4_nana(data_max_k4, data_min_k4, nana_k4) * 0.05) +
                           (hitung_ui_k5_nana(data_max_k5, data_min_k5, nana_k5) * 0.1) +
                           (hitung_ui_k6_nana(data_max_k6, data_min_k6, nana_k6) * 0.1) +
                           (hitung_ui_k7_nana(data_max_k7, data_min_k7, nana_k7) * 0.1) +
                           (hitung_ui_k8_nana(data_max_k8, data_min_k8, nana_k8) * 0.1) +
                           (hitung_ui_k9_nana(data_max_k9, data_min_k9, nana_k9) * 0.1) +
                           (hitung_ui_k10_nana(data_max_k10, data_min_k10, nana_k10) * 0.05) +
                           (hitung_ui_k11_nana(data_max_k11, data_min_k11, nana_k11) * 0.05) +
                           (hitung_ui_k12_nana(data_max_k12, data_min_k12, nana_k12) * 0.1) +
                           (hitung_ui_k13_nana(data_max_k13, data_min_k13, nana_k13) * 0.1))

print(f"Hasil akhir nana\t:\t{hasil_akhir_overall_nana}")

# hasil akhir syahrur
hasil_akhir_overall_syahrur = ((hitung_ui_k1_syahrur(data_max_k1, data_min_k1, syahrur_k1) * 0.05) +
                           (hitung_ui_k2_syahrur(data_max_k2, data_min_k2, syahrur_k2) * 0.05) +
                           (hitung_ui_k3_syahrur(data_max_k3, data_min_k3, syahrur_k3) * 0.05) +
                           (hitung_ui_k4_syahrur(data_max_k4, data_min_k4, syahrur_k4) * 0.05) +
                           (hitung_ui_k5_syahrur(data_max_k5, data_min_k5, syahrur_k5) * 0.1) +
                           (hitung_ui_k6_syahrur(data_max_k6, data_min_k6, syahrur_k6) * 0.1) +
                           (hitung_ui_k7_syahrur(data_max_k7, data_min_k7, syahrur_k7) * 0.1) +
                           (hitung_ui_k8_syahrur(data_max_k8, data_min_k8, syahrur_k8) * 0.1) +
                           (hitung_ui_k9_syahrur(data_max_k9, data_min_k9, syahrur_k9) * 0.1) +
                           (hitung_ui_k10_syahrur(data_max_k10, data_min_k10, syahrur_k10) * 0.05) +
                           (hitung_ui_k11_syahrur(data_max_k11, data_min_k11, syahrur_k11) * 0.05) +
                           (hitung_ui_k12_syahrur(data_max_k12, data_min_k12, syahrur_k12) * 0.1) +
                           (hitung_ui_k13_syahrur(data_max_k13, data_min_k13, syahrur_k13) * 0.1))

print(f"Hasil akhir syahrur\t:\t{hasil_akhir_overall_syahrur}")

# hasil akhir dewi
hasil_akhir_overall_dewi = ((hitung_ui_k1_dewi(data_max_k1, data_min_k1, dewi_k1) * 0.05) +
                           (hitung_ui_k2_dewi(data_max_k2, data_min_k2, dewi_k2) * 0.05) +
                           (hitung_ui_k3_dewi(data_max_k3, data_min_k3, dewi_k3) * 0.05) +
                           (hitung_ui_k4_dewi(data_max_k4, data_min_k4, dewi_k4) * 0.05) +
                           (hitung_ui_k5_dewi(data_max_k5, data_min_k5, dewi_k5) * 0.1) +
                           (hitung_ui_k6_dewi(data_max_k6, data_min_k6, dewi_k6) * 0.1) +
                           (hitung_ui_k7_dewi(data_max_k7, data_min_k7, dewi_k7) * 0.1) +
                           (hitung_ui_k8_dewi(data_max_k8, data_min_k8, dewi_k8) * 0.1) +
                           (hitung_ui_k9_dewi(data_max_k9, data_min_k9, dewi_k9) * 0.1) +
                           (hitung_ui_k10_dewi(data_max_k10, data_min_k10, dewi_k10) * 0.05) +
                           (hitung_ui_k11_dewi(data_max_k11, data_min_k11, dewi_k11) * 0.05) +
                           (hitung_ui_k12_dewi(data_max_k12, data_min_k12, dewi_k12) * 0.1) +
                           (hitung_ui_k13_dewi(data_max_k13, data_min_k13, dewi_k13) * 0.1))

print(f"Hasil akhir dewi\t:\t{hasil_akhir_overall_dewi}")

# hasil akhir gerald
hasil_akhir_overall_gerald = ((hitung_ui_k1_gerald(data_max_k1, data_min_k1, gerald_k1) * 0.05) +
                           (hitung_ui_k2_gerald(data_max_k2, data_min_k2, gerald_k2) * 0.05) +
                           (hitung_ui_k3_gerald(data_max_k3, data_min_k3, gerald_k3) * 0.05) +
                           (hitung_ui_k4_gerald(data_max_k4, data_min_k4, gerald_k4) * 0.05) +
                           (hitung_ui_k5_gerald(data_max_k5, data_min_k5, gerald_k5) * 0.1) +
                           (hitung_ui_k6_gerald(data_max_k6, data_min_k6, gerald_k6) * 0.1) +
                           (hitung_ui_k7_gerald(data_max_k7, data_min_k7, gerald_k7) * 0.1) +
                           (hitung_ui_k8_gerald(data_max_k8, data_min_k8, gerald_k8) * 0.1) +
                           (hitung_ui_k9_gerald(data_max_k9, data_min_k9, gerald_k9) * 0.1) +
                           (hitung_ui_k10_gerald(data_max_k10, data_min_k10, gerald_k10) * 0.05) +
                           (hitung_ui_k11_gerald(data_max_k11, data_min_k11, gerald_k11) * 0.05) +
                           (hitung_ui_k12_gerald(data_max_k12, data_min_k12, gerald_k12) * 0.1) +
                           (hitung_ui_k13_gerald(data_max_k13, data_min_k13, gerald_k13) * 0.1))

print(f"Hasil akhir gerald\t:\t{hasil_akhir_overall_gerald}")

# hasil akhir angga
hasil_akhir_overall_angga = ((hitung_ui_k1_angga(data_max_k1, data_min_k1, angga_k1) * 0.05) +
                           (hitung_ui_k2_angga(data_max_k2, data_min_k2, angga_k2) * 0.05) +
                           (hitung_ui_k3_angga(data_max_k3, data_min_k3, angga_k3) * 0.05) +
                           (hitung_ui_k4_angga(data_max_k4, data_min_k4, angga_k4) * 0.05) +
                           (hitung_ui_k5_angga(data_max_k5, data_min_k5, angga_k5) * 0.1) +
                           (hitung_ui_k6_angga(data_max_k6, data_min_k6, angga_k6) * 0.1) +
                           (hitung_ui_k7_angga(data_max_k7, data_min_k7, angga_k7) * 0.1) +
                           (hitung_ui_k8_angga(data_max_k8, data_min_k8, angga_k8) * 0.1) +
                           (hitung_ui_k9_angga(data_max_k9, data_min_k9, angga_k9) * 0.1) +
                           (hitung_ui_k10_angga(data_max_k10, data_min_k10, angga_k10) * 0.05) +
                           (hitung_ui_k11_angga(data_max_k11, data_min_k11, angga_k11) * 0.05) +
                           (hitung_ui_k12_angga(data_max_k12, data_min_k12, angga_k12) * 0.1) +
                           (hitung_ui_k13_angga(data_max_k13, data_min_k13, angga_k13) * 0.1))

print(f"Hasil akhir angga\t:\t{hasil_akhir_overall_angga}")

# hasil akhir fahmi
hasil_akhir_overall_fahmi = ((hitung_ui_k1_fahmi(data_max_k1, data_min_k1, fahmi_k1) * 0.05) +
                           (hitung_ui_k2_fahmi(data_max_k2, data_min_k2, fahmi_k2) * 0.05) +
                           (hitung_ui_k3_fahmi(data_max_k3, data_min_k3, fahmi_k3) * 0.05) +
                           (hitung_ui_k4_fahmi(data_max_k4, data_min_k4, fahmi_k4) * 0.05) +
                           (hitung_ui_k5_fahmi(data_max_k5, data_min_k5, fahmi_k5) * 0.1) +
                           (hitung_ui_k6_fahmi(data_max_k6, data_min_k6, fahmi_k6) * 0.1) +
                           (hitung_ui_k7_fahmi(data_max_k7, data_min_k7, fahmi_k7) * 0.1) +
                           (hitung_ui_k8_fahmi(data_max_k8, data_min_k8, fahmi_k8) * 0.1) +
                           (hitung_ui_k9_fahmi(data_max_k9, data_min_k9, fahmi_k9) * 0.1) +
                           (hitung_ui_k10_fahmi(data_max_k10, data_min_k10, fahmi_k10) * 0.05) +
                           (hitung_ui_k11_fahmi(data_max_k11, data_min_k11, fahmi_k11) * 0.05) +
                           (hitung_ui_k12_fahmi(data_max_k12, data_min_k12, fahmi_k12) * 0.1) +
                           (hitung_ui_k13_fahmi(data_max_k13, data_min_k13, fahmi_k13) * 0.1))

print(f"Hasil akhir fahmi\t:\t{hasil_akhir_overall_fahmi}")

# hasil akhir bima
hasil_akhir_overall_bima = ((hitung_ui_k1_bima(data_max_k1, data_min_k1, bima_k1) * 0.05) +
                           (hitung_ui_k2_bima(data_max_k2, data_min_k2, bima_k2) * 0.05) +
                           (hitung_ui_k3_bima(data_max_k3, data_min_k3, bima_k3) * 0.05) +
                           (hitung_ui_k4_bima(data_max_k4, data_min_k4, bima_k4) * 0.05) +
                           (hitung_ui_k5_bima(data_max_k5, data_min_k5, bima_k5) * 0.1) +
                           (hitung_ui_k6_bima(data_max_k6, data_min_k6, bima_k6) * 0.1) +
                           (hitung_ui_k7_bima(data_max_k7, data_min_k7, bima_k7) * 0.1) +
                           (hitung_ui_k8_bima(data_max_k8, data_min_k8, bima_k8) * 0.1) +
                           (hitung_ui_k9_bima(data_max_k9, data_min_k9, bima_k9) * 0.1) +
                           (hitung_ui_k10_bima(data_max_k10, data_min_k10, bima_k10) * 0.05) +
                           (hitung_ui_k11_bima(data_max_k11, data_min_k11, bima_k11) * 0.05) +
                           (hitung_ui_k12_bima(data_max_k12, data_min_k12, bima_k12) * 0.1) +
                           (hitung_ui_k13_bima(data_max_k13, data_min_k13, bima_k13) * 0.1))

print(f"Hasil akhir bima\t:\t{hasil_akhir_overall_bima}")