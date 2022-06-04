print("Nama: Faisal A. F. Rahman\nNIM: 2130511027\n")

def cari_luas_belahketupat(p, q):  
    """
    Fungsi didefinisikan dengan keyword def diikuti dengan nama fungsi dan parameternya dalam kurung (). 
    """

    operasi_hitung = p * q / 2

    """
    Pernyataan return [expression] akan membuat eksekusi program keluar dari fungsi saat itu, sekaligus 
    mengembalikan nilai tertentu. Nilai return yang tidak mengembalikan (ekspresi) nilai bersifat sama. 
    """
    return operasi_hitung
    
p = float(input("Masukkan panjang Diagonal 1: "))
q = float(input("Masukkan lebar Diagonal 2: "))

print("\nLuas dari belah ketupat dengan panjang", p, "cm dan lebar", q, "cm adalah",cari_luas_belahketupat(p, q), "cm3")
