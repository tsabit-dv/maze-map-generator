# Labirin Generator

Program ini menghasilkan labirin secara acak, dan menggambarnya menggunakan pustaka **Matplotlib** di Python. Labirin yang dihasilkan berupa matriks 2D yang kemudian divisualisasikan dengan menandai titik masuk dan keluar.

## Fitur

- Membuat labirin acak berbentuk persegi dengan ukuran yang ditentukan.
- Menampilkan labirin menggunakan Matplotlib, dengan titik masuk dan keluar yang jelas.
- Program ini cocok digunakan untuk pendidikan dan permainan logika untuk anak-anak.

## Tampilan Labirin

Berikut adalah contoh tampilan labirin yang dihasilkan oleh program ini:

![Contoh Labirin](https://img.freepik.com/premium-vector/education-logic-game-find-right-way-labyrinth-conundrum-kids-isolated-simple-square-maze_329400-10.jpg)

## Penjelasan Kode

### 1. **Fungsi `buat_labirin(w, h)`**

Fungsi ini digunakan untuk menghasilkan labirin acak dengan ukuran **`w`** (lebar) dan **`h`** (tinggi). Berikut adalah cara kerjanya:

- Labirin dimulai dengan mengisi semua sel dengan `1` (tembok).
- Fungsi `gali_jalur(x, y)` akan digunakan untuk membuat jalur (menandai `0`) dari titik masuk hingga titik keluar menggunakan metode rekursif.
- Arah jalur digabungkan secara acak untuk meningkatkan variasi labirin yang dihasilkan.

### 2. **Fungsi `gali_jalur(x, y)`**

Fungsi ini adalah fungsi rekursif yang akan menggali jalur labirin. Fungsi ini bekerja dengan cara:
- Memilih arah secara acak dari titik yang sedang diproses.
- Jika arah tersebut mengarah ke tempat yang valid (dalam batas labirin dan belum digali), maka membuat jalur dengan menandai `0` dan melanjutkan proses ke titik tersebut.

### 3. **Penentuan Titik Masuk dan Keluar**

- Titik masuk berada di koordinat `(1, 0)`, yaitu di bagian atas kiri labirin.
- Titik keluar berada di koordinat `(h - 1, w - 2)`, yaitu di bagian bawah kanan labirin.
## Instalasi

Untuk menjalankan program ini, Anda membutuhkan Python dan beberapa pustaka:

1. Pastikan Anda memiliki Python versi 3 keatas terinstal.
2. Instal pustaka yang dibutuhkan dengan menjalankan perintah berikut:

```bash
pip install numpy matplotlib
