import sqlite3
#database kütüphanesini import ediyoruz.
db = sqlite3.connect("veresiye.db")
yetki = db.cursor()
yetki.execute("CREATE TABLE IF NOT EXISTS Borçlular('Borçlu Adı','Borç Miktarı')")
#Borçlular adında bir veresiye tablosu oluşturuyoruz. 

def borcluekle():
    while True:
        isim = input("Borçlu İsim : ")
        borc = input("Borç Miktarı : ")
        yetki.execute(f"INSERT INTO Borçlular VALUES ('{isim}','{borc}')")
        db.commit()
        cevap = input("Borçlu Eklemeye Devam Etmek İstiyor Musunuz ? (E/H)".upper())
        if cevap == "E":
            continue
        else:
            break
#Borçlu ekle fonksiyonu oluşturuyoruz.
def borclugoruntule():
    yetki.execute("SELECT * FROM Borçlular")
    liste = yetki.fetchall()
    for i in liste:
        print(i)
    cvp = input("Yeni borçlu eklemek ister misin? E/H")
    if cvp == "E":
        borcluekle()
    else:
        print("Veresiye defterinden çıkılıyor, Kendinize iyi bakın...")
#Borçlu görüntüle fonksiyonunu oluşturuyoruz.
print("----------VERESİYE DEFTERİNE HOŞGELDİNİZ----------")
while True:
    menu = input("1 - Borçlu ekle \n2 - Borçlu görüntüle\n3 - Çıkış\n")
    if menu == "1":
        borcluekle()
    elif menu == "2":
        borclugoruntule()
    elif menu == "3":
        print("Veresiye defterinden çıkılıyor, Kendinize iyi bakın...") 
        break 
    else:
        print("Hatalı giriş yaptınız")