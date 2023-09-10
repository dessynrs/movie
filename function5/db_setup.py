# import
import sqlite3

con = None
cur = None

# ====================================================
def setup():
    "Fungsi setup database awal."
    global con
    con = sqlite3.connect("data_pesanan_sql.db")
    global cur
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS transaction_table(
                nama_item TEXT NOT NULL, 
                jumlah_item REAL NOT NULL, 
                harga_per_item REAL NOT NULL,
                total_harga REAL NOT NULL,
                diskon REAL NOT NULL,
                harga_setelah_diskon REAL NOT NULL,
                kode_transaksi TEXT NOT NULL
                )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS customer_table(
                id_customer AUTOINCREMENT PRIMARY KEY,
                nama TEXT NOT NULL, 
                alamat TEXT NOT NULL, 
                kota TEXT NOT NULL,
                kode_pos TEXT NOT NULL,
                telepon TEXT NOT NULL,
                no_transaksi TEXT NOT NULL)""")
    


    return con, cur
    # sql = "DROP TABLE transaction"
    # cur.execute(sql)

# ====================================================
# def save_transaction(nama_item: str, 
#                      jumlah_item: float, 
#                      harga_per_item: float, 
#                      total_harga: float,
#                      diskon: float,
#                      harga_setelah_diskon: float,
#                      kode_transaksi: str):
    
#     # simpan ke database
#     cur.execute(f"""INSERT INTO transaction 
#                 VALUES ("
#                 {nama_item}", "{jumlah_item}", "{harga_per_item},
#                 {total_harga}", "{diskon}", "{harga_setelah_diskon},
#                 {kode_transaksi}")""")
    
#     con.commit()
    


# ====================================================
def save_customer(id_customer: int,
                  nama: str,
                  alamat: str,
                  kota: str,
                  kode_pos: str,
                  telepon: str,
                  no_transaksi: str):
    
    # simpan ke database
    cur.execute(f"""INSERT INTO customer 
                VALUES ("
                "{id_customer}", "{nama}", "{alamat},
                "{kota}", "{kode_pos}", "{telepon},
                "{no_transaksi}")""")
    
    con.commit()

# sql table = tabel transaction
# melakukan export dataframe ke bentuk sql
#df_checkout.to_sql('transaction', con, index = True, if_exists = 'replace', method = None) # if exists = 'append' kalo sdh ok




