# Gerekli kütüphaneleri import ettik. cv2 kütüphanesi opencv için, np kütüphanesi ise çok boyutlu dizi ve matris işlemleri için kullanılır.
import cv2
import numpy as np

# cv2 kütüphanesi içerisindeki imread ile kullanacağımız görüntüyü yükledik
image = cv2.imread("D:\Balon.png")


# cvtColor fonkisyonunu kullanarak görüntümüzü grileştirdik
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Çekirdeğimizi oluşturduk. Burada kernel matrisini önce numpy dizisi olarak tanımlarız.
# Daha sonra, kernel matrisindeki tüm elemanların toplamına bölerek normalizasyon yaparız.
# Normalizasyon, matrisin toplamının 1'e eşit olmasını sağlar.
kernel = np.array([[0, 0, -1, 0, 0],
                   [0, -1, -2, -1, 0],
                   [-1, -2, 16, -2, -1],
                   [0, -1, -2, -1, 0],
                   [0, 0, -1, 0, 0]], dtype=np.float32)

#Çekirdeğe normalizasyon işlemi uyguladık. Convolutionda toplamın 1 olması gerekiyordu.
kernel_sum = np.sum(kernel)
if kernel_sum != 0:
    kernel /= kernel_sum

# Filtreyi grileştiriğimiz resme uyguladık.
result = cv2.filter2D(gray_image,-1,kernel)

# Çıktı görüntüleri orijinal, grileştirilmiş ve filtrelenmiş olarak verdik.
cv2.imshow("Original", image)
cv2.imshow("Gray Image", gray_image)
cv2.imshow("Filtered Image", result)
cv2.waitKey(0)

# Herhangi bir tuşa basınca tüm pencerelerin kapanmasını sağladık.
cv2.destroyAllWindows()
