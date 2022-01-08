import time
import json

def write_bets(bets, driver, email, password):
    log_in(driver, email, password)

    try:
        container = driver.find_element_by_xpath('/html/body/div/div[5]/div/div[1]/div[2]/div/div[1]/div[2]')
    except:
        print('\033[91m' + "Stryktipsetleague is not open! bets not written" + '\033[0m')
        return
   
    reset_buttons(container)

    for index, bet in bets.items():
        if "1" in bet:
            button = container.find_element_by_xpath(f'/html/body/div/div[5]/div/div[1]/div[2]/div/div[1]/div[2]/div[{index}]/div[1]/div[4]/div[1]')
            button.click()
        if "X" in bet:
            button = container.find_element_by_xpath(f'/html/body/div/div[5]/div/div[1]/div[2]/div/div[1]/div[2]/div[{index}]/div[1]/div[4]/div[2]')
            button.click()
        if "2" in bet:
            button = container.find_element_by_xpath(f'/html/body/div/div[5]/div/div[1]/div[2]/div/div[1]/div[2]/div[{index}]/div[1]/div[4]/div[3]')
            button.click()

    # Find button with xpath '/html/body/div/div[5]/div/div[1]/div[3]/div[1]'
    try:
        button = container.find_element_by_xpath('/html/body/div/div[5]/div/div[1]/div[3]/div[1]')
        button.click()
        print("Placing bets for the first time")
    except:
        try:
            button = container.find_element_by_xpath('/html/body/div/div[5]/div/div[1]/div[3]/div[2]')
            button.click()
            print("Redoing bets")
        except:
            print('\033[91m' + "No button found, nothing has changed" + '\033[0m')

    time.sleep(1)



def log_in(driver, email_value='', password_value=''):
    driver.get('https://www.stryktipsetleague.se/spel')
    time.sleep(1)

    # find and click button with xpath '/html/body/div/div[8]/div[2]/div/div[1]/div/div'
    button = driver.find_element_by_xpath('/html/body/div/div[8]/div[2]/div/div[1]/div/div')
    button.click()
    time.sleep(1)

    # find and cluck button with xpath '/html/body/div/div[7]/div/div[1]'
    button = driver.find_element_by_xpath('/html/body/div/div[7]/div/div[1]')
    button.click()
    time.sleep(1)

    # find fill mail with 'mail' and password with 'password'
    email = driver.find_element_by_xpath('/html/body/div/div[4]/div/form/div[1]/div[1]/div[1]/div/input')
    email.send_keys(email_value)
    password = driver.find_element_by_xpath('/html/body/div/div[4]/div/form/div[1]/div[1]/div[2]/div/input')
    password.send_keys(password_value)

    # Find and press button with xpath '/html/body/div/div[4]/div/form/div[1]/div[2]/button'
    button = driver.find_element_by_xpath('/html/body/div/div[4]/div/form/div[1]/div[2]/button')
    button.click()
    time.sleep(1)

    driver.get('https://www.stryktipsetleague.se/spel')
    time.sleep(1)
    

    # Find and press button with xpath '/html/body/div/div[5]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div/div[2]'
    try:
        button = driver.find_element_by_xpath('/html/body/div/div[5]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div/div[2]').click()
    except:
        try:
            button = driver.find_element_by_xpath('/html/body/div/div[5]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div/div').click()
        except:
            print('No button found')
    
def reset_buttons(container):
    old = {}
    for i in range(1, 14):
        game = ""
        for j in range(1, 4):
            button = container.find_element_by_xpath(f'/html/body/div/div[5]/div/div[1]/div[2]/div/div[1]/div[2]/div[{i}]/div[1]/div[4]/div[{j}]')
            if button.get_attribute('class') == 'nrs active':
                button.click()
                game += str(j if j == 1 else ("X" if j == 2 else "2"))
        old[i] = game
    return old