#ini karena blm ada data sebelumnya jadi gw definisiin manual
status_login = True
status = "Agent"
menu_tersedia = [["Login", "Register"],["Logout","Shop","Monster"],["Logout","Inventory","Battle","Arena","Shop","Laboratory"],["Save","Exit","Help"]] # menu blm login, admin, agent, all akses

def help():
    print("\n=========== HELP ===========\n")
    if (status_login) and (status == "Agent"):
        print("Halo Agent Purry. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
        print("\t1. Logout: Keluar dari akun yang sedang digunakan\n\t2. Inventory: Melihat owca-dex yang dimiliki oleh Agent\n\t3. Battle: Melakukan pertarungan dengan random monster secara 1v1 dan bergantian\n\t4. Arena: Melakukan pertarungan dengan random monster yang terdiri dari 5 stage.\n\t\t  Masing-masing stage merepresentasikan level monster yang akan dilawan.\n\t5. Shop: Memasuki shop sebagai tempat pembelian monster dan potion\n\t6. Laboratory: Melakukan upgrase monster yang dimiliki di inventory")
        print("\t7. Save: Menyimpan data game\n\t8. Exit: Keluar program")
    elif (status_login) and (status == "Admin"):
        print("Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:")
        print("\t1. Logout: Keluar dari akun yang sedang digunakan\n\t2. Shop: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent\n\t3. Monster : Melakukan manajemen pada database monster")
        print("\t4. Save: Menyimpan data game\n\t5. Exit: Keluar program")
    else:
        print("\nKamu belum login sebagai role apapun. Silahkan login terlebih dahulu.\n")
        print("\t1. Login: Masuk ke dalam akun yang sudah terdaftar \n\t2. Register: Membuat akun baru")
    print("\nFootnote:\n\t1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar\n\t2. Jangan lupa memasukkaninput yang valid")
    return

def cek_input_valid(input_user):
    input_valid = False
    if (status_login) and (status== "Agent"):
        if (input_user in menu_tersedia[2]) or (input_user in menu_tersedia[3]):
            input_valid = True
    elif (status_login) and (status == "Admin"):
        if (input_user in menu_tersedia[1]) or (input_user in menu_tersedia[3]):
            input_valid = True
    else:
        if (input_user in menu_tersedia[0]) or(input_user in menu_tersedia[3]):
            input_valid = True
    return input_valid

def menu():
    input_user = str(input())
    input_valid = cek_input_valid(input_user)
    while(input_valid == False):
        print("Input tidak valid")
        input_user = str(input())
        input_valid = cek_input_valid(input_user)
    #if (input_valid):
        #call fungsi terkait
    return(input_user)
menu()