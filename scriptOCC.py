from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.firefox.options import Options
import pandas as pd
import numpy as np
import time


def manejoDatos(datos:dict):
    archivo = input("Dame el nombre de tu archivo: ")+".csv"
    df_trabajos = pd.DataFrame(datos)
    print(df_trabajos.head())
    df_trabajos.to_csv(archivo, index=False)

def paginacion(driver) -> dict:

    trabajos = {
        'Puesto': [],
        'Sueldo': [],
        'Comodidades': [],
        'Empresa': []
    }

    paginacion = driver.find_element(By.XPATH, '//div/div[@class = "inline-block"]/ul')
    paginas = paginacion.find_elements(By.XPATH, './/li')
    ultima_pagina = int(paginas[-2].text)

    pagina_actual = 1

    while pagina_actual <= ultima_pagina:

        contenedor = driver.find_element(By.XPATH, '/html/body/main/div[4]/aside')
        ofertas = contenedor.find_elements(By.XPATH, './/div/div/div[contains(@class, "flex flex-col relative")]')

        for oferta in ofertas:
            # Extraemos Puesto
            try:
                trabajos['Puesto'].append(oferta.find_element(By.XPATH, './/h2').text)
            except:
                trabajos['Puesto'].append(np.nan)
            # Extraemos sueldo
            try:
                trabajos['Sueldo'].append(oferta.find_element(By.XPATH, './/span').text)
            except:
                trabajos["Sueldo"].append(np.nan)
            # Extraemos las comodidades ofrecidas por la empresa
            try:
                comodidades = [comodidad.text for comodidad in oferta.find_elements(By.XPATH, './/ul/li')]
                trabajos['Comodidades'].append(comodidades)
            except:
                trabajos['Comodidades'].append(np.nan)
            # Extraemos el nombre de la emppresa
            try:
                trabajos['Empresa'].append(oferta.find_element(By.XPATH, './/div/div/span').text)
            except:
                trabajos['Empresa'].append(np.nan)
        try:
            pagina_siguiente = driver.find_element(By.XPATH, '/html/body/main/div[4]/aside/div/div[23]/div/ul/li[6]')
            pagina_siguiente.click()
            pagina_actual += 1
        except:
            pass

        driver.quit()
        return trabajos


def main():

    options = Options()
    options.headless = False

    estado = input('Escribe tu estado:  ').lower()
    ciudad = input('Escribe tu ciudad: ').lower()


    website = f'https://www.occ.com.mx/empleos/en-{estado}/en-la-ciudad-de-{ciudad}/'
    driver = webdriver.Firefox(options)

    driver.get(website)
    driver.maximize_window()
    time.sleep(5)

    puesto = input("Escribe tu puesto deseado: ")
    campoTrabajo = driver.find_element(By.XPATH, '/html/body/main/div[2]/nav/form/div[1]/div/div/input')
    campoTrabajo.send_keys(puesto)
    time.sleep(3)


    botonBusqueda = driver.find_element(By.XPATH, '/html/body/main/div[2]/nav/form/div[3]/button/span')
    botonBusqueda.click()
    time.sleep(1)

    datos = paginacion(driver)
    manejoDatos(datos)


if __name__ == '__main__':
    main()