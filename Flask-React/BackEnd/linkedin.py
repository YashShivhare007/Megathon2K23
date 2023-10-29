from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv
from argparse import ArgumentParser

email = "shambhavi.jahagirdar@gmail.com"
password = "5@Monkeys"
# username = input("Enter Username: ")

#parse the arguments
def process_data_l(data):
    # value = data["linkedin"]
    # parser = ArgumentParser()
    # parser.add_argument("-l", "--link", dest="username", help="Username of user profile to be analysed", required=False, type=str)
    # args = parser.parse_args()
    username = data

    def Init():
        chrome_options = Options()
        # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        # chrome_options.add_argument(f'user-agent={user_agent}')
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options = chrome_options)
        driver.set_window_size(800, 1000)

        return driver


    def Login(driver,email,password):
        cardNo = driver.find_element(
            By.ID, "username")
        cardNo.send_keys(email)

        cardPin = driver.find_element(
            By.ID, "password")
        cardPin.send_keys(password)

        signin_button = driver.find_element(
        By.XPATH, "//button[@aria-label='Sign in']")
        signin_button.click()

        time.sleep(20)


    driver = Init()

    driver.get("https://www.linkedin.com/login")

    time.sleep(5)

    Login(driver,email,password)

    driver.get("https://www.linkedin.com/in/"+ username)

    time.sleep(5)

    text = []
    span_elements = driver.find_elements(By.XPATH, "//span[@aria-hidden='true']")
    # # span_elements = driver.find_element(By.ID, "about").find_elements(By.XPATH, ".//span[@aria-hidden='true']")
    flag = 0
    for span in span_elements:
        text_ = span.text
        if(text_ == "About"):
            flag = 1
            continue
        
        if(flag == 1):
            text.append(text_)
            flag = 0
            break
        
        print(text_)
    # text = element.text
    # print(text)

    time.sleep(10)
    driver.get("https://www.linkedin.com/in/"+ username + "/recent-activity/all/")
    time.sleep(5)
    span_elements = driver.find_elements(By.XPATH, "//span[@dir='ltr']")
    # text = []
    for span in span_elements:
        text_ = span.text
        print(text_)
        text.append(text_)

    print(text)
    text2 = [text]
    time.sleep(10)

    driver.quit()
    print("Done")


    output_csv = "linkedin.csv"
    with open(output_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(text2)
