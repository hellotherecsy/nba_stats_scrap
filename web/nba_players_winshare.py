from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time


def is_xpath_valid(record, path):
    try:
        record.find_element_by_xpath(path).text
        return True
    except NoSuchElementException as e:
        return False


def is_traded_player(record, path):
    try:
        record.find_element_by_xpath(path).text
        return True
    except NoSuchElementException as e:
        return False


# Set the Driver
driver = webdriver.Safari()
# get craw url
driver.get("https://www.basketball-reference.com/leagues/NBA_2018_advanced.html")

# get Path
records = driver.find_elements_by_xpath('//*[@id="advanced_stats"]/tbody/tr')

# Make Data frame for Total save to CSV
stats_index = ['PLAYER', 'POS', 'AGE', 'TEAM', 'GAME', 'MP', 'PER', 'TS%', '3PAR', 'FTR', 'ORB%', 'DRB%', 'TRB%', \
               'AST%', 'STL%','BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP']

stats_total = pd.DataFrame(columns=stats_index)

try:
    for idx, record in enumerate(records):
        if is_xpath_valid(record, './/td[1]/a'):
            name = record.find_element_by_xpath('.//td[1]/a').text
            pos = record.find_element_by_xpath('.//td[2]').text
            age = record.find_element_by_xpath('.//td[3]').text
            #team = record.find_element_by_xpath('.//td[4]/a').text
            if is_traded_player(record, './/td[4]/a'):
                team = record.find_element_by_xpath('.//td[4]/a').text
            else:
                team = record.find_element_by_xpath('.//td[4]').text

            game = record.find_element_by_xpath('.//td[5]').text
            mp = record.find_element_by_xpath('.//td[6]').text
            per = record.find_element_by_xpath('.//td[7]').text
            ts_prt = record.find_element_by_xpath('.//td[8]').text
            th_par = record.find_element_by_xpath('.//td[9]').text
            ftr = record.find_element_by_xpath('.//td[10]').text
            orb = record.find_element_by_xpath('.//td[11]').text
            drb = record.find_element_by_xpath('.//td[12]').text
            trb = record.find_element_by_xpath('.//td[13]').text
            ast = record.find_element_by_xpath('.//td[14]').text
            stl = record.find_element_by_xpath('.//td[15]').text
            blk = record.find_element_by_xpath('.//td[16]').text
            tov = record.find_element_by_xpath('.//td[17]').text
            usg = record.find_element_by_xpath('.//td[18]').text
            ows = record.find_element_by_xpath('.//td[19]').text
            dws = record.find_element_by_xpath('.//td[20]').text
            ws = record.find_element_by_xpath('.//td[21]').text
            ws_per_all = record.find_element_by_xpath('.//td[22]').text
            obpm = record.find_element_by_xpath('.//td[23]').text
            dbpm = record.find_element_by_xpath('.//td[24]').text
            bpm = record.find_element_by_xpath('.//td[25]').text
            vorp = record.find_element_by_xpath('.//td[26]').text

            record_data = [[name, pos, age, team, game, mp, per, ts_prt, th_par, ftr, orb, drb, trb, ast \
                               , stl, blk, tov, usg, ows, dws, ws, ws_per_all, obpm, dbpm, bpm, vorp]]

            # Save Team record to Dataframe

            print(record_data)

            team_stat = pd.DataFrame(record_data, columns=stats_index)
            stats_total = stats_total.append(team_stat, ignore_index=True)

except NoSuchElementException as e:
    print(e)
    pass
    driver.close()

stats_total = stats_total.replace('\n', '', regex=True)
stats_total.to_csv("../data/nba_players_winshare_stats.csv", mode='w', index=False)

driver.close()

