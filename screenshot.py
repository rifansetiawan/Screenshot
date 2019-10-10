import time
import os
import shutil
from selenium import webdriver
import pyautogui
import os
from datetime import datetime
datestring = datetime.strftime(datetime.now(), '(%Y-%m-%d)-(%H.%M.ss)')
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


cwd = os.getcwd()
DRIVER = 'chromedriver'

chrome_options = webdriver.ChromeOptions()
if os.name == "nt":
    # If current OS is Windows
    chrome_options.add_argument("--start-maximized")
else:
    # Other OS (Mac / Linux)
    chrome_options.add_argument("--kiosk")

#------------------- create folder of the date-------------------

targetPath = os.path.join(cwd, 'FolderPNG');
while not os.path.exists(targetPath):
    os.mkdir(targetPath)


#-----------------------------------------------------------------


#------------------------------------------------------------------
driver = webdriver.Chrome(DRIVER, chrome_options = chrome_options)
# driver.get('https://p2p.danamas.co.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/danamas.png')
# time.sleep(2)

# driver.get('https://www.investree.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/investree.png')
# time.sleep(2)


# driver.get('https://amartha.com/')
# driver.execute_script("window.scrollTo(0, 500)") 
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/amartha.png')
# time.sleep(2)


# driver.get('https://www.dompetkilat.co.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/dompetkilat.png')
# time.sleep(2)

# driver.get('http://kimo.co.id/')
# driver.execute_script("window.scrollTo(0, 450)") 
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/kimo.png')
# time.sleep(2)

# driver.get('https://www.tokomodal.co.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/tokomodal.png')
# time.sleep(2)

# driver.get('https://uangteman.com/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/uangteman.png')
# time.sleep(2)

# driver.get('https://koinworks.com/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/koinworks.png')
# time.sleep(2)

# driver.get('https://modalku.co.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/modalku.png')
# time.sleep(2)

# driver.get('http://www.pendanaan.com/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/pendanaan.png')
# time.sleep(2)

# driver.get('https://www.awantunai.com/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/awantunai.png')
# time.sleep(2)

# driver.get('https://klikacc.com/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/klikacc.png')
# time.sleep(2)

# driver.get('https://crowdo.co.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/crowdo.png')
# time.sleep(2)

# driver.get('https://www.akseleran.com/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/akseleran.png')
# time.sleep(2)

# driver.get('https://www.taralite.com/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/teralite.png')
# time.sleep(2)

# driver.get('http://fintag.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/fintag.png')
# time.sleep(2)

# driver.get('http://invoila.co.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/invoila.png')
# time.sleep(2)

# driver.get('https://www.tunaikita.com/')
# driver.execute_script("window.scrollTo(0, 800)") 
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/tunaikita.png')
# time.sleep(2)

# driver.get('https://igrow.asia/')
# driver.execute_script("window.scrollTo(0, 2800)") 
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/igrow.png')
# time.sleep(2)

# driver.get('https://www.cicil.co.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/cicil.png')
# time.sleep(2)

# driver.get('http://danamerdeka.co.id/')
# driver.execute_script("window.scrollTo(0, 500)") 
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/danamerdeka.png')
# time.sleep(2)

# driver.get('https://cashwagon.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/cashwagon.png')
# time.sleep(2)

# driver.get('https://www.estakapital.co.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/estacapital.png')
# time.sleep(2)

# driver.get('https://ammana.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/ammana.png')
# time.sleep(2)

# driver.get('https://gradana.co.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/gradana.png')
# time.sleep(2)

# driver.get('http://www.danamapan.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/danamapan.png')
# time.sleep(2)

# driver.get('http://www.aktivaku.com/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/aktivaku.png')
# time.sleep(2)

# driver.get('https://danakini.co.id/')
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.pum-close.popmake-close"))).click()
# driver.execute_script("window.scrollTo(0, 2200)") 
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/danakini.png')
# time.sleep(2)

# driver.get('https://www.finmas.co.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/finmas.png')
# time.sleep(2)

# driver.get('http://indodana.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/indodana.png')
# time.sleep(2)

# driver.get('https://www.kredivo.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/kredivo.png')
# time.sleep(2)

# driver.get('https://mekar.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/mekar.png')
# time.sleep(2)

# driver.get('https://www.pinjamango.co.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/pinjamango.png')
# time.sleep(2)

# driver.get('https://iternak.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/iternak.png')
# time.sleep(2)

# driver.get('http://kreditpintar.co.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/kreditpintar.png')
# time.sleep(2)

