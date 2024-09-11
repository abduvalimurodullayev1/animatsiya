import os
import shutil

fayl_turlari = {
    "rasmlar": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "hujjatlar": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "musiqalar": [".mp3", ".wav", ".ogg"],
    "videolar": [".mp4", ".avi", ".mov", ".mkv"],
    "arxivlar": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "dasturlar": [".exe", ".msi", ".apk", ".sh"]
}


def fayllarni_tartiblash(manba_papka):
    if not os.path.isdir(manba_papka):
        print(f"{manba_papka} papka emas, iltimos, to'g'ri papka kiriting.")
        return

    barcha_fayllar = os.listdir(manba_papka)

    for fayl in barcha_fayllar:
        fayl_yoli = os.path.join(manba_papka, fayl)

        if os.path.isfile(fayl_yoli):
            fayl_kengaytmasi = os.path.splitext(fayl)[1].lower()

            papka_topildi = False
            for papka_nomi, kengaytmalar in fayl_turlari.items():
                if fayl_kengaytmasi in kengaytmalar:
                    yangi_papka = os.path.join(manba_papka, papka_nomi)
                    os.makedirs(yangi_papka, exist_ok=True)
                    shutil.move(fayl_yoli, os.path.join(yangi_papka, fayl))
                    papka_topildi = True
                    print(f"{fayl} -> {yangi_papka}")
                    break

            if not papka_topildi:
                boshqa_papka = os.path.join(manba_papka, "boshqa")
                os.makedirs(boshqa_papka, exist_ok=True)
                shutil.move(fayl_yoli, os.path.join(boshqa_papka, fayl))
                print(f"{fayl} -> {boshqa_papka}")


if __name__ == '__main__':
    manba_papka = input("Fayllarni tartiblash kerak bo'lgan papka yo'lini kiriting: ")
    fayllarni_tartiblash(manba_papka)
