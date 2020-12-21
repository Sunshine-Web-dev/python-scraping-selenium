import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing import Pool

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# import requests

URL = 'https://app.dealroom.co/investors.lps'
driver = ""
cnt_num = 5
short_sleep = 5


def open():
  driver.set_window_size(1920, 1080)
  driver.get(URL)

def getData():
  print("getting data ...")


  try:
    # login section
    login =  driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/header/div[2]/div/button[2]')[0]
    login.click()
    time.sleep(10)
    driver.find_element_by_id("login-form__first-input").clear()
    driver.find_element_by_id("login-form__first-input").send_keys("alexis.caporale@trimaker.com")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("poweruser")
    login_submit = driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div/div/form/button')[0]
    login_submit.click()
    time.sleep(3)

    # //----------------------//
    table_list_wrapper = driver.find_elements_by_class_name('table-list-wrapper')[0]
    table_list_rows = table_list_wrapper.find_elements_by_class_name('table-list-item')
    
    for row in table_list_rows:
      title = row.find_elements_by_class_name('entity-name__name--black')[0].find_element(By.CSS_SELECTOR, 'a:first-child').text
      type = row.find_elements_by_class_name('type-element')[1].text

      print(title)
      print(type)
      el_2 = row.find_elements_by_class_name('table-list-columns')[0]
      preferredRound = el_2.find_elements_by_class_name('preferredRound')[0].text
      print(preferredRound)
      lpInvestmentsNum = el_2.find_elements_by_class_name('lpInvestmentsNum')[0].text
      print(lpInvestmentsNum)
      investments = el_2.find_elements_by_class_name('comma-list-column')[0].find_elements_by_tag_name('a')
      for investment in investments:
        print(investment.text)
      hqAllLocations = el_2.find_elements_by_class_name('hqAllLocations')[0].text
      print(hqAllLocations)
      dealSize = el_2.find_elements_by_class_name('dealSize')[0].text
      print(dealSize)
      prominences  = el_2.find_elements_by_class_name('prominence')[0].find_elements_by_tag_name('span')
      for prominence in prominences:
        print(prominence.text)
      investorTotalFunding = el_2.find_elements_by_class_name('investorTotalFunding')[0].text
      print(investorTotalFunding)
      investorPorfolioSize =  el_2.find_elements_by_class_name('investorPorfolioSize')[0].text
      print(investorPorfolioSize)
      x = range(6)
      for scroll_right in x:
        scroll_right = driver.find_elements_by_xpath('//*[@id="list-map-list"]/div[1]/div[1]/div/button[1]')[0]
        scroll_right.click()
      investmentsValuation = el_2.find_elements_by_class_name('investmentsValuation')[0].text
      print(investmentsValuation)
      investments = el_2.find_elements_by_class_name('investments')[0].find_elements_by_tag_name('a')
      for investment in investments:
        print(investment.text)
      investorExitsNum = el_2.find_elements_by_class_name('investorExitsNum')[0].text
      print(investorExitsNum)
      investorExitScore = el_2.find_elements_by_class_name('investorExitScore')[0].text
      print(investorExitScore)
      investorExitsFunding = el_2.find_elements_by_class_name('investorExitsFunding')[0].text
      print(investorExitsFunding)
      y = range(6)
      for scroll_left in y:
        scroll_left = driver.find_elements_by_xpath('//*[@id="list-map-list"]/div[1]/div[1]/div/div[1]/div/button')[0]
        scroll_left.click()
            

      
  except TimeoutException:
    print("email field is not ready")
    pass



  

if __name__ == "__main__":
  driver = webdriver.Chrome('driver_87/chromedriver')
  open()
  time.sleep(short_sleep)
  getData()

