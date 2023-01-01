# Bu projede selenium ile kaggle.com sitesinden bir veri setini indirip, pandas ile okuyup, matplotlib ile görselleştirme yapacağız.



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.kaggle.com/")
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("covid19")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until
    EC.presence_of_element_located((By.CLASS_NAME, main))
    print(main.text)
finally:
    driver.quit()

# bu kodu çalıştırdığımızda kaggle.com sitesinde covid19 araması yapıp, sonuçları görebiliriz.

# şimdi bu sonuçları pandas ile okuyalım

df = pd.read_csv("C:\Users\mert_\Desktop\covid19.csv")
print(df.head())

# şimdi bu veri setini matplotlib ile görselleştirelim

sns.set_style("darkgrid")
sns.lineplot(data=df, x="Date", y="Confirmed", hue="Country/Region")
plt.show()
