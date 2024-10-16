Nama: Vista Mellyna Atsfi
Nim: 2209106096

#Posttest 4 ada di bawah

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



#Posttest 4
Read Daftar Lomba
![image](https://github.com/user-attachments/assets/4ac28b99-f265-4b42-af09-f0009a1b6235)
![image](https://github.com/user-attachments/assets/6efbd545-bcda-48f6-8494-056e7a9025c1)

Create, Tambah Lomba
![image](https://github.com/user-attachments/assets/7ca122df-682c-4551-a980-2be0f1b46260)
![image](https://github.com/user-attachments/assets/f21e715a-1b02-4286-99e6-6d28382b8fb5)
![image](https://github.com/user-attachments/assets/88468552-01d7-49b5-82d5-61e27977b72d)
![image](https://github.com/user-attachments/assets/a2876aa8-4b5d-483c-b998-0a897dfcb836)
![image](https://github.com/user-attachments/assets/f6bef78d-bb82-474d-a1ef-72260d430a63)

Update, Ubah Lomba
Data Awal:![image](https://github.com/user-attachments/assets/2d80638e-dec3-48a0-a9ad-521440875c5e)
Proses Ubah: ![image](https://github.com/user-attachments/assets/d9c12248-d2a5-435a-b7e8-87d79dee098d)
Setelah diubah: ![image](https://github.com/user-attachments/assets/7b6696a4-6a8b-4c5b-92b1-d3912fa1d254)
![image](https://github.com/user-attachments/assets/66b8cd3e-4d2d-46d3-ae6a-a075ed1e3c5d)

Delete Lomba
Hapus Lomba Tidur: ![image](https://github.com/user-attachments/assets/d51270e3-814f-4f83-a711-836cde8db044)
![image](https://github.com/user-attachments/assets/ae48368a-7dde-4305-870a-f7c01fb1e347)
Lomba Tidur Telah Terhapus:![image](https://github.com/user-attachments/assets/180d2f98-79a6-44da-ab2d-069c961f55da)
![image](https://github.com/user-attachments/assets/4b31a680-f1b4-44d2-b75a-46f3d28bd3d5)

Search
![image](https://github.com/user-attachments/assets/e8a57740-15f5-4b64-8a42-d2f595286082)

Table Lomba:
![image](https://github.com/user-attachments/assets/082d5077-ee30-4850-8352-de7210ec3e5f)



