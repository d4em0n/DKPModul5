class userService:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.data = {
            "muhammadalifaramdhankelompok02@gmail.com" : {
                "email"     : "muhammadalifaramdhankelompok0@gmail.com",
                "password"  : "12345",
                "role"      : "superadmin"
            },
            "saipulanwarkelompok02@gmail.com" : {
                "email"     : "saipulanwarkelompok02@gmail.com",
                "password"  : "12345",
                "role"      : "user"
            }
        }
        self.histories = {
            "muhammadalifaramdhankelompok02@gmail.com" : {
                "peminjaman_buku"     : {"Fisika Dasar", "Dasar Komputer dan Pemrograman"},
                "tanggal_pinjam"  : "26-04-2020"
            },
            "saipulanwarkelompok02@gmail.com" : {
                "peminjaman_buku"     : {"Kalkulus", "Dasar Komputer dan Pemrograman", "Konsep Jaringan Komputer"},
                "tanggal_pinjam"  : "26-04-2020"
            }
        }
    def login(self):
        get_data, data_buku = self.checkCredentials()
        if get_data:
            print("\nWelcome ",get_data['role'])
            print("Logged it as user email: ",get_data['email'])
            print("{} meminjam buku : ".format(get_data['email']))
            for buku in data_buku['peminjaman_buku']:
                print(buku)
        else:
            print("\nInvalid Login!\n")

    def checkCredentials(self):
        for value in self.data:
            if value == self.email:
                get_data_user = self.data[value]
                data_buku = self.histories[value]
                if self.password == get_data_user['password']:
                    return get_data_user, data_buku
                else:
                    return False

print("System Login Kelompok 02!\n")
email = input("Email: ")
password = input("Password: ")
get_class = userService(email,password)
get_class.login()
