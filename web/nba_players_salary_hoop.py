from selenium import webdriver
import pandas as pd
import time


driver = webdriver.Safari()

# get craw salary url
driver.get("https://hoopshype.com/salaries/players/2017-2018/")

# Make Data frame for Total save to CSV
stats_index =['PLAYER','SALARY']
stats_total = pd.DataFrame(columns=stats_index)

try:
    # get Path
    salary_page = driver.find_elements_by_xpath('//*[@id="content-container"]/div/div[3]/div[2]/div/div[2]/table/tbody/tr')

    for idx, page in enumerate(salary_page):

        player = page.find_element_by_xpath('.//td[2]/a').text
        salary = page.find_element_by_xpath('.//td[3]').text

        player = player.encode('utf-8').strip()
        salary_data = [[player, salary.strip()]]
        print(salary_data)

        salary_stat = pd.DataFrame(salary_data, columns=stats_index)
        stats_total = stats_total.append(salary_stat, ignore_index=True)

except Exception as e:
    print(e)
    #driver.close()


stats_total = stats_total.replace('\n','', regex=True)

## ETL
#salary['SALARY'] = salary['SALARY'].str.replace(',', '')
#salary['SALARY'] = salary['SALARY'].str.replace('$', '')
#salary['SALARY'] = salary['SALARY'].astype(int)

#salary['PLAYER'] = salary['PLAYER'].str.replace('b', '')
#salary['PLAYER'] = salary['PLAYER'].str.replace("'", '')
try:
    salary['PLAYER'] = salary['PLAYER'].str.decode('utf-8')
except Exception as e:
    pass

stats_total.to_csv("../data/nba_players_salary_hoop.csv", mode='w',index=False)

driver.close()