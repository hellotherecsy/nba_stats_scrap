from selenium import webdriver
import pandas as pd
import time

#driver = webdriver.Chrome()
driver = webdriver.Safari()

#driver.get("https://stats.nba.com/leaders/")
driver.get("https://stats.nba.com/leaders/?Season=2017-18&SeasonType=Regular%20Season")

button = driver.find_element_by_xpath('//div[@class="nba-stat-table"]')
button.click()
time.sleep(2)

#players = driver.find_elements_by_xpath(
#    '/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr')
#players = driver.find_elements_by_xpath('.//div[2]/div[1]/table/tbody/tr')

# Make Data frame for Total save to CSV
stats_index = ['PLAYER','GP','MIN','PTS','FGM','FGA','FG%','3PM','3PA','3P%','FTM','FTA','FT%','OREB','DREB','REB','AST','STL','BLK','TOV','EFF']
stats_total = pd.DataFrame(columns=stats_index)


# Page index used to keep track of where we are.
page = 1

links = []
while int(page) < 7 :
        try:
                page += 1
                print(page)
                players = driver.find_elements_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr')
                for idx , player in enumerate(players):
                        index = player.find_element_by_xpath('.//td[1]').text
                        name  = player.find_element_by_xpath('.//td[2]/a').text
                        gp    = player.find_element_by_xpath('.//td[3]').text
                        min  = player.find_element_by_xpath('.//td[4]').text
                        pts = player.find_element_by_xpath('.//td[5]').text
                        pgm = player.find_element_by_xpath('.//td[6]').text
                        pga = player.find_element_by_xpath('.//td[7]').text
                        pg_per = player.find_element_by_xpath('.//td[8]').text
                        th_pm = player.find_element_by_xpath('.//td[9]').text
                        th_pa = player.find_element_by_xpath('.//td[10]').text
                        th_p_per = player.find_element_by_xpath('.//td[11]').text
                        ptm = player.find_element_by_xpath('.//td[12]').text
                        pta = player.find_element_by_xpath('.//td[13]').text
                        pt_per = player.find_element_by_xpath('.//td[14]').text
                        oreb = player.find_element_by_xpath('.//td[15]').text
                        dreb = player.find_element_by_xpath('.//td[16]').text
                        reb = player.find_element_by_xpath('.//td[17]').text
                        ast = player.find_element_by_xpath('.//td[18]').text
                        stl = player.find_element_by_xpath('.//td[19]').text
                        blk = player.find_element_by_xpath('.//td[20]').text
                        tov = player.find_element_by_xpath('.//td[21]').text
                        eff = player.find_element_by_xpath('.//td[22]').text

                        stats_data = [[ name,gp,min,pts,pgm,pga,pg_per,th_pm,th_pa,th_p_per,ptm,pta,pt_per,oreb \
                                           ,dreb,reb,ast,stl,blk,tov,eff]]
                        print(stats_data)

                        # Make DataFrame and append to total frame
                        player_stat = pd.DataFrame(stats_data,columns=stats_index)
                        stats_total = stats_total.append(player_stat,ignore_index=True)

                # Locate the next button element on the page and then call `button.click()` to click it.

                button = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[3]/div/div/a[2]')
                button.click()
                time.sleep(2)

        except Exception as e:
                print(e)
                driver.close()
                break

stats_total = stats_total.replace('\n','', regex=True)
stats_total.to_csv("../data/nba_players_advanced_stats.csv", mode='w',index=False)

driver.close()