!! Readme TUGAS 6
1. Apa perbedaan antara synchronous request dan asynchronous request?
Synchronous request itu permintaan ke server yang harus ditunggu sampai selesai, jadi halaman atau proses lain akan berhenti dulu sampai server membalas. Kalau asynchronous request (seperti AJAX), permintaan dikirim ke server di belakang layar, jadi halaman tetap bisa dipakai tanpa harus reload atau nunggu lama.

2. Bagaimana AJAX bekerja di Django (alur request–response)?
AJAX di Django biasanya pakai fetch atau XMLHttpRequest dari JavaScript untuk kirim request ke endpoint Django (misal, url yang mengembalikan JSON). Django menerima request itu, proses data, lalu balas dengan response (biasanya JSON). Di sisi frontend, JavaScript akan terima response itu dan update tampilan sesuai data yang didapat, tanpa reload halaman.

3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
Keuntungannya, user experience jadi lebih baik karena halaman tidak perlu reload penuh setiap ada aksi (misal, lihat detail produk, submit form, dsb). Data bisa diambil atau dikirim secara dinamis, lebih cepat, dan interaktif. Selain itu, beban server dan bandwidth juga bisa lebih ringan karena hanya data yang dibutuhkan saja yang dikirim.

4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Pastikan selalu mengirim CSRF token di setiap request POST (bisa lewat header atau form data). Validasi input di backend tetap wajib, jangan hanya di frontend. Gunakan HTTPS supaya data tidak mudah disadap. Selain itu, response dari server sebaiknya tidak mengandung data sensitif, dan error handling harus baik supaya tidak membocorkan informasi penting.

5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
AJAX bikin website terasa lebih responsif dan modern. User tidak perlu menunggu reload halaman, loading state dan error bisa ditampilkan langsung di bagian tertentu, dan interaksi jadi lebih cepat. Contohnya di kode saya, detail produk diambil pakai AJAX dan loading/error state langsung muncul di halaman, jadi user tahu apa yang sedang terjadi tanpa harus pindah halaman.

---

