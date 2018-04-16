import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

@pytest.fixture
def driver():
    url="https://www.univision.com/los-angeles/kmex/noticias/asesinatos/en-video-abandonan-el-cadaver-de-un-pandillero-junto-a-un-contenedor-de-basura"
    driver = webdriver.Firefox()
    driver.get(url)
    return driver

def is_Paused(driver):
    driver.execute_script("window.scrollTo(0, 300)")
    vidElement = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//video[@class='jw-video jw-reset']")))
    #//div[@class='jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-playback']
    vidElement.click()

    driver.implicitly_wait(5)
    timeBeforePause = driver.find_elements(By.XPATH, "//div[@class='jw-icon jw-icon-inline jw-text jw-reset jw-text-elapsed']")

    vidElement.click()
    timeAfterPause=driver.find_elements(By.XPATH, "//div[@class='jw-icon jw-icon-inline jw-text jw-reset jw-text-elapsed']")

    driver.implicitly_wait(5)

    durationTime= driver.find_elements(By.XPATH, "//div[@class='jw-icon jw-icon-inline jw-text jw-reset jw-text-duration']")

    print "Video Duration Time is:" + durationTime
    assert timeBeforePause == timeAfterPause

def playPause(driver):
    vidElement = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//video[@class='jw-video jw-reset']")))

    vidElement.click()

    driver.implicitly_wait(5)

    vidElement.click()
    assert 1 == 1