import pystray #pystray kütüphanemizi import ettik
import PIL.Image #pillow kütüphanemizin Image fonksiyonunu import ettik

image = PIL.Image.open("icon.png") #Icon olarak kullanacağımız fotoğrafı tanımladık

def on_clicked(icon, item): # Kullanacağımız fonksiyonu tanımladık
	if str(item) == "Tıklandı yaz": #MenuItem'da tanımladığımız başlık	
		print("Tıklandı")
	elif str(item) == "Çıkış": #Çıkış seçeneğinin işlemini de burada tanımladık
		icon.stop() #Farklı bir fonksiyon da tanımlayarak yapabiliriz
	elif str(item) == "Alt menü":
		print("Alt menüdeyiz")
icon = pystray.Icon("Linux", image, menu = pystray.Menu( #Tray iconumuzu tanımladık
	pystray.MenuItem("Tıklandı yaz", on_clicked), #Sağ tıkladığımızda çıkan menüye item ekledik
	pystray.MenuItem("Çıkış", on_clicked),
	pystray.MenuItem("Menü içinde Menü", pystray.Menu(
		pystray.MenuItem("Alt menü",on_clicked)
		))
))

icon.run() #Iconumuzu çalıştırdık