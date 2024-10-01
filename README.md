Nama: Vista Mellyna Atsfi
Nim: 2209106096

# Administration django

#Peserta
![image](https://github.com/user-attachments/assets/dca6be0f-618f-4171-b2f7-1e9650f7832c)
![image](https://github.com/user-attachments/assets/6a04d308-6ec8-4832-8702-dec93a9f7848)

#Penyelenggara
![image](https://github.com/user-attachments/assets/70979379-93ec-4367-8131-43cebe7db4bb)
![image](https://github.com/user-attachments/assets/c503aab7-95a2-45f9-a719-5aef23ac8905)

#Lomba
![image](https://github.com/user-attachments/assets/d1e72de9-7195-4edc-849f-fe1a1ad27ba5)
![image](https://github.com/user-attachments/assets/d4d192d3-515e-48cf-8839-7e7a7fc01a88)

#Jurusan
![image](https://github.com/user-attachments/assets/68a584e9-09da-49d6-9525-230f5959d4e6)
![image](https://github.com/user-attachments/assets/dc2636da-3d5d-4557-97cf-20393fdd0bbb)

#Account
![image](https://github.com/user-attachments/assets/358e58c2-9bd9-46d2-9fde-8af4cdb18cbc)
![image](https://github.com/user-attachments/assets/ae7efbe3-77ba-4256-a3f6-b287269e3642)


#Page
![image](https://github.com/user-attachments/assets/9f4a5b5c-4f7c-4297-a9b4-4e252df67456)
![image](https://github.com/user-attachments/assets/d39e3f73-327e-47db-92bd-a39ee678c6cb)
![image](https://github.com/user-attachments/assets/9d02461a-051d-4f95-ae65-5c51096529ff)


#Xammp
![image](https://github.com/user-attachments/assets/9b266176-ccc9-47d5-9ef8-f8c3f364c13c)
![image](https://github.com/user-attachments/assets/569f736e-cf49-417b-b3c8-c6c19fae15b0)
![image](https://github.com/user-attachments/assets/fa78ecc4-815a-49f3-90c6-42790daf3764)
![image](https://github.com/user-attachments/assets/fad0fe65-e129-4459-8c83-d7774a8a5cad)
![image](https://github.com/user-attachments/assets/993243ae-5b2a-4b78-9086-5a7fc24fca6e)

# Penjelasan
def save_model(self, request, obj, form, change):
        # Simpan peserta terlebih dahulu
        super().save_model(request, obj, form, change)

        # Cek apakah user dengan email peserta sudah ada
        user, created = Account.objects.get_or_create(
            email=obj.email,  # Pastikan menggunakan email dari peserta
            defaults={
                'password': make_password('default_password'),  # Menggunakan hashing password
                'role': Account.PESERTA  # Atur role sebagai peserta
            }
        )

        if not created:
            # Jika user sudah ada, perbarui role (jika perlu)
            user.role = Account.PESERTA
            user.save()
Otomatis membuat akun saat membuat peserta dan penyelenggara

untuk gambar digunakan sebagai background:
body {
            background-image: url('{% static "images/bunga.jpg" %}');

