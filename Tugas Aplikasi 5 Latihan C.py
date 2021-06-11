# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:47:51 2021

@author: Nik
"""

# Tugas Aplikasi 5 Latihan C
print("#####################################")
print (" Menampilkan bilangan bulat 1-100")
print("#####################################")
N=input("Masukan Nilai Bilangan = ")
if int(N)>100 :
    print(" Masukan Angka dari 0 sampai dengan 100")
if int(N)>=80 :
    print("Baik Sekali")
if int(N)>=65 and int(N)<=80:
    print("Baik")
if int(N)>=55 and int(N)<=65:
    print("Cukup")
if int(N)>=40 and int(N)<=55:
    print("Kurang")
if int(N)<=40 : 
    print("Kurang Sekali")
   