# Mini-Project-2
Dhita Olivia | 2409116040 | Sistem Informasi A 2024 | Tema : Pembayaran Uang Kas

# Flowchart
![Minpro DDP 2](https://github.com/user-attachments/assets/4f219a79-d58e-47ea-b0ab-92a3869f58e2)

# Penjelasan Program Dari Awal Hingga Akhir 

# Menu Login
Gambar dibawah ini adalah bentuk login sebagai Bendahara dan Pengguna.

![Screenshot 2024-10-15 032151](https://github.com/user-attachments/assets/f3c6ad88-68ab-453c-a8a3-d7da526e730c)

# penjelasan menu login
1. jika user memasukkan "bendahara" beserta password nya, maka ia akan berperan sebagai bendahara. bendahara sendiri bisa melakukan CRUD(Create, Read, Update, Delete) pada pembayaran uang kas.
2. jika user memasukkan "pengguna" beserta password nya, maka ia akan berperan sebagai pengguna. pengguna sendiri hanya bisa melakukan transaksi atau pembayaran saja.

![Screenshot 2024-10-15 033448](https://github.com/user-attachments/assets/45cdfbab-0643-41c9-8730-0c0de0a88e23)

![Screenshot 2024-10-15 033508](https://github.com/user-attachments/assets/98355904-f5a0-481b-a26d-e83da234fd09)

Berikut adalah kode fungsi untuk masing-masing login role. jika user login tidak sesuai dengan role nya, maka akan diarahkan untuk mengisi data kembali.

![Screenshot 2024-10-15 033922](https://github.com/user-attachments/assets/8e95b756-3ea0-484b-8923-9df4a86632c7)

# Menu Bendahara

![Screenshot 2024-10-15 034521](https://github.com/user-attachments/assets/c777761c-f404-4a57-88dc-21c6d9b69b58)

Pada menu bendahara, user akan diberi 5 menu. setelah bendahara memasukkan nomor sesuai dengan keiinginannya, bendahara akan langsung diarahkan sesuai dengan pilihannya. berikut adalah kode yang dimana setiap nomor pilihan akan diarahkan ke masing-masing fungsi. 

![Screenshot 2024-10-15 035502](https://github.com/user-attachments/assets/d6a3ab56-da0b-4dc0-9ad8-38780d65c718)

# penjelasan menu bendahara
1. Menampilkan Data List Kas

![Screenshot 2024-10-15 040032](https://github.com/user-attachments/assets/bdf873e8-2ae8-4111-af0d-d9b84eb2e921)

ketika bendahara memilih pilihan 1, maka akan keluar rincian kas dari bulan Januari hingga Mei. berikut untuk menampilkan kode nya

![Screenshot 2024-10-15 041038](https://github.com/user-attachments/assets/5c3b937b-d012-4be1-869e-cab8bf790e2d)


2. Menambah Data List Kas

![Screenshot 2024-10-15 041733](https://github.com/user-attachments/assets/340a5c81-41b4-448e-93c9-806a12329589)


ketika bendahara memilih pilihan 2, maka akan keluar tabel yang memperlihatkan kas yang awal. kemudian, bendahara akan diarahkan untuk menginput bulan dan data baru. berikut untuk menampilkan kode nya

![Screenshot 2024-10-15 041818](https://github.com/user-attachments/assets/b290f782-6a0b-4967-a773-9614e5c41d2f)

3. Menghapus Data Kas Yang Tidak Diperlukan

![Screenshot 2024-10-15 042044](https://github.com/user-attachments/assets/14432620-5d4f-4cf1-8b58-c5fee4d49cc4)

ketika bendahara memilih pilihan 3, maka akan keluar tabel yang memperlihatkan kas yang awal. kemudian, bendahara akan diarahkan untuk menginput bulan yang ingin dihapus. maka otomatis akan terhapus bersama nilainya. berikut untuk menampilkan kode nya

![Screenshot 2024-10-15 042520](https://github.com/user-attachments/assets/b99a942c-1e95-49ca-ad41-14329bf7371d)

4. Mengganti Data Kas Dengan Yang Baru

![Screenshot 2024-10-15 042821](https://github.com/user-attachments/assets/9b42f452-74b8-4517-9887-6a8105758704)

ketika bendahara memilih pilihan 4, maka akan keluar tabel yang memperlihatkan kas yang awal. kemudian, bendahara akan diarahkan untuk menginput bulan yang ingin diganti, dan menginput data baru. maka otomatis data yang lama akan terganti dengan yang baru. berikut untuk menampilkan kode nya

![Screenshot 2024-10-15 043209](https://github.com/user-attachments/assets/7df9dac0-ce87-44fd-a9f3-0b6a08d04e75)

5. Keluar Menu

jika bendahara memilih pilihan 5, maka program akan otomatis berhenti dan memulai dari awal. 

![Screenshot 2024-10-15 043611](https://github.com/user-attachments/assets/b0157051-01b0-46d3-ad96-acd56c3d153e)

berikut untuk menampilkan kode nya

![Screenshot 2024-10-15 043733](https://github.com/user-attachments/assets/675ee5a0-c763-4d94-a3b4-20565d93dd26)

# Menu Pengguna

![Screenshot 2024-10-15 044419](https://github.com/user-attachments/assets/5e40d701-cd14-473b-bc51-3547cf5116fa)

user harus login sesuai dengan uname dan password, jika salah maka program akan mengulang login. ketika user masuk sebagai pengguna, maka akan terlihat pada gabar diatas. berikut untuk menampilkan kode nya

![Screenshot 2024-10-15 044934](https://github.com/user-attachments/assets/9d3f042b-89df-468f-9f68-723d1cf49700)

sama seperti menu bendahara, menu pengguna juga ada nomor yang bisa dipilih.

# penjelasan menu pengguna

1. Transaksi

![Screenshot 2024-10-15 051233](https://github.com/user-attachments/assets/9b328e80-8b3b-4b34-8bb6-01794661045d)

jika pengguna memilih pilihan 1, maka pengguna akan diarahkan untuk menginput bulan yang ingin ditransaksi kan. kemudian, pengguna akan diarahkan kembali untuk menginput jumlah kas yang yang akan dibayar. berikut untuk menampilkan kode nya

![Screenshot 2024-10-15 051701](https://github.com/user-attachments/assets/4430a092-7c3d-42b4-8a44-a1327c05f521)

2. Keluar Menu

jika bendahara memilih pilihan 5, maka program akan otomatis berhenti dan memulai dari awal. 

![Screenshot 2024-10-15 051822](https://github.com/user-attachments/assets/83938ba8-6198-4541-92ec-a1f4544a1112)

berikut untuk menampilkan kode nya

![Screenshot 2024-10-15 051944](https://github.com/user-attachments/assets/a95e98ff-0b77-482f-bc8d-3bbcd329bec2)
