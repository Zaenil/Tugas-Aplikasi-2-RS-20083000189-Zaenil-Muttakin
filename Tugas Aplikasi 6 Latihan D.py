# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 01:05:11 2021

@author: Nik
"""
print("================================")
print("     Upah Kerja Per Jam ")
print("================================")
print("Upah Perjam Rp.2.500")
N=input("Masukan Jumlah Jam Kerja Anda ? ")
Upah_Kerja=2500
Pajak =375
Jumlah_Pajak=Pajak * N
Jumlah_Upah= N * Upah_Kerja
if (N)>0 :
    print(Jumlah_Upah)-int(Jumlah_Pajak)