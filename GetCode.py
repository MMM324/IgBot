from tkinter import N
from webbrowser import BaseBrowser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random
import clipboard
from soupsieve import select
#Creamos una funcion para crear un mail temporario
def createMail():
    list1 = []
    options = Options()
    options.add_argument('https://correotemporal.org/')
    browser = webdriver.Firefox(options=options, executable_path=r'C:\Users\diego\OneDrive\Escritorio\IGBot\geckodriver.exe')
    browser.implicitly_wait(5)
    sleep_random = random.randint(5, 10)
    time.sleep(sleep_random)
    copy_button = browser.find_element_by_xpath('//*[@id="botoncopiar"]')
    copy_button.click()
    get_mail = clipboard.paste()
    #getCode(options)
    list1.append(get_mail)
    list1.append(options)
    return list1
#Buscamos el codigo y lo tomamos
def getCode(y):
    options = y
    browser = webdriver.Firefox(options=options, executable_path=r'C:\Users\diego\OneDrive\Escritorio\IGBot\geckodriver.exe')
    browser.implicitly_wait(5)
    button_Retrieve = browser.find_element_by_xpath("/html/body/header/div/div/div[2]/button")
    button_Retrieve.click()
    button_Select = browser.find_element_by_xpath('//*[@id="email-alias-input"]')
    button_Select.click()
    try:        
        openMail_code = browser.find_element_by_xpath("/html/body/main/aside[2]/div[2]/div[1]/div[1]/div[2]/div/button[1]")
        openMail_code.click()
        getCode_ig = browser.find_element_by_xpath('//*[@id="mensaje-modal-1658172057990-label"]')
        print(getCode_ig)
    except Exception:
        print("Error: No se ecnontro el Codigo")
        pass
    pass
#Creamos una funcion que elabora el nombre para el registro de la cuenta
def nameUser():
    listNames = ["Miguel","Tahiel","Juan","Carlos", "Pablo", "Nicolas", "Ignacio", "Luis", "Agustin", "Francisco", "Lautaro", "Jose"]
    nameSelect =  random.randint(0,11)
    return listNames[nameSelect]
#creamos una funcion para elaborar el nombre de usduario de la cuenta
def createUser(name, time):
    user =  name
    listChar = ["_", "0302","2201","45","789","12","0_1","._","234","Lol","Xx","Yz"]
    for i in range(time):
        randomNumber = random.randint(0, 11)
        user += listChar[randomNumber]
    return user
#Creamos una funcion para generar una contraseña
def createKey(keyword,time):
    password = keyword
    listChar = ["1","2","45","789","12",".345","Lol","Xx","Yz", "2201","0302",".2071"]
    for i in range(time):
        randomNumber = random.randint(0, 11)
        password += listChar[randomNumber]
    return password
#creamos una funcion para la creacion y registro de la cuenta
def register():
    metaData = [] #Guardamos los datos de la cuenta
    options = Options()
    options.add_argument('https://www.instagram.com/')
    browser = webdriver.Firefox(options=options, executable_path=r'C:\Users\diego\OneDrive\Escritorio\IGBot\geckodriver.exe')
    browser.implicitly_wait(5)
    #Le damos click al boton de sing Up
    singUp_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/div/p/a")
    singUp_button.click()
    time.sleep(5)
    #Agregamos en la casilla del mail el mail que creamos anteriormente
    gmail_input = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[3]/div/label/input")
    mail =  createMail()
    gmail_input.send_keys(mail[0])
    metaData.append(mail[0])
    time.sleep(7)
    #Agregamos el nombre que creamos anteriormente
    name_user_input = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input")
    name = nameUser()
    name_user_input.send_keys(name)
    metaData.append(name)
    time.sleep(10)
    #Agregamos el nombre de usuario para la cuenta
    user_input = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/label/input")
    userRandomTime = random.randint(5, 15)
    userName = createUser(name,userRandomTime)
    user_input.send_keys(userName)
    metaData.append(userName)
    time.sleep(5)
    #Agreamos la contraseña para la cuenta
    password_input = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input")
    keyRandomTime = random.randint(5, 20)
    key = createKey("KPruebaD",keyRandomTime)
    password_input.send_keys(key)
    metaData.append(key)
    #Presionamos el boton para continuar
    sing_Up_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button")
    sing_Up_button.click()
    #Seleccionamos el año de nacimiento
    year_input = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[34]")
    year_input.click()
    #Presionamos el boton para continuar
    sendCode_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/div[6]/button")
    sendCode_button.click()
    #Presionamos para reenviar el codigo
    resentCode_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button")
    resentCode_button.click()
    print("Se envio el codigo al correo")
    getCode(mail[1])
    #return metaData
register()
