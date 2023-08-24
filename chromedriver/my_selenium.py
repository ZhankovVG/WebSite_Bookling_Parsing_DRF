from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

try:
    driver.get('http://127.0.0.1:8000/')
    time.sleep(3)
    
    klick_registration = driver.find_element(By.CLASS_NAME, "registration-link").click()
    time.sleep(1)
    
    username_input = driver.find_element(By.ID, 'id_username')
    username_input.clear()
    username_input.send_keys('Vitaliy111')
    time.sleep(1)
    
    email_input = driver.find_element(By.ID, 'id_email')
    email_input.clear()
    email_input.send_keys('python.developer.v@gmail.com')
    time.sleep(1)
    
    paswword_input = driver.find_element(By.ID, 'id_password1')
    paswword_input.clear()
    paswword_input.send_keys('123456789xcv')
    time.sleep(1)
    
    paswword_input = driver.find_element(By.ID, 'id_password2')
    paswword_input.clear()
    paswword_input.send_keys('123456789xcv')
    time.sleep(1)
    
    login_button = driver.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(5)
    
    
    klick_description = driver.find_element(By.CLASS_NAME, 'books').click()
    time.sleep(1)
    
    username_input = driver.find_element(By.CLASS_NAME, 'input-name')
    username_input.clear()
    username_input.send_keys('Vitaliy')
    time.sleep(1)
    
    email_input = driver.find_element(By.CLASS_NAME, 'input-email-user')
    email_input.clear()
    email_input.send_keys('python.developer.v@gmail.com')
    time.sleep(1)
    
    comment_input = driver.find_element(By.CLASS_NAME, 'input-comment')
    comment_input.clear()
    comment_input.send_keys('Nice a book')
    time.sleep(1)
    
    comment_button = driver.find_element(By.CLASS_NAME, 'button-user').click()
    time.sleep(5)
    
    
    klick_add_cart = driver.find_element(By.CLASS_NAME, 'add_cart').click()
    time.sleep(5)
    
    
except Exception as ex:
    print(ex)    
finally:
    driver.close()
    driver.quit()