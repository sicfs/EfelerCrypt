import hashlib

import os
import os.path
from pathlib import Path

import time
import datetime

#yardimci metodlar
#---------------------------------------------------------------------------------------------

#dosyalarin dogruluk kontrolleri icin
def getHashFromFile(hedefDosya,yontem="md5"):
        #https://www.joelverhagen.com/blog/2011/02/md5-hash-of-file-in-python/
        if(yontem.lower() == "md5"):
                with open(hedefDosya, 'rb') as fh:
                        m = hashlib.md5()
                        while True:
                            data = fh.read(8192)
                            if not data:
                                break
                            m.update(data)
                        return m.hexdigest()
                
        elif(yontem.lower() == "sha"):
                with open(hedefDosya, 'rb') as fh:
                        m = hashlib.sha256()
                        while True:
                            data = fh.read(8192)
                            if not data:
                                break
                            m.update(data)
                        return m.hexdigest()

#tek yonlu sifrelemeler icin
def getHashFromStr(metin,yontem="md5"):
        metin = metin.encode("utf-8")
        if(yontem.lower() == "md5"):
                return hashlib.md5(metin).hexdigest()
        elif(yontem.lower() == "sha"):
                return hashlib.sha256(metin).hexdigest()
                
def dosyaVarMi(dosyaURL):
        return os.path.isfile(dosyaURL)

def sifreUygun(sifre):
        sifre = str(sifre)
        return len(sifre) > 6 and len(sifre) < 15 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#test-----------------------------------------------------------------------------------------
