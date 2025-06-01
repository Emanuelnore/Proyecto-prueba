from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(5)

valor=driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr").text

print(valor)
row=len(driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr"))
col =len(driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr[1]/th"))
print(row)

print(col)
for n in range(2,row+1):
	for b in range(1,col+1):
		xpath=f'//*[@id="customers"]/tbody/tr[{n}]/td[{b}]'
		dato=driver.find_element(By.XPATH, xpath).text
		print(dato,end=' ')
	print()

	#Agregando un comentario 