# driver.get('https://kredito.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/kredito.png')
# time.sleep(2)

# driver.get('https://crowdo.co.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/crowdo.png')
# time.sleep(2)

# driver.get('http://www.kreditplusteknologi.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/kreditplusteknologi.png')
# time.sleep(2)

# driver.get('https://tanifund.com/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/tanifund.png')
# time.sleep(2)

# driver.get('https://m.danain.co.id/beranda')
# element = driver.find_element_by_css_selector('div.no-padding-bottom')
# driver.execute_script("arguments[0].scrollIntoView()", element)
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/danain.png')
# time.sleep(2)

# driver.get('https://indofund.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/indofund.png')
# time.sleep(2)

# driver.get('http://kreditpro.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/kreditpro.png')
# time.sleep(2)

# driver.get('http://www.avantee.co.id/')
# driver.execute_script("window.scrollTo(0, 700)") 
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/avantee.png')
# time.sleep(2)

# driver.get('http://www.do-it.id/')
# time.sleep(10)
# screenshot = driver.save_screenshot('FolderPNG/do-it.png')
# time.sleep(2)

driver.get('http://www.rupiahcepat.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/rupiahcepat.png')
time.sleep(2)

driver.get('http://www.danarupiah.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/danarupiah.png')
time.sleep(2)

driver.get('http://danabijak.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/danabijak.png')
time.sleep(2)

driver.get('http://cashcepat.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/cashcepat.png')
time.sleep(2)

driver.get('http://danalaut.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/danalaut.png')
time.sleep(2)

driver.get('http://danasyariah.id/')
driver.execute_script("window.scrollTo(0, 750)") 
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/danasyariah.png')
time.sleep(2)

driver.get('http://telefin.co.id/')
driver.execute_script("window.scrollTo(0, 200)") 
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/telefin.png')
time.sleep(2)

driver.get('http://modalrakyat.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/modalrakyat.png')
time.sleep(2)

driver.get('http://kawancicil.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/kawancicil.png')
time.sleep(2)

driver.get('http://sanders.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/sanders.png')
time.sleep(2)

driver.get('http://kreditcepat.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/kreditcepat.png')
time.sleep(2)

driver.get('http://uangme.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/uangme.png')
time.sleep(2)

driver.get('http://pinjamduit.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/pinjamduit.png')
time.sleep(2)

driver.get('http://www.pinjamyuk.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/pinjamyuk.png')
time.sleep(2)

driver.get('http://pinjammodal.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/pinjammodal.png')
time.sleep(2)

driver.get('http://julo.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/julo.png')
time.sleep(2)

driver.get('http://indo.geteasycash.asia/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/geteasycash.png')
time.sleep(2)

driver.get('http://maucash.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/maucash.png')
time.sleep(2)

driver.get('http://rupiahone.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/rupiahone.png')
time.sleep(2)

driver.get('http://pohondana.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/pohondana.png')
time.sleep(2)

driver.get('http://danacita.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/danacita.png')
time.sleep(2)

driver.get('http://danadidik.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/danadidik.png')
time.sleep(2)

driver.get('http://trustiq.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/trustiq.png')
time.sleep(2)

driver.get('http://danai.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/danai.png')
time.sleep(2)

driver.get('http://pinduit.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/pinduit.png')
time.sleep(2)

driver.get('http://smartcapital.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/smartcapital.png')
time.sleep(2)

driver.get('http://danamart.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/danamart.png')
time.sleep(2)

driver.get('http://samakita.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/samakita.png')
time.sleep(2)

driver.get('http://sayamodalin.co.id/')
driver.execute_script("window.scrollTo(0, 300)") 
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/sayamodalin.png')
time.sleep(2)

driver.get('http://plazapinjaman.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/plazapinjaman.png')
time.sleep(2)

driver.get('http://web.vestia.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/vestia.png')
time.sleep(2)

driver.get('http://singa.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/singa.png')
time.sleep(2)

driver.get('https://www.adakami.id')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/adakami.png')
time.sleep(2)

driver.get('http://modalusaha.id/')
driver.execute_script("window.scrollTo(0, 300)") 
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/modalusaha.png')
time.sleep(2)

driver.get('http://asetku.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/asetku.png')
time.sleep(2)

driver.get('http://danafix.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/danafix.png')
time.sleep(2)

driver.get('http://lumbungdana.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/lumbungdana.png')
time.sleep(2)

driver.get('http://lahansikam.co.id')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/lahansikam.png')
time.sleep(2)

driver.get('http://www.modalnasional.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/modalnasional.png')
time.sleep(2)

