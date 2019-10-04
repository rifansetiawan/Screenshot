import time
import os
from selenium import webdriver
import pyautogui
import os

path = os.getcwd()
DRIVER = 'chromedriver'

chrome_options = webdriver.ChromeOptions()
if os.name == "nt":
    # If current OS is Windows
    chrome_options.add_argument("--start-maximized")
else:
    # Other OS (Mac / Linux)
    chrome_options.add_argument("--kiosk")

driver = webdriver.Chrome(DRIVER, chrome_options = chrome_options)
driver.get('https://p2p.danamas.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danamas.png')
time.sleep(2)

driver.get('https://www.investree.id/')
time.sleep(10)
screenshot = driver.save_screenshot('investree.png')
time.sleep(2)


driver.get('https://amartha.com/')
time.sleep(10)
screenshot = driver.save_screenshot('amartha.png')
time.sleep(2)


driver.get('https://www.dompetkilat.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('dompetkilat.png')
time.sleep(2)


driver.get('https://www.tokomodal.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('tokomodal.png')
time.sleep(2)

driver.get('https://uangteman.com/')
time.sleep(10)
screenshot = driver.save_screenshot('uangteman.png')
time.sleep(2)

driver.get('https://koinworks.com/')
time.sleep(10)
screenshot = driver.save_screenshot('koinworks.png')
time.sleep(2)

driver.get('https://modalku.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('modalku.png')
time.sleep(2)

driver.get('http://www.pendanaan.com/')
time.sleep(10)
screenshot = driver.save_screenshot('pendanaan.png')
time.sleep(2)

driver.get('https://www.awantunai.com/')
time.sleep(10)
screenshot = driver.save_screenshot('awantunai.png')
time.sleep(2)

driver.get('https://klikacc.com/')
time.sleep(10)
screenshot = driver.save_screenshot('klikacc.png')
time.sleep(2)

driver.get('https://crowdo.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('crowdo.png')
time.sleep(2)

driver.get('https://www.akseleran.com/')
time.sleep(10)
screenshot = driver.save_screenshot('akseleran.png')
time.sleep(2)

driver.get('https://www.taralite.com/')
time.sleep(10)
screenshot = driver.save_screenshot('teralite.png')
time.sleep(2)

driver.get('http://fintag.id/')
time.sleep(10)
screenshot = driver.save_screenshot('fintag.png')
time.sleep(2)

driver.get('http://invoila.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('invoila.png')
time.sleep(2)

driver.get('https://www.tunaikita.com/')
time.sleep(10)
screenshot = driver.save_screenshot('tunaikita.png')
time.sleep(2)

driver.get('https://igrow.asia/')
time.sleep(10)
screenshot = driver.save_screenshot('igrow.png')
time.sleep(2)

driver.get('https://www.cicil.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('cicil.png')
time.sleep(2)

driver.get('http://danamerdeka.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danamerdeka.png')
time.sleep(2)

driver.get('https://cashwagon.id/')
time.sleep(10)
screenshot = driver.save_screenshot('cashwagon.png')
time.sleep(2)

driver.get('https://www.estakapital.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('estacapital.png')
time.sleep(2)

driver.get('https://ammana.id/')
time.sleep(10)
screenshot = driver.save_screenshot('ammana.png')
time.sleep(2)

driver.get('https://gradana.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('gradana.png')
time.sleep(2)

driver.get('http://www.danamapan.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danamapan.png')
time.sleep(2)

driver.get('http://www.aktivaku.id/')
time.sleep(10)
screenshot = driver.save_screenshot('aktivaku.png')
time.sleep(2)

driver.get('https://danakini.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danakini.png')
time.sleep(2)

driver.get('https://www.finmas.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('finmas.png')
time.sleep(2)

driver.get('http://indodana.id/')
time.sleep(10)
screenshot = driver.save_screenshot('indodana.png')
time.sleep(2)

driver.get('https://www.kredivo.id/')
time.sleep(10)
screenshot = driver.save_screenshot('kredivo.png')
time.sleep(2)

driver.get('https://mekar.id/')
time.sleep(10)
screenshot = driver.save_screenshot('mekar.png')
time.sleep(2)

driver.get('https://www.pinjamango.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('pinjamango.png')
time.sleep(2)

driver.get('https://iternak.id/')
time.sleep(10)
screenshot = driver.save_screenshot('iternak.png')
time.sleep(2)

driver.get('http://kreditpintar.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('kreditpintar.png')
time.sleep(2)

driver.get('https://kredito.id/')
time.sleep(10)
screenshot = driver.save_screenshot('kredito.png')
time.sleep(2)

driver.get('https://crowde.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('crowde.png')
time.sleep(2)

driver.get('http://www.kreditplusteknologi.id/')
time.sleep(10)
screenshot = driver.save_screenshot('kreditplusteknologi.png')
time.sleep(2)

driver.get('https://tanifund.id/')
time.sleep(10)
screenshot = driver.save_screenshot('tanifund.png')
time.sleep(2)

driver.get('https://www.danain.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danain.png')
time.sleep(2)

driver.get('https://indofund.id/')
time.sleep(10)
screenshot = driver.save_screenshot('indofund.png')
time.sleep(2)

driver.get('http://kreditpro.id/')
time.sleep(10)
screenshot = driver.save_screenshot('kreditpro.png')
time.sleep(2)

driver.get('http://www.avantee.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('avantee.png')
time.sleep(2)

driver.get('http://www.do-it.id/')
time.sleep(10)
screenshot = driver.save_screenshot('do-it.png')
time.sleep(2)

driver.get('http://rupiahcepat.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('rupiahcepat.png')
time.sleep(2)

driver.get('http://www.danarupiah.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danarupiah.png')
time.sleep(2)

driver.get('http://danabijak.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danabijak.png')
time.sleep(2)

driver.get('http://cashcepat.id/')
time.sleep(10)
screenshot = driver.save_screenshot('cashcepat.png')
time.sleep(2)

driver.get('http://danalaut.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danalaut.png')
time.sleep(2)

driver.get('http://danasyariah.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danasyariah.png')
time.sleep(2)

driver.get('http://telefin.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('telefin.png')
time.sleep(2)

driver.get('http://modalrakyat.id/')
time.sleep(10)
screenshot = driver.save_screenshot('modalrakyat.png')
time.sleep(2)

driver.get('http://kawancicil.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('kawancicil.png')
time.sleep(2)

driver.get('http://sanders.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('sanders.png')
time.sleep(2)

driver.get('http://kreditcepat.id/')
time.sleep(10)
screenshot = driver.save_screenshot('kreditcepat.png')
time.sleep(2)

driver.get('http://uangme.id/')
time.sleep(10)
screenshot = driver.save_screenshot('uangme.png')
time.sleep(2)

driver.get('http://pinjamduit.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('pinjamduit.png')
time.sleep(2)

driver.get('http://pinjamyuk.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('pinjamyuk.png')
time.sleep(2)

driver.get('http://pinjammodal.id/')
time.sleep(10)
screenshot = driver.save_screenshot('pinjammodal.png')
time.sleep(2)

driver.get('http://julo.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('julo.png')
time.sleep(2)

driver.get('http://indo.geteasycash.asia/')
time.sleep(10)
screenshot = driver.save_screenshot('geteasycash.png')
time.sleep(2)

driver.get('http://maucash.id/')
time.sleep(10)
screenshot = driver.save_screenshot('maucash.png')
time.sleep(2)

driver.get('http://rupiahone.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('rupiahone.png')
time.sleep(2)

driver.get('http://pohondana.id/')
time.sleep(10)
screenshot = driver.save_screenshot('pohondana.png')
time.sleep(2)

driver.get('http://danacita.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danacita.png')
time.sleep(2)

driver.get('http://danadidik.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danadidik.png')
time.sleep(2)

driver.get('http://trustiq.id/')
time.sleep(10)
screenshot = driver.save_screenshot('trustiq.png')
time.sleep(2)

driver.get('http://danai.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danai.png')
time.sleep(2)

driver.get('http://pinduit.id/')
time.sleep(10)
screenshot = driver.save_screenshot('pinduit.png')
time.sleep(2)

driver.get('http://smartcapital.id/')
time.sleep(10)
screenshot = driver.save_screenshot('smartcapital.png')
time.sleep(2)

driver.get('http://danamart.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danamart.png')
time.sleep(2)

driver.get('http://samakita.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('samakita.png')
time.sleep(2)

driver.get('http://sayamodalin.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('sayamodalin.png')
time.sleep(2)

driver.get('http://plazapinjaman.id/')
time.sleep(10)
screenshot = driver.save_screenshot('plazapinjaman.png')
time.sleep(2)

driver.get('http://web.vestia.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('vestia.png')
time.sleep(2)

driver.get('http://singa.id/')
time.sleep(10)
screenshot = driver.save_screenshot('singa.png')
time.sleep(2)

driver.get('http://adakami.id/')
time.sleep(10)
screenshot = driver.save_screenshot('adakami.png')
time.sleep(2)

driver.get('http://modalusaha.id/')
time.sleep(10)
screenshot = driver.save_screenshot('modalusaha.png')
time.sleep(2)

driver.get('http://asetku.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('asetku.png')
time.sleep(2)

driver.get('http://danafix.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danafix.png')
time.sleep(2)

driver.get('http://lumbungdana.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('lumbungdana.png')
time.sleep(2)

driver.get('http://lahansikam.co.id')
time.sleep(10)
screenshot = driver.save_screenshot('lahansikam.png')
time.sleep(2)

driver.get('http://www.modalnasional.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('modalnasional.png')
time.sleep(2)

driver.get('http://www.danabagus.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danabagus.png')
time.sleep(2)

driver.get('http://www.lenteradana.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('lenteradana.png')
time.sleep(2)

driver.get('http://www.ikredo.id/')
time.sleep(10)
screenshot = driver.save_screenshot('ikredo.png')
time.sleep(2)

driver.get('http://www.adakita.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('adakita.png')
time.sleep(2)

driver.get('http://www.ukuindo.com/')
time.sleep(10)
screenshot = driver.save_screenshot('ukuindo.png')
time.sleep(2)

driver.get('http://www.pinjamwinwin.com/')
time.sleep(10)
screenshot = driver.save_screenshot('pinjamwinwin.png')
time.sleep(2)

driver.get('http://www.pasarpinjam.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('pasarpinjam.png')
time.sleep(2)

driver.get('http://www.kredinesia.id/')
time.sleep(10)
screenshot = driver.save_screenshot('kredinesia.png')
time.sleep(2)

driver.get('http://www.bkdana.id/')
time.sleep(10)
screenshot = driver.save_screenshot('bkdana.png')
time.sleep(2)

driver.get('http://www.gandengtangan.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('gandengtangan.png')
time.sleep(2)

driver.get('http://www.modalantara.id/')
time.sleep(10)
screenshot = driver.save_screenshot('modalantara.png')
time.sleep(2)

driver.get('http://www.komunal.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('komunal.png')
time.sleep(2)

driver.get('http://www.prosperitree.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('prosperitree.png')
time.sleep(2)

driver.get('http://www.danakoo.id/')
time.sleep(10)
screenshot = driver.save_screenshot('danakoo.png')
time.sleep(2)

driver.get('http://www.cairin.id/')
time.sleep(10)
screenshot = driver.save_screenshot('cairin.png')
time.sleep(2)

driver.get('http://www.batumbu.id/')
time.sleep(10)
screenshot = driver.save_screenshot('batumbu.png')
time.sleep(2)

driver.get('http://www.empatkali.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('empatkali.png')
time.sleep(2)

driver.get('http://www.jembatanemas.id/')
time.sleep(10)
screenshot = driver.save_screenshot('jembatanemas.png')
time.sleep(2)

driver.get('http://www.klikumkm.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('klikumkm.png')
time.sleep(2)

driver.get('http://www.kredible.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('kredible.png')
time.sleep(2)

driver.get('http://www.klikkami.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('klikkami.png')
time.sleep(2)

driver.get('http://www.kaching.id/')
time.sleep(10)
screenshot = driver.save_screenshot('kaching.png')
time.sleep(2)

driver.get('http://www.finplus.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('finplus.png')
time.sleep(2)

driver.get('http://www.p2p.alamisharia.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('alamisharia.png')
time.sleep(2)

driver.get('http://www.syarfi.id/')
time.sleep(10)
screenshot = driver.save_screenshot('syarfi.png')
time.sleep(2)

driver.get('http://www.digilend.id/')
time.sleep(10)
screenshot = driver.save_screenshot('digilend.png')
time.sleep(2)

driver.get('http://www.asakita.id/')
time.sleep(10)
screenshot = driver.save_screenshot('asakita.png')
time.sleep(2)

driver.get('http://www.duhasyariah.com/')
time.sleep(10)
screenshot = driver.save_screenshot('duhasyariah.png')
time.sleep(2)

driver.get('http://bocil.id')
time.sleep(10)
screenshot = driver.save_screenshot('bocil.png')
time.sleep(2)

driver.get('http://www.qazwa.id/')
time.sleep(10)
screenshot = driver.save_screenshot('qazwa.png')
time.sleep(2)

driver.get('http://www.bsalam.id/')
time.sleep(10)
screenshot = driver.save_screenshot('bsalam.png')
time.sleep(2)

driver.get('http://www.onehope.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('onehope.png')
time.sleep(2)

driver.get('http://www.ladangmodal.com/')
time.sleep(10)
screenshot = driver.save_screenshot('ladangmodal.png')
time.sleep(2)

driver.get('http://www.dhanapala.id/')
time.sleep(10)
screenshot = driver.save_screenshot('dhanapala.png')
time.sleep(2)

driver.get('http://www.restock.id/')
time.sleep(10)
screenshot = driver.save_screenshot('restock.png')
time.sleep(2)

driver.get('http://www.solusi-ku.id/')
time.sleep(10)
screenshot = driver.save_screenshot('solusi-ku.png')
time.sleep(2)

driver.get('http://www.pinjamdisini.com/')
time.sleep(10)
screenshot = driver.save_screenshot('pinjamdisini.png')
time.sleep(2)

driver.get('http://www.adapundi.com/')
time.sleep(10)
screenshot = driver.save_screenshot('adapundi.png')
time.sleep(2)

driver.get('http://www.treeplus.id/')
time.sleep(10)
screenshot = driver.save_screenshot('treeplus.png')
time.sleep(2)

driver.get('http://www.assetkita.com/')
time.sleep(10)
screenshot = driver.save_screenshot('assetkita.png')
time.sleep(2)

driver.get('http://www.edufund.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('edufund.png')
time.sleep(2)

driver.get('http://finanku.com/')
time.sleep(10)
screenshot = driver.save_screenshot('finanku.png')
time.sleep(2)

driver.get('http://www.tunasaku.co.id/')
time.sleep(10)
screenshot = driver.save_screenshot('tunasaku.png')
time.sleep(2)

driver.get('http://www.uatas.id/')
time.sleep(10)
screenshot = driver.save_screenshot('uatas.png')
time.sleep(2)

