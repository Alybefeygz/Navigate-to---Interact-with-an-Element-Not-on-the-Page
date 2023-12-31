# Selenium için gerekli modülleri içe aktarın
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Chrome web sürücüsünü ChromeDriverManager kullanarak başlatın
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Belirtilen URL'yi Chrome tarayıcısında açın
driver.get("https://nicepage.com/tr/k/liste-web-sitesi-sablonlari")

# Hedef elementin class adını tanımlayın
hedefElementClassName = "media-image"

# Tarayıcı işlemlerini gerçekleştirmek için ActionChains'in bir örneğini oluşturun
actions = ActionChains(driver)

# 10 saniyelik bir zaman aşımı ile bir WebDriverWait örneği oluşturun
wait = WebDriverWait(driver, 10)

# Hedef elementi, class adına dayanarak WebDriverWait kullanarak bulun
hedefElement = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, hedefElementClassName)))[100]

# Hedef elementi görünür hale getirmek için sayfayı JavaScript kullanarak kaydırın
driver.execute_script("arguments[0].scrollIntoView(true);", hedefElement)
time.sleep(2)

# Sayfayı 150 piksel yukarı kaydırmak için JavaScript kullanın
driver.execute_script("window.scrollBy(0,-150)")
time.sleep(3)

# JavaScript kullanarak hedef elemente tıklayın
driver.execute_script("arguments[0].click();", hedefElement)

# Betik yürütmesini uzun bir süre (100,000 saniye) duraklatın
time.sleep(100000000)
