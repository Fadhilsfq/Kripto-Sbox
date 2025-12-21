# Alat Analisis S-Box

Proyek ini menyediakan serangkaian alat analisis kriptografi untuk S-Box (Substitution Box). Alat-alat ini menghitung berbagai properti kriptografi dari S-Box, termasuk namun tidak terbatas pada:

- Strict Avalanche Criterion (SAC)
- Linear Approximation Probability (LAP)
- Nonlinearity
- Differential Uniformity
- Differential Approximation Probability (DAP)
- Entropy
- Bit Independence Criterion (BIC)

## Fitur

1. **Analisis S-Box**: Alat untuk menganalisis kekuatan dan properti kriptografi dari sebuah S-Box.
2. **Antarmuka Web Streamlit**: Antarmuka berbasis web untuk mengunggah, memproses, dan memvisualisasikan S-Box.

## Persyaratan

Pastikan Anda sudah menginstal hal-hal berikut:

- Python 3.x
- pip

Instal dependensi Python yang diperlukan:
```bash
pip install streamlit
pip install numpy
pip install pandas
pip install openpyxl
```

Untuk menjalankan aplikasi Streamlit
```bash
streamlit run main.py
```
atau
```bash
python -m streamlit run main.py
```

## Penggunaan
Unggah S-Box: Aplikasi Streamlit memungkinkan Anda untuk mengunggah S-Box dalam bentuk daftar 256 elemen. Anda dapat menempelkan S-Box langsung atau mengunggah file.

Pilih Analisis: Setelah S-Box diunggah, Anda dapat memilih berbagai opsi analisis untuk menghitung properti dari S-Box tersebut.

Lihat Hasil: Aplikasi akan menampilkan hasil dari setiap analisis, seperti SAC, LAP, entropy, dan lainnya.

## Metode Analisis
Berikut adalah metode analisis kriptografi yang termasuk dalam proyek ini:

1. Strict Avalanche Criterion (SAC)
Kriteria ini mengevaluasi seberapa banyak output berubah ketika setiap bit dari input dibalik.

2. Linear Approximation Probability (LAP)
Ini mengukur probabilitas bahwa sebuah pendekatan linear berlaku untuk S-Box.

3. Nonlinearity
Nonlinearity mengukur sejauh mana S-Box menyimpang dari fungsi linear.

4. Differential Uniformity
Ini mengukur keseragaman perbedaan antara input dan output dalam S-Box.

5. Differential Approximation Probability (DAP)
Ini mengukur probabilitas bahwa pendekatan diferensial berlaku untuk S-Box.

6. Entropy
Entropy dari S-Box memberi gambaran tentang jumlah informasi yang dimilikinya, yaitu seberapa tidak dapat diprediksi output-nya.

7. Bit Independence Criterion (BIC)
Kriteria ini mengevaluasi seberapa independen bit-bit dalam output ketika bit-bit dalam input dibalik.

## Contoh S-Box
Sebuah contoh S-Box 8-bit (256 elemen) dapat dianalisis dengan alat ini. Berikut adalah contoh input:

```math
\begin{bmatrix}
99 & 205 & 85 & 71 & 25 & 127 & 113 & 219 & 63 & 244 & 109 & 159 & 11 & 228 & 94 & 214 \\
77 & 177 & 201 & 78 & 5 & 48 & 29 & 30 & 87 & 96 & 193 & 80 & 156 & 200 & 216 & 86 \\
116 & 143 & 10 & 14 & 54 & 169 & 148 & 68 & 49 & 75 & 171 & 157 & 92 & 114 & 188 & 194 \\
121 & 220 & 131 & 210 & 83 & 135 & 250 & 149 & 253 & 72 & 182 & 33 & 190 & 141 & 249 & 82 \\
232 & 50 & 21 & 84 & 215 & 242 & 180 & 198 & 168 & 167 & 103 & 122 & 152 & 162 & 145 & 184 \\
43 & 237 & 119 & 183 & 7 & 12 & 125 & 55 & 252 & 206 & 235 & 160 & 140 & 133 & 179 & 192 \\
110 & 176 & 221 & 134 & 19 & 6 & 187 & 59 & 26 & 129 & 112 & 73 & 175 & 45 & 24 & 218 \\
44 & 66 & 151 & 32 & 137 & 31 & 35 & 147 & 236 & 247 & 117 & 132 & 79 & 136 & 154 & 105 \\
199 & 101 & 203 & 52 & 57 & 4 & 153 & 197 & 88 & 76 & 202 & 174 & 233 & 62 & 208 & 91 \\
231 & 53 & 1 & 124 & 0 & 28 & 142 & 170 & 158 & 51 & 226 & 65 & 123 & 186 & 239 & 246 \\
38 & 56 & 36 & 108 & 8 & 126 & 9 & 189 & 81 & 234 & 212 & 224 & 13 & 3 & 40 & 64 \\
172 & 74 & 181 & 118 & 39 & 227 & 130 & 89 & 245 & 166 & 16 & 61 & 106 & 196 & 211 & 107 \\
229 & 195 & 138 & 18 & 93 & 207 & 240 & 95 & 58 & 255 & 209 & 217 & 15 & 111 & 46 & 173 \\
223 & 42 & 115 & 238 & 139 & 243 & 23 & 98 & 100 & 178 & 37 & 97 & 191 & 213 & 222 & 155 \\
165 & 2 & 146 & 204 & 120 & 241 & 163 & 128 & 22 & 90 & 60 & 185 & 67 & 34 & 27 & 248 \\
164 & 69 & 41 & 230 & 104 & 47 & 144 & 251 & 20 & 17 & 150 & 225 & 254 & 161 & 102 & 70 \\
\end{bmatrix}
```
