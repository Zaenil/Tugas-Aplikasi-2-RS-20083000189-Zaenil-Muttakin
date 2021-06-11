# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print ("===============================================")
print ("           KATEGORI NILAI MAHASISWA")
print ("===============================================")
N=input("Masukan Nilai Mahasiswa = ")
if int(N)>=90 and int(N)<=100 :
    print ("         KATEGORI NILAI A")
if int(N)>=81 and int(N)<=9 :
    print ("         KATEGORI NILAI B")
if int(N)>=71 and int(N)<=80 :
    print ("         KATEGORI NILAI C")
if int(N)>=61 and int(N)<=70 :
     print ("         KATEGORI NILAI D")
if int(N)<=61 :
    print ("         KATEGORI NILAI E")
if int(N) >100 :
    print ("SILAHKAN MASUKAN ANGKA 1 SAMPAI DENGAN 100")