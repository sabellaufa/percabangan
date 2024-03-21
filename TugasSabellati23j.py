#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Menentukan ganjil genap 
nilai = int(input('isikan Nilai:'))
sisa_bagi = nilai % 2

if sisa_bagi==0:
    print(f'{nilai} adalah bilangan genap')
else:
    print(f'{nilai} adalah bilangan ganjil')
print('program selesai')


# In[8]:



nilai_program = int(input('isikan Nilai pemrograman:'))
if nilai_program < 0 or nilai_program > 100:
    print("Nilai Anda Salah")
else:
    if nilai_program <50:
        print("E")
    elif nilai_program <60:
        print("D")
    elif nilai_program <70:
        print("C")
    elif nilai_program <85:
        print("B")
    elif nilai_program <=100:
        print("A")
   


# In[11]:


username = input('isikan Username:')
password = input('isikan Password:')

#jika username salah => Username anda salah 
#jika password salah => Password anda salah 
#jika keduanya salah => Username dan password anda salah
#jika keduanya benar => Selamat datang {username}
#username: admin
#password: admin

if username == 'admin':
    if password== 'admin':
        print(f'selamat datang {username}')
    else:
        print(f'password anda salah')
else:
    if password == 'admin':
        print("Username anda salah")
    else:
        print("Username dan Password anda salah")


# In[34]:


nama = input("Masukan nama:")
umur = int(input("Masukan umur:"))
alamat = input("Masukan alamat:")
tabungan = int(input("Masukan jumlah tabungan:"))

pangkat = ''

if umur > 40:
    if alamat == 'New York' or alamat =='Nevada' or alamat =='Havana':
        if tabungan > 10000000:
            pangkat = 'Don'
    
elif umur >25 and umur <40:
       if alamat == 'New Jersey' or alamat == 'Manhattan' or alamat == 'Nevada':
            if tabungan <=1000000 and tabungan >=200000000:
                pangkat = 'Underboss'
                
elif umur >18 and umur <24:
        if alamat == 'California' or alamat == 'Detroit' or alamat == 'Boston':
            if tabungan <=1000000:
                pangkat = 'Capo'

if pangkat != '':
    print(f'{nama} kemungkinan seorang anggota mafia dengan pangkat {pangkat}')
else:
    print(f'{nama} tidak mencurigakan')      


# In[ ]:




