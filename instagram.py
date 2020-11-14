from selenium import webdriver
from time import sleep
import getpass

def pulsar_boton_por_texto( texto, etiqueta="button" ):
    path = "//%s[contains(text(), '%s')]" % (etiqueta, texto)
    pulsar_xpath( path )

def pulsar_boton_por_aria_label( texto, etiqueta="div" ):
    path = "//%s[@aria-label='%s']" % (etiqueta, texto)
    pulsar_xpath( path )
    
def pulsar_xpath( xpath, sleep_time=0.5 ):
    path = xpath
    botones = driver.find_elements_by_xpath( path )
    # Si se encuentra el botón se pulsa
    if len(botones) > 0:
        boton = botones[0]
        boton.click()
    sleep( sleep_time )

options = webdriver.ChromeOptions()
options.add_argument("--start-fullscreen")

# Cargamos instagram
driver = webdriver.Chrome( options=options )
driver.get( "https://instagram.com" )
sleep(2)

pulsar_boton_por_texto( "Aceptar" )

# Introducimos nuestro nombre de usuario
print("Introduce tu nombre de usuario:")
username = input()
password = getpass.getpass( prompt="Introduce tu password:")

driver.find_element_by_name("username").send_keys( username )
sleep(0.5)
driver.find_element_by_name("password").send_keys( password )
sleep(0.5)
driver.find_element_by_name("password").send_keys( u'\ue007' )

# Esperamos 2 segundos que cargue la página
sleep( 4 )
pulsar_boton_por_texto("Ahora no")








