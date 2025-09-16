1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?  

Data delivery adalah proses mengirim, menerima, dan menyajikan data dari satu komponen ke komponen lain (server ke client dan sebaliknya, antar users, dsb.) secara cepat, aman, dan reliabel. Kita membutuhkannya karena:  

- Tanpa pengantaran data yang baik, pengguna tidak dapat melihat konten, produk, atau hasil proses secara real-time.  
- Kami butuh konsistensi dan perlu menjaga agar data yang tampil di UI sama dengan state pada server (contoh: transaksi, stok, status pesanan).  
- Kita juga perlukan untuk kinerja dan efisiensi sistem seperti caching, cdn, dan protokol yang efisien, waktu muat menjadi cepat dan pengalaman pengguna meningkat.  
- Terakhir, juga untuk keamanan seperti data sensitif (akun, pembayaran) perlu dikirim dengan enkripsi dan otentikasi agar tidak disadap atau dimanipulasi.  

---

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?  

“Lebih baik” itu bergantung kebutuhan. Menurutku lebih baik menggunakan JSON. Dalam praktik web modern, JSON lebih populer karena:  
- Ia bersifat ringkas dan mudah dibaca dengan struktur lebih pendek, hemat bandwidth.  
- Ia native di JavaScript jadi langsung di-parse/dipakai di browser tanpa konversi rumit.  
- Ia ada kinerja parsing jadi umumnya lebih cepat dan sederhana dibanding XML.  
- Ia memiliki ekosistem di hampir semua framework API, frontend, dan tool modern mengutamakan JSON.  

Kapan XML tetap berguna? Saat butuh metadata kaya (atribut), skema formal yang ketat (XSD), dokumen berstruktur kompleks, atau interoperabilitas dengan sistem lama/enterprise.  

---

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?  

`is_valid()` memicu validasi form: memeriksa field wajib, tipe data, batas nilai, unique constraint (via model form), hingga validasi kustom. Jika valid, `cleaned_data` tersedia agar data aman digunakan/disimpan. Kita membutuhkan method is_valid untuk:  
- Menjaga integritas data sebelum ke database.  
- Mencegah error runtime akibat format/tipedata salah.  
- Mencegah input berbahaya (mis. script injection) melalui mekanisme cleaning/validation.  

---

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkannya? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?  

`csrf_token` melindungi dari Cross-Site Request Forgery (CSRF) dengan memastikan setiap POST berasal dari halaman sah milik aplikasi (bukan dari situs lain). Tanpa token:  
- Penyerang dapat membuat halaman luar yang diam-diam mengirimkan form ke aplikasi saat user sedang login.  
- Aksi berbahaya bisa terjadi tanpa sepengetahuan user (misal ganti password, transaksi, hapus data).  

Dengan token unik per sesi/permintaan, request palsu dari domain lain akan ditolak karena tidak memiliki token valid.  

---

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).  

Berikut langkah yang saya lakukan di repo ini:  

- Tahap implementasi dimulai membuat folder templates pada root project yang berisi base.html dan edit settings.py untuk include 'DIRS' ke templates.
- Kemudian dilakukan penyesuaian pada file main.html utama untuk menyusun tampilan aplikasi (pakai extends base.html dan block content)
- Selanjutnya, membuat forms.py untuk buat struktur input, menambahkan method showcase nya pada views.py.
- Pada saat yang sama membuat create_product.html dan product_detail.html dan edit urls.py menyesuaikannya. Lalu buka settings.py dan tambahkan CSRF trusted origins.
- Selanjutnya di views.py saya tambahkan method show xml, xmlbyid, json, dan jsonbyid dan menambahkan routing masing masing pada urls.py pada main.
- Terakhir saya lakukan pengujian end-point JSON/XML (lewat Postman) untuk memastikan data ter-deliver dengan benar.  

Catatan: untuk design html saya memanfaatkan AI untuk menghias tampilan antarmuka (diperbolehkan oleh ibu Ilma)

---

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?  

So far so good, terima kasih banyak kakak asdos atas semua bimbingan dan bantuannya sejauh ini. Sukses juga untuk studiesnya ya kak :D
