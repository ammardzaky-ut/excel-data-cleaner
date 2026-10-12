import pandas as pd
import sys

class OdooDataCleaner:
    """
    Script OOP untuk membersihkan dan menstandarisasi data Excel mentah
    agar siap diimpor ke modul Contacts/CRM Odoo.
    """
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file
        self.df = None

    def load_data(self):
        try:
            print(f"[*] Membaca data dari: {self.input_file}")
            # openpyxl bekerja di latar belakang untuk membaca file .xlsx
            self.df = pd.read_excel(self.input_file)
            print(f"[+] Berhasil memuat {len(self.df)} baris data mentah.")
        except FileNotFoundError:
            print(f"[!] Error: File '{self.input_file}' tidak ditemukan.")
            sys.exit(1)

    def clean_basic_structure(self):
        """Menghapus baris kosong sepenuhnya dan data duplikat."""
        print("[*] Menghapus baris kosong dan duplikat...")
        awal = len(self.df)
        
        self.df.dropna(how='all', inplace=True)
        self.df.drop_duplicates(inplace=True)
        
        akhir = len(self.df)
        print(f"[+] {awal - akhir} baris sampah/duplikat berhasil dibersihkan.")

    def standardize_text(self):
        """Merapikan format teks (Title Case) dan membersihkan spasi berlebih."""
        print("[*] Menstandarisasi format teks nama dan email...")
        
        if 'Nama Pelanggan' in self.df.columns:
            # Title Case (misal: "aLiCe sMiTh" menjadi "Alice Smith")
            self.df['Nama Pelanggan'] = self.df['Nama Pelanggan'].astype(str).str.strip().str.title()
        
        if 'Email' in self.df.columns:
            # Lowercase dan hapus spasi tak terlihat
            self.df['Email'] = self.df['Email'].astype(str).str.strip().str.lower()

    def format_phone_numbers(self):
        """Mengubah format telepon berantakan menjadi standar internasional +62."""
        print("[*] Merapikan format nomor telepon...")
        
        if 'Nomor Telepon' in self.df.columns:
            # Bersihkan spasi, strip (-), dan ".0" jika Excel membacanya sebagai float
            self.df['Nomor Telepon'] = self.df['Nomor Telepon'].astype(str).str.replace(r'\.0$', '', regex=True)
            self.df['Nomor Telepon'] = self.df['Nomor Telepon'].str.replace(r'[\s\-]', '', regex=True)
            
            def fix_phone(phone: str) -> str:
                if phone == 'nan' or not phone:
                    return ''
                if phone.startswith('0'):
                    return '+62' + phone[1:]
                elif phone.startswith('62'):
                    return '+' + phone
                elif not phone.startswith('+'):
                    return '+62' + phone
                return phone
                
            self.df['Nomor Telepon'] = self.df['Nomor Telepon'].apply(fix_phone)

    def export_data(self):
        """Mengekspor DataFrame bersih ke format CSV (Format Impor Default Odoo)."""
        print(f"[*] Mengekspor data bersih ke: {self.output_file}")
        self.df.to_csv(self.output_file, index=False)
        print("\n[+] EKSPOR SELESAI! Data siap diimpor ke Odoo tanpa error.")

    def run_pipeline(self):
        """Menjalankan seluruh alur pembersihan (Controller Method)."""
        self.load_data()
        if self.df is not None:
            self.clean_basic_structure()
            self.standardize_text()
            self.format_phone_numbers()
            self.export_data()

if __name__ == "__main__":
    print("=== Odoo Data Migration Preparation Tool ===\n")
    # Tentukan nama file sumber (Excel) dan file hasil (CSV)
    cleaner = OdooDataCleaner("data_mentah.xlsx", "data_siap_import.csv")
    cleaner.run_pipeline()