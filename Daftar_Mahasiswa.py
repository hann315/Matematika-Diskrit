"""
Name: Faisal A. F. Rahman
NIM: 21***11027
Purposes: Add new data, search data, and show added data from List.
Text Editor: Visual Code Studio
Interpreter: Python 3.10.4
Operating System: Windows 11
Cons: The value stored on the list will be deleted if the instance restarted
"""

nama = []
nomor_telp = []
alamat = []
matkul = []
nim = []

def menu_utama():
    print('''
__________ MENU __________
    1. Data Baru
    2. Cari Data
    3. Tampilkan Data
    ''')
    pilih_menu = input('Masukkan pilihan: ')
    if pilih_menu == '1':
        menu_data_baru()
    elif pilih_menu == '2':
        menu_cari_data()
    elif pilih_menu == '3':
        menu_tampilkan_data()
    else:
        print('\nPilihan tersebut tidak ada!')
        menu_utama()

def menu_data_baru():
    print('\n\n')
    print('=' * 30)
    in_Nama = str(input('\nMasukkan nama: '))
    in_NIM = str(input('Masukkan NIM: '))
    in_Matkul = str(input('Masukkan mata kuliah favorit: '))
    in_Alamat = str(input('Masukkan alamat: '))
    in_nomor_telp = str(input('Masukkan nomor telepon: '))
    print('=' * 30, '\n')

    nim.append(in_NIM)
    nama.append(in_Nama)
    matkul.append(in_Matkul)
    alamat.append(in_Alamat)
    nomor_telp.append(in_nomor_telp)

def menu_cari_data():
    in_NIM_cari = str(input('Masukkan NIM: '))
    nim_cari = nim.index(in_NIM_cari)

    print('\n\n')
    print('=' * 30)
    print('Nama: ', nama [nim_cari])
    print('Alamat: ', alamat [nim_cari])
    print('Nomor Induk Mahasiswa: ', nim [nim_cari])
    print('Nomor telepon: ', nomor_telp [nim_cari])
    print('Mata kuliah favorit: ', matkul [nim_cari])
    print('=' * 30, '\n')

    if in_NIM_cari not in nim:
        print('\nData yang Anda cari tidak terdaftar atau tidak ditemukan')
        menu_cari_data()

def menu_tampilkan_data():
    if len(nim) == 0:
        print('\nData yang Anda cari tidak terdaftar atau tidak ditemukan')
    elif len(nim) >= 1:
        batas = '-'
        samping = '|'
        a = 'Nama'
        b = 'NIM'
        c = 'Nomor Telepon'
        d = 'Alamat'
        e = 'Mata kuliah favorit'
        
        print(120 * batas)
        print(samping,3*' '+a+(30-len(a))*' '+samping+3*' '+b+(15-len(b))*' '+samping+3*' '+c+(15-len(c))*' '+samping+3*' '+d+(16-len(d))*' '+samping+3*' '+e+(22-len(e))*' '+samping,)
        print(120 * batas)
        for x in range(len(nim)):
            print(samping,3*' '+nama[x]+(30-len(nama[x]))*' '+samping+3*' '+nim[x]+(15-len(nim[x]))*' '+samping+3*' '+nomor_telp[x]+(15-len(nomor_telp[x]))*' '+samping+3*' '+alamat[x]+(16-len(alamat[x]))*' '+samping+3*' '+matkul[x]+(22-len(matkul[x]))*' '+samping,)
        print(120 * batas)

while(True):
    menu_utama()
    out = input('\nApakah Anda ingin melanjutkan? (Y/T)\n')

    if out == 'Y' or out == 'y' or out == 'Ya' or out == 'ya':
        menu_utama()
    elif out == 'T' or out == 't' or out == 'Tidak' or out == 'tidak':
        break
exit()