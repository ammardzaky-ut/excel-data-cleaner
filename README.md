# ERP Data Cleansing Tool (Pandas & OOP)

An enterprise-grade Python script designed to automate the cleaning and standardization of raw Excel data for seamless ERP (e.g., Odoo) migration.

## Business Value & Features

When migrating legacy data to a new ERP system, raw spreadsheets often contain formatting errors that trigger import failures. This tool resolves those bottlenecks through:
* **Data Integrity:** Automatically identifies and removes completely empty rows and duplicate entries.
* **Text Standardization:** Formats customer names to Title Case and sanitizes email addresses (lowercased and stripped of hidden spaces).
* **Phone Number Formatting:** Converts irregular local phone numbers into a standardized international format (e.g., `+62` for Indonesia) to ensure compatibility with CRM/WhatsApp modules.
* **OOP Architecture:** Built with a clean, scalable Object-Oriented structure utilizing the `pandas` and `openpyxl` data science libraries.

## How to Run

1. Ensure Python 3.x is installed.
2. Install the required dependencies:
   ```bash
   pip install pandas openpyxl
   ```
3. Place your raw data inside the project folder as data_mentah.xlsx.
4. Execute the script:
    ```bash
    python data_cleaner.py
    ```

# Example Output (CLI Logs)

```bash
=== Odoo Data Migration Preparation Tool ===

[*] Membaca data dari: data_mentah.xlsx
[+] Berhasil memuat 5 baris data mentah.
[*] Menghapus baris kosong dan duplikat...
[+] 2 baris sampah/duplikat berhasil dibersihkan.
[*] Menstandarisasi format teks nama dan email...
[*] Merapikan format nomor telepon...
[*] Mengekspor data bersih ke: data_siap_import.csv

[+] EKSPOR SELESAI! Data siap diimpor ke Odoo tanpa error.
```
# Development Note

*Developed as a portfolio piece to demonstrate Techno-Functional capabilities in handling real-world data migration scenarios for ERP implementations. By automating data preparation, this tool eliminates manual formatting bottlenecks in Excel.*

# Author

Created by Dzaky