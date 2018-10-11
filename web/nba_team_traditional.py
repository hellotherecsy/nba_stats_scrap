from selenium import webdriver
import pandas as pd
import time


driver = webdriver.Safari()

# get craw url
driver.get("https://stats.nba.com/teams/traditional/?sort=W&dir=-1&Season=2017-18&SeasonType=Regular%20Season")

# get Path
team = driver.find_elements_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr')

# Make Data frame for Total save to CSV
stats_index =['TEAM','GP','W','L','WIN%','MIN','PTS','FGM','FGA','FG%','3PM','3PA','3P%','FTM','FTA', \
              'FT%','OREB','DREB','REB','AST','TOV','STL','BLK','BLKA','PF','PFD','+-']

stats_total = pd.DataFrame(columns=stats_index)
try:
        for idx, team in enumerate(team):
                name = team.find_element_by_xpath('.//td[2]/a').text
                gp = team.find_element_by_xpath('.//td[3]').text
                w = team.find_element_by_xpath('.//td[4]').text
                l = team.find_element_by_xpath('.//td[5]').text
                win_per = team.find_element_by_xpath('.//td[6]').text
                mini = team.find_element_by_xpath('.//td[7]').text
                pts = team.find_element_by_xpath('.//td[8]').text
                pgm = team.find_element_by_xpath('.//td[9]/a').text
                pga = team.find_element_by_xpath('.//td[10]/a').text
                pg_per =   team.find_element_by_xpath('.//td[11]').text
                th_pm = team.find_element_by_xpath('.//td[12]/a').text
                th_pa = team.find_element_by_xpath('.//td[13]/a').text
                th_p_per = team.find_element_by_xpath('.//td[14]').text
                ftm = team.find_element_by_xpath('.//td[15]').text
                fta = team.find_element_by_xpath('.//td[16]').text
                ft_per = team.find_element_by_xpath('.//td[17]').text
                oreb = team.find_element_by_xpath('.//td[18]/a').text
                dreb = team.find_element_by_xpath('.//td[19]/a').text
                reb = team.find_element_by_xpath('.//td[20]/a').text
                ast = team.find_element_by_xpath('.//td[21]/a').text
                tov = team.find_element_by_xpath('.//td[22]/a').text
                stl  = team.find_element_by_xpath('.//td[23]/a').text
                blk = team.find_element_by_xpath('.//td[24]/a').text
                blka = team.find_element_by_xpath('.//td[25]/a').text
                pf = team.find_element_by_xpath('.//td[26]').text
                pfd = team.find_element_by_xpath('.//td[27]').text
                plusMinus = team.find_element_by_xpath('.//td[28]').text

                team_data = [[name, gp, w, l, win_per, mini, pts, pgm, pga, pg_per, th_pm \
                                     ,th_pa, th_p_per, ftm, fta, ft_per, oreb, dreb \
                                     ,reb, ast, tov, stl, blk, blka, pf, pfd, plusMinus]]

                # Save Team record to Dataframe

                print(team_data)

                team_stat = pd.DataFrame(team_data, columns=stats_index)
                stats_total = stats_total.append(team_stat, ignore_index=True)

except Exception as e:
        print(e)
        driver.close()


stats_total = stats_total.replace('\n','', regex=True)
stats_total.to_csv("../data/nba_team_traditional_stats.csv", mode='w',index=False)

driver.close()