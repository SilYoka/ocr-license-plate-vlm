
# OCR Plat Nomor Indonesia dengan Visual Language Model (VLM)

Proyek ini dibuat sebagai bagian dari tugas akhir mata kuliah **Computer Vision (RE604)**, Program Studi Teknik Robotika, Semester Genap 2024/2025.

## 🎯 Tujuan Proyek

Melakukan Optical Character Recognition (OCR) terhadap gambar plat nomor kendaraan Indonesia menggunakan **Visual Language Model (VLM)** seperti LLaVA, yang dijalankan secara lokal menggunakan **LMStudio**.

Evaluasi hasil dilakukan menggunakan **Character Error Rate (CER)**.

---

## 🗂️ Struktur Folder

```
project_ocr_vlm/
├── images/Indonesian License Plate Dataset/images/test/  # Gambar dari Kaggle
├── ground_truth.csv          # Label jawaban benar
├── run_ocr.py                # Script utama OCR + evaluasi
├── result.csv                # Hasil prediksi dan skor CER
```

---

## ⚙️ Cara Menjalankan

### 1. Aktifkan LMStudio
- Jalankan LMStudio dan pilih model multimodal (misal `llava-llama-3-8b`)
- Pastikan tersedia di endpoint: `http://localhost:1234/v1/chat/completions`

### 2. Install Dependency
```bash
pip install requests pandas python-Levenshtein pillow
```

### 3. Jalankan Script
```bash
python run_ocr.py
```

Script akan membaca semua gambar di folder `test`, kirim ke VLM, lalu menyimpan hasil ke `result.csv`.

---

## 🧪 Evaluasi Akurasi

Karakter Error Rate (CER) dihitung menggunakan formula:

```
CER = (S + D + I) / N
```

- S = jumlah karakter salah (substitusi)
- D = karakter dihapus (deletion)
- I = karakter ditambah (insertion)
- N = jumlah karakter di jawaban benar

---

## 📦 Dataset

Dataset diambil dari:
[Kaggle: Indonesian License Plate Dataset](https://www.kaggle.com/datasets/juanthomaswijaya/indonesian-license-plate-dataset)

Hanya folder `test` yang digunakan untuk inference.

---

## 📸 Prompt yang Digunakan ke VLM

```
What is the license plate number shown in this image? Respond only with the plate number.
```

---

## 📬 Kontak

Silakan hubungi saya untuk pertanyaan atau kolaborasi lebih lanjut.

---

&copy; 2025 | Tugas Akhir Computer Vision - Teknik Robotika
