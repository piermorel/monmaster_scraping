#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd


from parametres import code_formation
from parametres import username
from parametres import password


cand = pd.read_csv("no_candidats.csv")
print(cand)




driver = webdriver.Safari()
driver.get("https://interne.candidature.monmaster.gouv.fr/formationscandidatables/"+code_formation+"/candidatures")
driver.implicitly_wait(10)
time.sleep(4)

# In[ ]:


elem = driver.find_element(By.ID,"username")
elem.clear()
elem.send_keys(username)
elem = driver.find_element(By.ID,"password")
elem.clear()
elem.send_keys(password)
elem.send_keys(Keys.RETURN)


# In[ ]:

time.sleep(4)
for index, row in cand.iterrows():
    
    print("Telechargement candidat ",index," code ",row.no)
    WebDriverWait(driver, timeout=20).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR,"[id^=page-candidatures-noCandidat-]")))
    time.sleep(1)
    elem = driver.find_element(By.CSS_SELECTOR,"[id^=page-candidatures-noCandidat-]")
    elem.clear()
    elem.send_keys(row.no)
    elem.send_keys(Keys.RETURN)
    
    WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable(
        (By.XPATH,"//a[contains(text(), 'Télécharger la candidature')]")))
    time.sleep(1)
    elem = driver.find_element(By.XPATH,"//a[contains(text(), 'Télécharger la candidature')]")
    elem.click()
    #driver.execute_script('arguments[0].click()', elem)
    
    time.sleep(8)
    
    driver.back()



driver.back()





