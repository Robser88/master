from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

# Ruta al chromedriver
#chromedriver_path = '/path/to/chromedriver'

# Configurar el navegador Chrome
driver = webdriver.Chrome()

# Abrir la página web
driver.get('https://sga-cloud.casewaresa.com/unireformada/sgacampus/#home')  # Reemplaza con la URL del formulario
time.sleep(2)
# Llenar un campo de texto
input_element = driver.find_element(By.NAME, 'userName')  # Reemplaza con el nombre del campo
input_element.send_keys('1129539213')  # Reemplaza con el texto que quieres ingresar
input_element = driver.find_element(By.NAME, 'password')  # Reemplaza con el nombre del campo
input_element.send_keys('Robser67')  # Reemplaza con el texto que quieres ingresar

# Seleccionar un valor de una lista desplegable
#select_element = Select(driver.find_element_by_name('Password'))  # Reemplaza con el nombre del campo
#select_element.select_by_visible_text('Valor a seleccionar')  # Reemplaza con el valor que quieres seleccionar
#time.sleep(2)
# Si el formulario tiene un botón de enviar
#submit_button = driver.find_element(By.XPATH, 'table//tr//td//table//tr//td//button[text()="Entrar"]')  # Reemplaza con el nombre del botón
#submit_button = driver.find_element(By.TAG_NAME, 'Entrar')
#submit_button = driver.find_element((By.ID, 'isc_3D'))  # Reemplaza con el XPath o selector adecuado

button = driver.find_element(By.CLASS_NAME, 'button')  # Reemplaza 'button_class' con la clase del botón
button.click()


#submit_button.click()
#submit_button.select()



# Esperar unos segundos para que se procese la acción (opcional)
time.sleep(10)

# Cerrar el navegador
# driver.quit()