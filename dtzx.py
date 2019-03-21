from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
from time import sleep
username = '用户名'
password = '密码'
# def downloadCookie():
#     driver = webdriver.Chrome()
#     driver.get('http://dyjy.dtdjzx.gov.cn/')
#     sleep(30)
#     pickle.dump(driver.get_cookies(), open("cookies.pkl", 'wb'))

# def login_cookie(driver):
#     cookies = pickle.load(open('cookies.pkl', 'rb'))
#     driver.get('http://dyjy.dtdjzx.gov.cn/')
#     for cookie in cookies:
#         driver.add_cookie(cookie)
def circleOpera(driver):
    sleep(15)
    print(driver.current_window_handle)
    try:
        driver.find_element(By.XPATH, '//*[@id="personal_list_html"]/li[1]/span[6]/a[2]').click()
    except:
        sleep(5)
        print('历史列表已全部处理完毕')
        driver.quit()
        return
    handles = driver.window_handles
    try:
        print(handles)
        driver.switch_to_window(handles[1])
        sleep(3)
        #来到新标签页，首先获取视频长度信息，然后点击播放按钮，等待播放完毕后关闭标签页
        video = driver.find_element(By.XPATH, '//*[@id="my-video_html5_api"]')
        print(video)
        # video_src = driver.execute_script("return arguments[0].currentSrc;", video)
        # print(video_src)
        #driver.execute_script("return arguments[0].play();", video)
        sleep(6)
        driver.find_element(By.XPATH, '//*[@id="my-video"]/div[5]').click()
        sleep(5)
        video_duration = driver.execute_script("return arguments[0].duration;", video)
        print(video_duration)
        #等待播放完毕
        sleep(video_duration)
    except:
        print('异常了')
    finally:
        sleep(5)
        driver.close()
        driver.switch_to_window(handles[0])
        driver.refresh()
    circleOpera(driver)


# #downloadCookie()
driver = webdriver.Chrome()
driver.get('http://dyjy.dtdjzx.gov.cn/personal')
driver.find_element(By.ID, 'username').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.ID, 'validateCode').click()
driver.execute_script("alert('请手工输入验证码')")
sleep(10)# 手工输入验证码的时间
driver.find_element(By.CSS_SELECTOR, 'a.js-submit.tianze-loginbtn').click()
sleep(5) # 历史播放列表加载完毕
#获取duration，格式11'
# duration = driver.find_element(By.XPATH,'//*[@id="personal_list_html"]/li[1]/span[3]').text
# duration_minutes = int(duration[:len(duration)-1])
# print(duration_minutes)
circleOpera(driver)

