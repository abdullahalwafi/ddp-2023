pilihan  = int(input("""Silahkan pilih nomor dibawah ini
untuk menggunakan tools dibawah ini
==================================
Pilihan
==================================
1. Pertambahan
2. Pengurangan
3. Pembagian
=================================
Pilihan mu? """))
match pilihan:
    case 1:
        bilangan1 = input("bilangan 1 = ")
        bilangan2 = input("bilangan 2 = ")
        print("hasilnya adalah", bilangan1 + bilangan2)
    case "2":
        bilangan1 = input("bilangan 1 = ")
        bilangan2 = input("bilangan 2 = ")
        print("hasilnya adalah", bilangan1 - bilangan2)
