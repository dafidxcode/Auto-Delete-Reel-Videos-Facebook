import requests
import time

ACCESS_TOKEN = "AKSES TOKEN HALAMAN"  # Token akses untuk autentikasi ke API Facebook
PAGE_ID = "ID HALAMAN"  # ID halaman Facebook yang akan dioperasikan

def delay(seconds):
    """Menunggu selama jumlah detik yang ditentukan."""
    for remaining in range(seconds, 0, -1):
        print(f"   --> Silahkan Tunggu {remaining:02d} Detik               ", end='\r')  # Menampilkan waktu tunggu
        time.sleep(1)  # Menunggu selama 1 detik
    print()  # Untuk pindah ke baris baru setelah delay

def delete_videos(page_id, access_token):
    """Menghapus semua video dari halaman yang ditentukan."""
    url = f"https://graph.facebook.com/v18.0/{page_id}/videos?fields=id&access_token={access_token}"  # URL untuk mendapatkan daftar video
    response = requests.get(url)  # Mengirim permintaan GET untuk mendapatkan video
    videos = response.json().get("data", [])  # Mengambil data video dari respons

    for video in videos:
        video_id = video["id"]  # Mengambil ID video
        delete_url = f"https://graph.facebook.com/v18.0/{video_id}?access_token={access_token}"  # URL untuk menghapus video
        delete_response = requests.delete(delete_url)  # Mengirim permintaan DELETE untuk menghapus video
        print(f"Deleted {video_id}: {delete_response.json()}")  # Menampilkan hasil penghapusan video
        delay(10)  # Menunggu selama 10 detik sebelum menghapus video berikutnya

# Memanggil fungsi untuk menghapus video
delete_videos(PAGE_ID, ACCESS_TOKEN)  # Memanggil fungsi dengan ID halaman dan token akses
