1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step :  

Pertama saya membuat folder lokal bernama tugas-2pbp untuk menampung proyek. Dari terminal, saya masuk ke folder tersebut lalu mengaktifkan virtual environment Python sesuai arahan dari tutorial 0. Setelah itu saya membuat file requirements.txt dan melakukan instalasi dependensi melalui terminal agar Django serta kebutuhan lain siap digunakan.  

Setelah environment installed, saya menjalankan perintah untuk membuat proyek Django baru. Saya juga menambahkan file .env dan .env.prod untuk konfigurasi environment, khususnya untuk memisahkan pengaturan development dan production. Pada settings.py, saya memuat variabel dengan load_dotenv, menambahkan domain PWS pada ALLOWED_HOSTS, serta menyesuaikan konfigurasi database.  

Langkah berikutnya adalah melakukan makemigrations dan migrate supaya database terbentuk dengan baik. Setelah itu saya membuat repository GitHub, menambahkan .gitignore, lalu menghubungkan proyek lokal dengan repository tersebut dan menjaga pengembangan pada branch utama.  

Setelah repository siap, saya melakukan konfigurasi deployment pada PWS dan menambahkan domain PWS (`https://i-gusti411-tugas2.pbp.cs.ui.ac.id/`) ke ALLOWED_HOSTS. Setelah itu saya membuat aplikasi main dengan python3 manage.py startapp main, mendaftarkannya di INSTALLED_APPS, serta menambahkan folder templates untuk menampung HTML.  

Saya kemudian mengimplementasikan model Product sesuai ketentuan tugas, menjalankan migrasi ulang, lalu membuat fungsi pada views.py untuk menghubungkan data ke template. Setelah itu saya mengatur routing pada urls.py di level aplikasi maupun proyek untuk menampilkan halaman show_main. Terakhir, saya melakukan commit dan push agar kode tersimpan di GitHub dan push pada PWS agar tampil pada web.

---

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.  

Alur kerjanya adalah sebagai berikut: Web browser (client) mengirimkan HTTP request ke server Django. Request tersebut akan diproses oleh urls.py untuk mencocokkan pola URL. Jika cocok, Django akan memanggil fungsi atau class yang ada di views.py. Apabila view membutuhkan data, maka views.py akan berkomunikasi dengan models.py untuk mengambil data dari database. Hasilnya dikembalikan ke view, lalu view mengolah data tersebut menjadi context dan merender template HTML. Template akan menampilkan data dengan struktur yang rapi, dan Django mengembalikan response HTML ke browser.  

- urls.py bertindak sebagai code yang memetakan URL ke fungsi view.  
- views.py mengatur logika apa yang harus dilakukan ketika URL dipanggil.  
- models.py berperan sebagai penghubung antara view dan database.  
- HTML template digunakan sebagai tampilan akhir yang akan disajikan ke pengguna.  

---

3. Jelaskan peran settings.py dalam proyek Django!  
settings.py merupakan pusat konfigurasi dalam proyek Django. File ini menyimpan informasi penting seperti daftar aplikasi yang digunakan (INSTALLED_APPS), pengaturan database, konfigurasi security, template, middleware, hingga variabel environment. Tanpa settings.py, proyek tidak akan bisa berjalan dengan baik karena file ini yang mengatur bagaimana Django harus bekerja di development maupun production.

---

4. Bagaimana cara kerja migrasi database di Django?  
Migrasi database dijalankan ketika kita membuat atau mengubah model pada models.py. Pertama, perintah makemigrations digunakan untuk membuat catatan perubahan dalam bentuk file migrasi. File ini berisi instruksi Python yang menjelaskan apa yang berubah, misalnya membuat tabel baru, menambah kolom, atau menghapus field.  

Setelah file migrasi terbentuk, perintah migrate dijalankan untuk mengeksekusi instruksi tersebut ke dalam database. Django juga menyimpan catatan migrasi yang sudah pernah dijalankan dalam tabel django_migrations, sehingga status migrasi dapat dilacak dengan baik. Dengan cara ini, database dan kode tetap sinkron.

---

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?  
Menurut saya Django sangat cocok untuk pemula karena framework ini memiliki banyak fitur penting yang sudah tersedia sejak awal tanpa harus menambahkan library tambahan. Alurnya jelas, aman, dan terstruktur, sehingga mudah dipelajari oleh mahasiswa yang baru pertama kali membuat aplikasi web. Selain itu, karena Django berbasis Python, sintaksnya lebih ramah bagi pemula dibandingkan framework lain. Dokumentasinya lengkap dan komunitasnya luas sehingga memudahkan saat belajar.

---

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?  
Sejauh ini pengalaman saya bersama asdos di tutorial 1 sangat baik. Penjelasan yang diberikan jelas dan membantu saya memahami konsep yang awalnya membingungkan. Tidak hanya memberi arahan, tapi asisten dosen juga menjelaskan manfaat setiap langkah untuk kebutuhan ke depannya sehingga saya jadi lebih mengerti konteksnya. Terima kasih banyak kakak asdos.
