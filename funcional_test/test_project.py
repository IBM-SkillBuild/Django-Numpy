
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time




class TestProject(StaticLiveServerTestCase):
  
  def setUp(self):
    self.browser= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  def tearDown(self):
    self.browser.close()  
  
  # test que comprueba el titulo de la página  
  def test_Title(self):
    self.browser.get(self.live_server_url)  
    assert "Bejob-IBM SkillBuild" in self.browser.title
    time.sleep(3)
  # test que comprueba el texto o innerhtml del h1  
  def test_h1(self):
    self.browser.get(self.live_server_url)  
    elemento=self.browser.find_element(By.TAG_NAME, "h1")
    assert "Generador de Matrices Numpy" in elemento.text
    time.sleep(3)
  def test_input(self):
    self.browser.get(self.live_server_url)  
    select=self.browser.find_element(By.NAME, "N")
    boton=self.browser.find_element(By.ID, "btn-submit")
    elemento=self.browser.find_element(By.TAG_NAME, "h1")
    number=7
    select.send_keys(number)
    boton.send_keys(Keys.RETURN)
    time.sleep(1)
    self.browser.get(self.browser.current_url)
    elemento=self.browser.find_element(By.TAG_NAME, "h1")
    texto="Matriz generada de %s x %s"%(number,number)
    assert texto in elemento.text
    time.sleep(3)
