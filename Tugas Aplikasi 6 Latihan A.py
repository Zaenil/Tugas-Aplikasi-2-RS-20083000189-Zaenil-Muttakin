# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 17:13:03 2021

@author: Nik
"""
#TUGAS APLIKASI 8 LATIHAN A
print("#####################################")
print ("      Transaksi Pembelian")
print("#####################################")
N=input("Jumlah Pembelian =")
Harga_satuan=660000
Diskon=99000
Jumlah_Diskon= int(N)*Diskon
Total_Harga= int(N) * int(Harga_satuan)
if int(N)>0 and int(N)<1500000 :
    print (Total_Harga )
if (Total_Harga)>1500000 :
    print =(Total_Harga)-int(Jumlah_Diskon)
    