#!/usr/bin/env python3
# Ebedi Kırmızı Işık Simülatörü (Yeşil denemesi)
# Bu kod gerçekten çalışır. Yeşil ışık hiç yanmaz.

import time
import random
import sys

SIKAYETLER = [
    "Kırmızı yanıyor abi, yeşil nerede?",
    "Bu ışık yemin ederim bana takıldı.",
    "Trafik polisi gelse de yeşil yaksın diye bekliyorum.",
    "Belki de ışık arızalandı, ama arıza da kırmızı.",
    "Yeşil ışık tatile çıkmış, dönüş tarihi belli değil.",
    "Bu ışık bana 'dur' diyor, ben de duruyorum, sonsuza kadar.",
    "Komşu ışık yeşil yandı, bizimki kıskandı.",
    "Belki de ben kırmızıyım, ışık değil.",
    "Trafik ışığı felsefe yapıyor: 'Durmak da bir harekettir.'",
    "Yeşil ışık özel şoförle gelmiş, bize gelmemiş."
]

def ebedi_kirmizi():
    print("\ud83d\udea6 Ebedi Kırmızı Işık Simülatörü başladı...")
    print("Yeşil ışık hiç yanmayacak. Alış.")
    print("Ctrl+C ile kaçabilirsin ama ışık kaçmaz.\n")
    
    sayac = 0
    while True:
        sayac += 1
        sikayet = random.choice(SIKAYETLER)
        print(f"[{sayac}] KIRMIZI: {sikayet}")
        time.sleep(random.uniform(1.5, 4.0))
        
        # Yeşil ışık denemesi (başarısız)
        if sayac % 50 == 0:
            print("   → YEŞİL denendi... Olmadı. Yine kırmızı.")
        
        if sayac % 10 == 0:
            print("   → Yeşil ışık kontrol edildi: Hala yok. Sürpriz yok.")
        
        # Gizli not: Bazen trafik de böyle, herkes kendi ışığını bekler.

if __name__ == "__main__":
    try:
        ebedi_kirmizi()
    except KeyboardInterrupt:
        print("\n\nKaçtın! Ama ışık hala kırmızı. Sonsuza dek.")
        sys.exit(0)
