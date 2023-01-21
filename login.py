import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLoginRegister(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_signup_success(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"signUp").click()
        time.sleep(3)
        driver.find_element(By.ID, "name_register").send_keys("hikmahsalam")
        time.sleep(2)
        driver.find_element(By.ID, "email_register").send_keys("hikmahsalam9@gmail.com")
        time.sleep(2)
        driver.find_element(By.ID, "password_register").send_keys("hikmah")
        time.sleep(2)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(3)

        response_data = driver.find_element(By.CSS_SELECTOR, "#swal2-title").text
        self.assertEqual(response_data, "berhasil")

    def test_signup_with_already_register(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"signUp").click()
        time.sleep(3)
        driver.find_element(By.ID, "name_register").send_keys("hikmahsalam")
        time.sleep(2)
        driver.find_element(By.ID, "email_register").send_keys("hikmahsalam@gmail.com")
        time.sleep(2)
        driver.find_element(By.ID, "password_register").send_keys("hikmah")
        time.sleep(2)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(3)

        response_data = driver.find_element(By.CSS_SELECTOR, "#swal2-title").text
        self.assertEqual(response_data, "Oops...")

    def test_login_success(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys("hikmahsalam@gmail.com")
        time.sleep(2)
        driver.find_element(By.ID, "password").send_keys("hikmah")
        time.sleep(2)
        driver.find_element(By.ID, "signin_login").click()
        time.sleep(3)

        response_data = driver.find_element(By.CSS_SELECTOR, "#swal2-title").text
        self.assertEqual(response_data, "Welcome hikmahsalam")
    
    def test_login_failed(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys("hikmahsal@gmail.com")
        time.sleep(2)
        driver.find_element(By.ID, "password").send_keys("hikmah")
        time.sleep(2)
        driver.find_element(By.ID, "signin_login").click()
        time.sleep(3)

        response_data = driver.find_element(By.CSS_SELECTOR, "#swal2-title").text
        self.assertEqual(response_data, "User's not found")



unittest.main()          
          