driver.get('http://www.danabagus.id/')
driver.execute_script("window.scrollTo(0, 700)") 
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/danabagus.png')
time.sleep(2)

driver.get('https://www.lenteradana.co.id/lender/lender-home')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/lenteradana.png')
time.sleep(2)

driver.get('http://www.ikredo.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/ikredo.png')
time.sleep(2)

driver.get('http://www.adakita.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/adakita.png')
time.sleep(2)

driver.get('http://www.ukuindo.com/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/ukuindo.png')
time.sleep(2)

driver.get('http://www.pinjamwinwin.com/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/pinjamwinwin.png')
time.sleep(2)

driver.get('http://www.pasarpinjam.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/pasarpinjam.png')
time.sleep(2)

driver.get('http://www.kredinesia.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/kredinesia.png')
time.sleep(2)

driver.get('http://www.bkdana.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/bkdana.png')
time.sleep(2)

driver.get('http://www.gandengtangan.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/gandengtangan.png')
time.sleep(2)

driver.get('http://www.modalantara.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/modalantara.png')
time.sleep(2)

driver.get('http://www.komunal.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/komunal.png')
time.sleep(2)

driver.get('http://www.prosperitree.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/prosperitree.png')
time.sleep(2)

driver.get('http://www.danakoo.id/')
driver.execute_script("window.scrollTo(0, 1000)") 
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/danakoo.png')
time.sleep(2)

driver.get('http://www.cairin.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/cairin.png')
time.sleep(2)

driver.get('http://www.batumbu.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/batumbu.png')
time.sleep(2)

driver.get('http://www.empatkali.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/empatkali.png')
time.sleep(2)

driver.get('http://www.jembatanemas.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/jembatanemas.png')
time.sleep(2)

driver.get('http://www.klikumkm.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/klikumkm.png')
time.sleep(2)

driver.get('http://www.kredible.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/kredible.png')
time.sleep(2)

driver.get('http://www.klikkami.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/klikkami.png')
time.sleep(2)

driver.get('http://www.kaching.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/kaching.png')
time.sleep(2)

driver.get('http://www.finplus.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/finplus.png')
time.sleep(2)

driver.get('http://www.p2p.alamisharia.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/alamisharia.png')
time.sleep(2)

driver.get('http://www.syarfi.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/syarfi.png')
time.sleep(2)

driver.get('http://www.digilend.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/digilend.png')
time.sleep(2)

driver.get('http://www.asakita.id/')
time.sleep(10)
driver.execute_script("document.body.style.zoom='50%'")
screenshot = driver.save_screenshot('FolderPNG/asakita.png')
time.sleep(2)

driver.get('http://www.duhasyariah.com/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/duhasyariah.png')
time.sleep(2)

driver.get('http://bocil.id')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/bocil.png')
time.sleep(2)

driver.get('http://www.qazwa.id/bermasalah')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/qazwa.png')
time.sleep(2)

driver.get('http://www.bsalam.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/bsalam.png')
time.sleep(2)

driver.get('http://www.onehope.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/onehope.png')
time.sleep(2)

driver.get('http://www.ladangmodal.com/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/ladangmodal.png')
time.sleep(2)

driver.get('http://www.dhanapala.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/dhanapala.png')
time.sleep(2)

driver.get('http://www.restock.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/restock.png')
time.sleep(2)

driver.get('http://www.solusi-ku.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/solusi-ku.png')
time.sleep(2)

driver.get('http://www.pinjamdisini.com/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/pinjamdisini.png')
time.sleep(2)

driver.get('http://www.adapundi.com/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/adapundi.png')
time.sleep(2)

driver.get('http://www.treeplus.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/treeplus.png')
time.sleep(2)

driver.get('http://www.assetkita.com/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/assetkita.png')
time.sleep(2)

driver.get('http://www.edufund.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/edufund.png')
time.sleep(2)

driver.get('http://finanku.com/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/finanku.png')
time.sleep(2)

driver.get('http://www.tunasaku.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/tunasaku.png')
time.sleep(2)

driver.get('http://www.uatas.id/')
time.sleep(10)
screenshot = driver.save_screenshot('FolderPNG/uatas.png')
time.sleep(2)

targetPath_PNG = os.path.join("FolderPNG", datestring)
while not os.path.exists(targetPath_PNG):
	os.mkdir(targetPath_PNG)


cwd = os.getcwd()
source = cwd+'/FolderPNG/'
dest1 = targetPath_PNG


files = os.listdir(source)

for f in files:
        shutil.move(source+f, targetPath_PNG)