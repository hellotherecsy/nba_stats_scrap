from selenium import webdriver
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException


#driver = webdriver.Chrome()
driver = webdriver.Safari()


def is_xpath_valid(record, path):
    try:
        record.find_element_by_xpath(path).text
        return True
    except NoSuchElementException as e:
        return False


driver.get("https://stats.nba.com/players/traditional/?sort=PTS&dir=-1&Season=2017-18&SeasonType=Regular%20Season")

button = driver.find_element_by_xpath('//div[@class="nba-stat-table"]')
button.click()
time.sleep(2)

# Make Data frame for Total save to CSV

name_index  = ['PLAYER']
stats_index = ['TEAM','AGE','GP','W','L','MIN','PTS','FGM',\
                             'FGA','FG%','3PM','3PA','3P%','FTM','FTA','FT%','OREB',\
                             'DREB','REB','AST','TOV','STL','BLK','PF','FP','DD2','TD3','+/-']


name_total = pd.DataFrame(columns=name_index)
stats_total = pd.DataFrame(columns=stats_index)


# Page index used to keep track of where we are.
page = 1

links = []


while int(page) < 12 :
        try:
                page += 1
                print(page)

                name_page = driver.find_elements_by_xpath(
                        '/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[2]/table/tbody/tr')
                for idx, name_list in enumerate(name_page):
                        name  = name_list.find_element_by_xpath('.//td[2]/a').text

                        name_data = [[name]]
                        print(name_data)

                        # Make DataFrame and append to total frame
                        names = pd.DataFrame(name_data, columns=name_index)
                        name_total = name_total.append(names, ignore_index=True)

                players = driver.find_elements_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr')

                for idx , player in enumerate(players):


                        team = player.find_element_by_xpath('.//td[3]/a').text
                        age = player.find_element_by_xpath('.//td[4]').text
                        gp = player.find_element_by_xpath('.//td[5]').text
                        w = player.find_element_by_xpath('.//td[6]').text
                        l = player.find_element_by_xpath('.//td[7]').text
                        min = player.find_element_by_xpath('.//td[8]').text
                        pts = player.find_element_by_xpath('.//td[9]').text
                        fgm = player.find_element_by_xpath('.//td[10]/a').text
                        fga = player.find_element_by_xpath('.//td[11]/a').text
                        pg_per = player.find_element_by_xpath('.//td[12]').text


                        if is_xpath_valid(player,'.//td[13]/a'):
                                th_pm = player.find_element_by_xpath('.//td[13]/a').text
                        else  :
                                th_pm = player.find_element_by_xpath('.//td[13]').text

                        if is_xpath_valid(player,'.//td[14]/a'):
                                th_pa = player.find_element_by_xpath('.//td[14]/a').text
                        else  :
                                th_pa = player.find_element_by_xpath('.//td[14]').text

                        if is_xpath_valid(player,'.//td[15]/a'):
                                th_p_per = player.find_element_by_xpath('.//td[15]/a').text
                        else  :
                                th_p_per = player.find_element_by_xpath('.//td[15]').text




                        ftm = player.find_element_by_xpath('.//td[16]').text
                        fta = player.find_element_by_xpath('.//td[17]').text
                        ft_per = player.find_element_by_xpath('.//td[18]').text

                        if is_xpath_valid(player,'.//td[19]/a'):
                                oreb = player.find_element_by_xpath('.//td[19]/a').text
                        else  :
                                oreb = player.find_element_by_xpath('.//td[19]').text



                        if is_xpath_valid(player, './/td[20]/a'):
                                dreb = player.find_element_by_xpath('.//td[20]/a').text
                        else:
                                dreb = player.find_element_by_xpath('.//td[20]').text



                        if is_xpath_valid(player, './/td[21]/a'):
                                reb = player.find_element_by_xpath('.//td[21]/a').text
                        else:
                                reb = player.find_element_by_xpath('.//td[21]').text

                        if is_xpath_valid(player, './/td[22]/a'):
                                ast = player.find_element_by_xpath('.//td[22]/a').text
                        else:
                                ast = player.find_element_by_xpath('.//td[22]').text

                        if is_xpath_valid(player, './/td[23]/a'):
                                tov = player.find_element_by_xpath('.//td[23]/a').text
                        else:
                                tov = player.find_element_by_xpath('.//td[23]').text

                        if is_xpath_valid(player, './/td[24]/a'):
                                stl = player.find_element_by_xpath('.//td[24]/a').text
                        else:
                                stl = player.find_element_by_xpath('.//td[24]').text


                        if is_xpath_valid(player, './/td[25]/a'):
                                blk = player.find_element_by_xpath('.//td[25]/a').text
                        else:
                                blk = player.find_element_by_xpath('.//td[25]').text

                        if is_xpath_valid(player, './/td[26]/a'):
                                pf = player.find_element_by_xpath('.//td[26]/a').text
                        else:
                                pf = player.find_element_by_xpath('.//td[26]').text


                        fp = player.find_element_by_xpath('.//td[27]').text
                        dd2 = player.find_element_by_xpath('.//td[28]').text
                        td3 = player.find_element_by_xpath('.//td[29]').text
                        pm = player.find_element_by_xpath('.//td[30]').text

                        stats_data = [[team,age,gp,w,l,min,pts,fgm,fga,pg_per,th_pm,\
                                        th_pa,th_p_per,ftm,fta,ft_per,oreb,dreb,reb,ast,tov,stl,blk,pf,fp,dd2,td3,pm ]]

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
                #driver.close()
                break

name_total = name_total.replace('\n','', regex=True)
name_total.to_csv("../data/nba_players_traditional_names.csv", mode='w',index=False)

stats_total = stats_total.replace('\n','', regex=True)
stats_total.to_csv("../data/nba_players_traditional_stats.csv", mode='w',index=False)

driver.close()