# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:38:12 2021

@author: Nik
"""
#Mengecek Tingkat Usia
#Tugas Aplikasi 5 Latihan B
print("#####################################")
print ("     Mengecek Tingkat Usia")
print("#####################################")
N=input("Masukan Nilai Usia = ")
if int(N)>=60 :
    print("Lansia")
if int(N)>=35 and int(N)<=59 :
        print("Dewasa")
if int(N)>=18 and int(N)<=34 :
        print("Pemuda")
if int(N)>=15 and int(N)<=17:
        print("Remaja")
if int(N)>=0 and int(N)<=16:
        print("Anak-Anak")