def textHash():
        print(getHashFromFile("metin.txt"))
        print(getHashFromFile("orjinal.txt"))
        print(getHashFromStr("fc"))
        print(getHashFromStr("fc","sha"))

        print(sifreUygun(123))
        print(sifreUygun("asdsdasdsd"))
        print(sifreUygun(1233211234))
        print(sifreUygun(True))
        print(sifreUygun("123456"))
        
        print (bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
        print (bcolors.FAIL + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
        print (bcolors.OKBLUE + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
        print (bcolors.FAIL + bcolors.BOLD + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------



def mainMenu():
        ekran = """***************
        #İşelemler:
        #1-) Sezar Şifreleme
        #2-) Sezar Şifreleme Çözme
        #3-) Bitsel Şifreleme
        #4-) Bitsel Şifreleme Çözme
        #5-) Cikis
        *************************
        """
        while True:
        
                print(ekran)
                secim = input("Yapmak istediginiz islemin numarasini giriniz: ")
                
                if (secim == "1"):
                        time.sleep(2)
                        print("Sezar sifreleme")
                        
                        kaynak = input("Sifrelenecek dosya: ")
                        if(dosyaVarMi(kaynak) == False):
                                print (bcolors.WARNING + "Sifrelencek dosya mevcut degil!" + bcolors.ENDC)
                                print (bcolors.WARNING + "islem sonlandiriliyor..." + bcolors.ENDC)
                                continue
                        
                        hedef = input("Yeni dosyanin adi: ")
                        
                        sifre = input("Sifre: ")
                        if(sifreUygun(sifre) == False):
                                print (bcolors.WARNING + "Sifre 6 karakterden az 15 karakterden falza olmamalıdır..." + bcolors.ENDC)
                                print (bcolors.WARNING + "islem sonlandiriliyor..." + bcolors.ENDC)
                                continue
                        
                        print("islem baslatiliyor...")
                        time.sleep(2)
                        
                        simdi = datetime.datetime.today()
                        
                        sifreleSezarFromFile(kaynak,hedef,sifre)
                        
                        sonra = datetime.datetime.today()
                        fark = sonra - simdi
                        print("islem tamamlandi.")
                        print("islem {} saniye surdu".format(fark.seconds))
                                
                elif(secim == "2"):
                        time.sleep(2)
                        print("Sezar sifre cozme")
                        
                        kaynak = input("Sifrelenmis dosya: ")
                        if(dosyaVarMi(kaynak) == False):
                                print (bcolors.WARNING + "Dosya mevcut degil!" + bcolors.ENDC)
                                print (bcolors.WARNING + "islem sonlandiriliyor..." + bcolors.ENDC)
                                continue
                        
                        hedef = input("Yeni dosyanin adi: ")
                        
                        sifre = input("Sifre: ")
                        if(sifreUygun(sifre) == False):
                                print (bcolors.WARNING + "Sifre 6 karakterden az 15 karakterden falza olmamalıdır..." + bcolors.ENDC)
                                print (bcolors.WARNING + "islem sonlandiriliyor..." + bcolors.ENDC)
                                continue
                        
                        print("islem baslatiliyor...")
                        time.sleep(2)
                        
                        simdi = datetime.datetime.today()
                        
                        sifreCozSezarFromFile(kaynak,hedef,sifre)
                        
                        sonra = datetime.datetime.today()
                        fark = sonra - simdi
                        print("islem tamamlandi.")
                        print("islem {} saniye surdu".format(fark.seconds))
                        
                        
                elif(secim == "3"):
                        time.sleep(2)
                        print("Bitsel sifreleme")
                        
                        kaynak = input("Sifrelenecek dosya: ")
                        if(dosyaVarMi(kaynak) == False):
                                print (bcolors.WARNING + "Sifrelencek dosya mevcut degil!" + bcolors.ENDC)
                                print (bcolors.WARNING + "islem sonlandiriliyor..." + bcolors.ENDC)
                                continue
                        
                        hedef = input("Yeni dosyanin adi: ")
                        
                        sifre = input("Sifre: ")
                        if(sifreUygun(sifre) == False):
                                print (bcolors.WARNING + "Sifre 6 karakterden az 15 karakterden falza olmamalıdır..." + bcolors.ENDC)
                                print (bcolors.WARNING + "islem sonlandiriliyor..." + bcolors.ENDC)
                                continue
                        
                        print("islem baslatiliyor...")
                        time.sleep(2)
                        
                        simdi = datetime.datetime.today()
                        
                        sifreleBitsel(kaynak,hedef,sifre)
                        
                        sonra = datetime.datetime.today()
                        fark = sonra - simdi
                        print("islem tamamlandi.")
                        print("islem {} saniye surdu".format(fark.seconds))
                         
                        break
                elif(secim == "4"):
                        time.sleep(2)
                        print("Bitsel sifre cozme")
                        
                        kaynak = input("Sifrelenmis dosya: ")
                        if(dosyaVarMi(kaynak) == False):
                                print (bcolors.WARNING + "Dosya mevcut degil!" + bcolors.ENDC)
                                print (bcolors.WARNING + "islem sonlandiriliyor..." + bcolors.ENDC)
                                continue
                        
                        hedef = input("Yeni dosyanin adi: ")
                        
                        sifre = input("Sifre: ")
                        if(sifreUygun(sifre) == False):
                                print (bcolors.WARNING + "Sifre 6 karakterden az 15 karakterden falza olmamalıdır..." + bcolors.ENDC)
                                print (bcolors.WARNING + "islem sonlandiriliyor..." + bcolors.ENDC)
                                continue
                        
                        print("islem baslatiliyor...")
                        time.sleep(2)
                        
                        simdi = datetime.datetime.today()
                        
                        sifreCozBitsel(kaynak,hedef,sifre)
                        
                        sonra = datetime.datetime.today()
                        fark = sonra - simdi
                        print("islem tamamlandi.")
                        print("islem {} saniye surdu".format(fark.seconds))
                         
                        break
                else:
                        print("Hatali islem secimi")
                        print("Programdan cikiliyor...")
                        break
                        
#menuye eklenicek kontroller
#sifre 6 karakterden az 16 karakterden fazla olamaz

#zaman bas-son

#sezar sifreleme--------------------------------------------------------------------
#verilen bit str bilgisini anahtarla sezar sifreleme yontemi kullanarak sifreler

def sifreleSezarFromFile(kaynakDosyaUrl,hedefDosyaURL,sifre):
        oku = okuTXT(kaynakDosyaUrl)
        sifreliMetin = sifreleSezar(oku,sifre)
        yazTXT(hedefDosyaURL,sifreliMetin)
        
def sifreCozSezarFromFile(kaynakDosyaUrl,hedefDosyaURL,sifre):
        oku = okuTXT(kaynakDosyaUrl)
        cozulmusMetin = sifreCozSezar(oku,sifre)
        yazTXT(hedefDosyaURL,cozulmusMetin)
        
        
def sifreleSezar(metin,sifre):
        sonuc = kaydirma(sifre)
        #liste = list(metin)
        asciiListe = list(map(ord,metin))
        i = 0
        while(i<len(asciiListe)):
                asciiListe[i] = asciiListe[i] + sonuc
                i = i + 1     
        return ''.join(list(map(chr,asciiListe)))

def sifreCozSezar(sifMetin,sifre):
        sonuc = kaydirma(sifre)
        liste = list(sifMetin)
        asciiListe = list(map(ord,liste))
        i = 0
        while(i<len(asciiListe)):
                asciiListe[i] = asciiListe[i] - sonuc
                i = i + 1
        return ''.join(list(map(chr,asciiListe)))
        
#ortak islemler fonksiyon yapildi
def kaydirma(sifre):
        lSifre = list(sifre)
        i = 0
        sonuc = 0
        while(i<len(lSifre)):
                 sonuc += ord(lSifre[i])
                 i = i + 1       
        sonuc = sonuc%17 #sadece sayiyi kucultmek icin uyduruldu
        return sonuc

def yazTXT(hedefDosyaURL,veri):
        with open(hedefDosyaURL,"w") as dosya:
                dosya.write(veri)
                return True        

def okuTXT(kaynakDosyaURL):
        #dosya mevcut mu? kontrolu gerekli...
        str_listesi = []
        with open(kaynakDosyaURL,"r") as dosya:
                str_listesi = list(dosya.read())
        return str_listesi

#test metodlari
#-------------------------------------------------------------------------------
def testSezar():
        metin = list("fatih öçşğiü *_-çÇÖŞÜĞİı;,.:\}][{¾½$#£>><!'^+%&/()=?_#")
        sifre = "zxczxc"
        sifMetin = sifreleSezar(metin,sifre)
        print(sifMetin)
        orjinalMetin = sifreCozSezar(sifMetin,sifre) 
        print(orjinalMetin)
        
        sifreleSezarFromFile("metin.txt","hedef.txt","sifre")
        sifreCozSezarFromFile("hedef.txt","orjinal.txt","sifre")

#testSezar()
#--------------------------------------------------------------------------------
#-------------------------------sezar sifreleme----------------------------------



#bitsel sifreleme----------------------------------------------------------------
def sifreleBitsel(kaynakDosyaURL,hedefDosyaURL,sifre):
        byteArray = okuBIN(kaynakDosyaURL)
        sifre = karistirma(sifre)
        
        bos_dizi = bytearray(b'')
        for i in range(len(byteArray)):          
                byte_sifre = ord(sifre)
                cikti = byteArray[i] ^ byte_sifre
                bos_dizi.append(cikti)
        yazBIN(hedefDosyaURL,bos_dizi)
        return True
        
        
def sifreCozBitsel(kaynakDosyaURL,hedefDosyaURL,sifre):
        sifreleBitsel(kaynakDosyaURL,hedefDosyaURL,sifre)
        return True


def okuBIN(kaynakDosyaURL):
        with open(kaynakDosyaURL,"rb") as binary_file:
                data = binary_file.read()
                return data        
        
def yazBIN(hedefDosyaURL,byteArray):
        with open(hedefDosyaURL,"wb") as dosya:
                dosya.write(byteArray)
                return True

def karistirma(sifre):
        #add salt
        sifre = getHashFromStr(sifre)
        ":-@".join(sifre)
        "%&_^+".join(sifre)
        #--------
        lSifre = list(sifre)
        i = 0
        sonuc = 0
        while(i<len(lSifre)):
                 sonuc += ord(lSifre[i])
                 i = i + 1       
        sonuc = sonuc%17 #sadece sayiyi kucultmek icin uyduruldu
        return sonuc.to_bytes(1,byteorder="big",signed=True)


#test----------------------------------------------------------------------------


#sifreleBitsel("a.mp3","asd.mp3","123")
#sifreCozBitsel("asd.mp3","cikti.mp3","123")

#sifreleBitsel("a.mp3","asd.mp3","sifrelelele")
#sifreCozBitsel("asd.mp3","cikti.mp3","sifrelelele")



#print(getHashFromFile("a.mp3"))
#print(getHashFromFile("asd.mp3"))
#print(getHashFromFile("cikti.mp3"))


#sifreleBitsel("metin.txt","asd.txt","123")
#sifreCozBitsel("asd.txt","cikti.txt","123")

#print(getHashFromFile("metin.txt"))
#print(getHashFromFile("asd.txt"))
#print(getHashFromFile("cikti.txt"))


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------




