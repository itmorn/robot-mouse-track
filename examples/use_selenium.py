from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pyautogui
import time


def 模拟作答1():
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/input[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/input[6]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/input[10]").click()
    time.sleep(1)
    slider = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]")
    ActionChains(driver).click_and_hold(slider).perform()
    i = 0
    distance = 358
    while i <= distance:
        ActionChains(driver).move_by_offset(20, 0).perform()
        i += 20
    ActionChains(driver).release().perform()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/button").click()
    time.sleep(1)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("file:///D:\\work_github\\robot-mouse-track-recognition\\examples\\collect_data.html")

    # 模拟作答1()
    # for i in range(100):
    #     pyautogui.moveTo(200+i*5, 200)
    pyautogui.moveTo(1000, 200)
    pyautogui.moveTo(990, 800, 10)
    time.sleep(111)
    driver.close()
