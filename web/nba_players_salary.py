from selenium import webdriver
import pandas as pd
import time


driver = webdriver.Safari()

# get craw salary url
driver.get("http://www.espn.com/nba/salaries/_/year/2018/seasontype/1")

# get Path
salary_page = driver.find_elements_by_xpath('//*[@id="my-players-table"]/div/div[2]/table/tbody/tr')

# Make Data frame for Total save to CSV
stats_index =['NAME','TEAM','SALARY']

stats_total = pd.DataFrame(columns=stats_index)
try:
        for idx, page in enumerate(salary_page):
                print(idx+1)
                if (idx+1) % 11 != 1 :
                        name = page.find_element_by_xpath('.//td[2]/a').text
                        team = page.find_element_by_xpath('.//td[3]/a').text
                        salary = page.find_element_by_xpath('.//td[4]').text


                        salary_data = [[name,team,salary]]

                        # Save Team record to Dataframe
                        print(salary_data)

                        salary_stat = pd.DataFrame(salary_data, columns=stats_index)
                        stats_total = stats_total.append(salary_stat, ignore_index=True)

except Exception as e:
        print(e)
        driver.close()


stats_total = stats_total.replace('\n','', regex=True)
stats_total.to_csv("../data/nba_players_salary.csv", mode='w',index=False)

driver.close()