!! Readme TUGAS 5
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Dalam CSS berlaku konsep cascading, yaitu aturan dievaluasi berdasarkan bobot dan urutan penulisan. Prioritas tertinggi diberikan pada deklarasi dengan !important, kemudian inline style pada elemen, disusul selector ID (#id), selector class, atribut, dan pseudo-class (.class, [attr], :hover), lalu selector elemen atau pseudo-element (div, ::after), dan terakhir universal selector (*). Jika bobotnya sama, aturan yang ditulis paling akhir akan menang. Prinsip ini memastikan style yang lebih spesifik atau terbaru akan diterapkan.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Responsive design penting karena menjamin tampilan web tetap nyaman digunakan di berbagai perangkat, dari layar ponsel hingga desktop, sehingga meningkatkan aksesibilitas, user experience, sekaligus mendukung SEO dan menurunkan bounce rate. Contoh implementasi baik ada pada Tokopedia atau Instagram yang menyesuaikan grid, tipografi, serta komponen berdasarkan ukuran layar, sedangkan banyak situs institusi lama kurang responsif karena tabel melebar, teks kecil, dan navigasi sulit di ponsel. Framework seperti Bootstrap membantu pengembangan responsive design dengan pendekatan mobile-first dan class siap pakai.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Margin, border, dan padding adalah tiga konsep utama dalam CSS box model. Margin mengatur jarak luar antar elemen agar tidak menempel, border adalah garis tepi yang membingkai elemen, sedangkan padding memberikan ruang antara konten dengan border sehingga isi elemen tampak lebih lega. Sebagai contoh, aturan .card { margin:16px; border:1px solid #ddd; padding:12px; } akan menghasilkan sebuah card dengan jarak ke elemen lain, garis tepi abu-abu tipis, dan ruang dalam yang cukup untuk konten.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox dan Grid adalah dua metode modern untuk mengatur layout. Flexbox bekerja secara satu dimensi, baik horizontal maupun vertikal, sehingga cocok untuk perataan elemen seperti navbar atau toolbar; misalnya dengan display:flex; justify-content:space-between; align-items:center;. Sebaliknya, Grid Layout dirancang untuk komposisi dua dimensi dengan baris dan kolom sehingga sangat efektif untuk membuat layout kompleks seperti galeri atau katalog produk, contohnya display:grid; grid-template-columns:repeat(auto-fit, minmax(240px,1fr)); gap:16px;. Keduanya saling melengkapi dalam membangun antarmuka web modern.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Pertama, saya membuka base.html dan menambahkan script source tailwindcss.com. Lalu saya menambahkan fungsi edit news dan delete news pada views.py dan menambahkan mereka ke urls.py. Setelah itu, pada main.html saya menambahkan fitur tombol edit dan delete. Sesudah itu, saya menambahkan navigation bar yang memiliki opsi Home, All Categories, Racket, Shoes, Accesories, Bags, dan Balls. Setelah itu, saya menambahkan konfigurasi static files pada aplikasi dan menambahkan static root, static file dirs, dan static url. Setelah itu, saya menambahkan global.css dimana saya menambahkan styling untuk design page saya dan menambahkan no-product.png. Setelah itu saya sesuaikan page register, login, menambahkan card_product.html, sesuaikan main.html, product_detail.html, create_product.html, serta edit_product.html. Setelah itu, saya membuat readme.

---
!! Readme TUGAS 4

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

Menurut saya, AuthenticationForm adalah form bawaan dari Django yang ada di django.contrib.auth.forms dan memang dipakai untuk menangani login. Fungsinya adalah mengecek apakah username yang dimasukkan ada di database, lalu memastikan password yang diberikan sesuai dengan user tersebut. Kalau cocok, maka user dianggap sudah tervalidasi dan bisa login. Kelebihan dari form ini adalah saya tidak perlu repot menulis validasi manual, karena Django sudah menyiapkan logikanya. Selain itu, AuthenticationForm sudah terintegrasi dengan sistem autentikasi Django, jadi bisa langsung dipakai bersama view login tanpa konfigurasi yang rumit. Form ini juga cukup mudah untuk diubah atau dikustomisasi sesuai kebutuhan. Kekurangannya, form ini hanya mendukung login berbasis username dan password secara default, jadi kalau aplikasi saya butuh login pakai email atau OTP, tetap harus saya modifikasi lagi. Dari sisi fleksibilitas untuk tampilan modern, kadang juga agak terbatas.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Kalau saya bedakan, autentikasi itu adalah proses untuk memastikan identitas user biasanya lewat username dan password, sedangkan otorisasi adalah langkah selanjutnya setelah identitas diverifikasi, yaitu menentukan hak akses apa saja yang boleh dilakukan user tersebut. Django sudah punya sistem bawaan untuk dua hal ini. Untuk autentikasi, ada modul django.contrib.auth dan form login bawaan. Setelah login, middleware AuthenticationMiddleware akan otomatis menambahkan informasi user ke dalam request, jadi saya bisa tahu siapa yang sedang login. Untuk otorisasi, Django menyediakan sistem permission dan groups yang bisa dipakai untuk mengatur level akses. Selain itu, ada juga decorator seperti @login_required atau @permission_required yang bisa langsung dipasang pada view tertentu supaya hanya user dengan akses yang sesuai yang bisa membuka halaman atau menjalankan fungsi tersebut.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Dalam konteks menyimpan state, cookies dan session punya cara kerja yang berbeda. Cookies disimpan di sisi client, yaitu di browser, sehingga tidak membebani server. Ini membuat cookies cocok untuk menyimpan data kecil yang perlu dipakai lintas request. Tapi karena cookies selalu dikirim setiap kali ada request ke server, ukurannya terbatas dan bisa menambah overhead. Selain itu, cookies bisa dilihat dan diubah langsung oleh user, jadi tidak aman untuk menyimpan data penting. Sementara itu, session disimpan di sisi server. Browser hanya menyimpan ID session di cookie, sedangkan datanya ada di server. Menurut saya, session lebih aman untuk menyimpan data sensitif seperti user_id dan lebih fleksibel karena bisa menyimpan data kompleks. Namun, session membuat server harus menyimpan data tambahan dan ada kebutuhan untuk menghapus session yang kadaluarsa. Kalau aplikasi saya punya skala besar, biasanya saya perlu pakai sistem tambahan seperti Redis supaya pengelolaan session tetap efisien.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Menurut saya jawabannya tidak sepenuhnya. Cookies bisa dicuri lewat serangan XSS, dicegat lewat man-in-the-middle attack, atau bahkan diubah sendiri oleh user melalui browser. Risiko besar yang sering muncul adalah session hijacking, di mana orang lain mencuri session ID lalu masuk seolah-olah sebagai user kita, serta serangan seperti session fixation atau CSRF. Django sendiri sudah menyiapkan beberapa proteksi. Misalnya, ada opsi SESSION_COOKIE_SECURE=True supaya cookies hanya bisa dikirim lewat HTTPS, lalu SESSION_COOKIE_HTTPONLY=True agar cookies tidak bisa diakses dari JavaScript. Django juga menyediakan SESSION_COOKIE_SAMESITE yang bisa diatur agar cookies tidak dipakai lintas domain sembarangan, sehingga lebih aman dari CSRF. Selain itu, Django otomatis menambahkan CSRF token di form POST dan juga punya fitur signed cookies supaya cookies tidak bisa dimodifikasi sembarangan. Jadi walaupun cookies punya risiko, Django sudah cukup membantu saya untuk mengamankannya.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pertama saya set dan aktifakn virtual environment dan membuka views.py dan menambahkan importUserCreationForm dan messages. Lalu saya tambahkan fungs register di views.py. Setelah itu saya membuat register.html under directory main.templates dan menambahkan url routing pada urls.py. saya lakukan hal yang sama untuk method login dengan menambahkan import AuthenticationForm, buat login_user method, login.html, dan menambahkan routing nya pada urls.py. Kemudian saya menambahkan method logout user pada views.py dan menambahkan buttonnya pada main.html. Setelah itu saya tambahkan di views.py import login_required dan menambahkan decorator diatas fungsi show_main dan show_product. Saya juga menambahkan method last_login dengan import datetime, HttpResponseRedirect, dan verse. Saya memanfaatkan request.COOKIES untuk menampilkan data tersebut dan ubah fungsi logout user untuk menghapus cookies last login setelah lakukan logout. Setelah itu saya buat objek user pada class Product dan migrate kembali. Saya juga sesuaikan method create_product untuk mengirimkan data siapa yang membuat product. Saya sesuaikan method show_main, main.html, dan product_detail.html agar sesuai. Setelah itu, saya git add-commit-push dan juga push ke PWS.