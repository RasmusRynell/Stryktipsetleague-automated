import time

def write_bets(bets, driver, email, password):
    container = log_in(driver, email, password)
    reset_buttons(container, driver)

    for index, bet in bets.items():
        print(bet)
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
    button = container.find_element_by_xpath('/html/body/div/div[5]/div/div[1]/div[3]/div[1]')
    button.click()

def log_in(driver, email_value='', password_value=''):
    for i in range(10):
        try:
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
            time.sleep(1)
            password = driver.find_element_by_xpath('/html/body/div/div[4]/div/form/div[1]/div[1]/div[2]/div/input')
            password.send_keys(password_value)
            time.sleep(1)

            # Find and press button with xpath '/html/body/div/div[4]/div/form/div[1]/div[2]/button'
            button = driver.find_element_by_xpath('/html/body/div/div[4]/div/form/div[1]/div[2]/button')
            button.click()
            time.sleep(1)

            driver.get('https://www.stryktipsetleague.se/spel')
            time.sleep(1)
            
            # Find and press button with xpath '/html/body/div/div[5]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div/div[2]'
            button = driver.find_element_by_xpath('/html/body/div/div[5]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div/div[2]')
            button.click()
            time.sleep(1)

            container = driver.find_element_by_xpath('/html/body/div/div[5]/div/div[1]/div[2]/div/div[1]/div[2]')
            time.sleep(1)

            print('Logged in')
            return container
        except Exception as e:
            if i == 9:
                print('Failed to log in')
                raise Exception('Could not log in')

            # print e traceback
            print(e.__traceback__)
            print("Could not log in, trying again!")


    raise Exception('Could not log in')
    
def reset_buttons(container, driver):
    for i in range(1, 14):
        for j in range(1, 4):
            button = container.find_element_by_xpath(f'/html/body/div/div[5]/div/div[1]/div[2]/div/div[1]/div[2]/div[{i}]/div[1]/div[4]/div[{j}]')
            if button.get_attribute('class') == 'nrs active':
                button.click()