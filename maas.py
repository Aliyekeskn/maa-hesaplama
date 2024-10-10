mevcut_maaş = int(input("maaşınızı giriniz"))
çalışılan_yıl_sayısı = int(input("çalışılan yıl sayısı giriniz"))
performans_puanı = int(input("performans puanı giriniz"))
yüzde_miktarı = int(input("yüzde miktarı giriniz"))
zam_miktarı = mevcut_maaş * yüzde_miktarı
if mevcut_maaş <= 10000 and performans_puanı >= 90 and çalışılan_yıl_sayısı <= 5 :
  print(mevcut_maaş + zam_miktarı)
if mevcut_maaş <= 10000 and performans_puanı > 50 and performans_puanı < 69 and çalışılan_yıl_sayısı <= 5: 
  print(mevcut_maaş + zam_miktarı)
if mevcut_maaş <= 10000 and performans_puanı >= 90 and çalışılan_yıl_sayısı > 5 :
  print(mevcut_maaş + zam_miktarı)
if mevcut_maaş <= 10000 and 70 < performans_puanı < 89 and çalışılan_yıl_sayısı > 5 : 
  print(mevcut_maaş + zam_miktarı)
if mevcut_maaş <= 10000 and 50 < performans_puanı < 69 and çalışılan_yıl_sayısı > 5 : 
  print(mevcut_maaş + zam_miktarı)
if mevcut_maaş <= 10000 and performans_puanı < 50 and çalışılan_yıl_sayısı < 5 or çalışılan_yıl_sayısı > 5 :
  print(mevcut_maaş + zam_miktarı)
elif mevcut_maaş > 10000 :
  print(mevcut_maaş + zam_miktarı + mevcut_maaş * 0.3)
