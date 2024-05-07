username = []
username_pass = {}

karakter = ['.', ',']

angka = ['1','2','3','4','5','6','7','8','9','0']

huruf_besar = [chr(i)for i in range(ord('A'), ord('Z')+1,1)]

huruf_kecil = [chr(i) for i in range(ord('a'), ord('z')+1, 1)]

login = False

def cek_password(password):
    hurufB = False
    hurufK = False
    cek_angka = False
    cek_karakter = False
    if len(password) < 8:               # Jika panjang password lebih kecil dari 8
        print ("Password minimal 8 karakter")

    else:
        for i in range(len(password)):   # cek satu per satu indeks string
            if password[i] in angka :      # Jika string password memiliki angka
                cek_angka = True
            elif password[i] in huruf_besar:  # Jika string password memiliki huruf besar
                hurufB = True
            elif password[i]in huruf_kecil:     # Jika string password memiliki huruf kecil
                hurufK = True
            elif password[i] in karakter:       # Jika string password memiliki karakter
                cek_karakter = True

        if not cek_angka:                           # Jika password tidak memiliki angka
            print("Password harus memiliki angka")
        if not hurufB:                              # Jika password tidak memiliki huruf besar
            print("Password harus memiliki huruf besar")
        if not hurufK:                                      # Jika password tidak memiliki huruf kecil
            print("Password harus memiliki huruf kecil")
        if not cek_karakter:                                # Jika password tidak memiliki karakter special
            print("Password harus memiliki karakter spesial seperti ',' atau '.'")

        if cek_angka and cek_karakter and hurufB and hurufK :   # Jika semua kategori sudah mememuhi
            return True
        else :                  # Jika belum
            return False

def register():

    finished = False
    while (finished == False):   # Selama pembuatan akun belum berhasil
        print("=" * 50)
        print(" "* 19 + "Register")
        print("="*50)
        print()
        username = input("Username: ")
        password = input("Password: ")
        hasil = cek_password(password)              # password akan di cek apakah sudah memenuhi standard

        # cek_password adalah sebuah subprogram yang mengembalikan buah nilai False or True dan juga merupakan sebuah prosedur yang akan mencetak kriteria password yang belum terpenuhi
        print()

        while not hasil or username in username_pass:    # Selama password belum memenuhi kriteria atau Username sudah pernah ada terdaftar
            if username in username_pass:        # Jika username pasien terdaftar
                print("Username Sudah pernah digunakan.")
                print()
                username = input("Username: ")
                password = input("Password: ")
                hasil = cek_password(password)

            else:           # Jika Password belum memenuhi kriteria
                password = input("Password: ")
                hasil = cek_password(password)
            print()

        username_pass[username] = password
        finished = True

        #selesai buat akun

def login():
    global login

    username= input("Username: ")
    password = input("Password : ")

    salah = 0

    while((username not in username_pass or password != username_pass[username]) and salah != 2 ):      # selama username pasien belum terdaftar atau password dari username tersebut salah dan belum salah selama 3 kali
        if(username not in username_pass):               # Jika username pasien belum terdaftar
            print(f"Username {username} tidak ditemukan. ")
        if(username in username_pass):                       # Jika username pasien terdaftar
            if password != username_pass[username]:          # Jika password yang di input tidak sesuai dengan yang seharusnya

                print("Password salah, coba lagi")
        salah += 1
        username = input("Username: ")
        password = input("Password: ")

    if (username in username_pass and password == username_pass[username]):       # Jika username terdaftar dan password benar
        print ()
        login = True
        return login

    else:
        print("Tidak berhasil Login")
        return False
    
