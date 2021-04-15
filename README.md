Imsakiyah Ramadan
===
Command line script untuk menggenerate file `ics` berisi jadwal imsakiyah/jadwal sholat. 
Script ini menggunakan API dari [PrayTimes.org](http://praytimes.org/ "PrayTimes.org")

Requirements
---
Script ini membutuhkan python versi 3.0+

Instalasi
---
- `git clone https://github.com/lantip/imsakiyah.git`
- `$cd imsakiyah`
- Jalankan `pip install  -r requirements.txt`

Penggunaan
---
Command line:

    $ python imsakiyah.py <lat> <lon> <startdate> <days> <method=Makkah>
    
    contoh: `python imsakiyah.py -7.797068 110.370529 2021-04-13 30 --option=+8`
    gunakan `--option=+8` untuk perhitungan model Muhammadiyah. Kosongkan untuk mengikuti perhitungan pemerintah.

### Metode: 
- **`Makkah`** (Umm Al-Qura University, Makkah) default
- `MWL` (Muslim World League)
- `ISNA` (Islamic Society of North America)
- `Egypt` (Egyptian General Authority of Survey)
- `Karachi` (University of Islamic Sciences, Karachi)
- `Tehran` (Institute of Geophysics, University of Tehran)
- `Jafari` (Shia Ithna-Ashari, Leva Institute, Qum).

Import ke Calendar
---
Setelah Anda menjalankan perintah di atas, sebuah file `ics` akan tergenerate.
Silakan buka apps `Calendar` di OSX, klik `File > Import` lalu pilih file hasil generate.

Catatan
---

Untuk me-reset calendar, silakan tutup app `Calendar`, buka `Finder`, klik `Go`, ketikkan `~/Library/Calendars/`. 
Hapus file:
	- Calendar Cache
	- Calendar Cache-shm
	- Calendar Cache-wal

Lalu `Empty Trash`

WARNING: LANGKAH INI AKAN MENGHAPUS SELURUH ISIAN CALENDAR ANDA
