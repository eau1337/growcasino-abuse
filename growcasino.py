from selenium import webdriver
import random, time, string, os, json, requests, json, warnings
from twocaptcha import TwoCaptcha
refcodes = "system";password = "Password332!";sleeptime = 1.0;global solution;solution = "";words = [];os.system("title growcasino.pwn by sa#0006"); warnings.filterwarnings("ignore", category=DeprecationWarning) 
def watermark(): print("""\n\n\n\n\n\n
       ___   ____
        /' --;^/ ,-_\     \ | /                       
       / / --o\ o-\ \\   --(_)--
      /-/-/|o|-|\-\\|\\   / | \    
       '`  ` |-|   `` '
             |-|
█▀▀▀ █▀▀█ █▀▀█ █   █ █▀▀▀ █▀▀ █▀▀▄ 
█ ▀█ █▄▄▀ █  █ █▄█▄█ █░▀█ █▀▀ █  █ 
▀▀▀▀ ▀ ▀▀ ▀▀▀▀  ▀ ▀  ▀▀▀▀ ▀▀▀ ▀  ▀
             |-|O
             |-(\,__
          ...|-|\--,\_....
      ,;;;;;;;;;;;;;;;;;;;;;;;;,.
~~,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\n\n\n
    """)
with open('words.txt') as f:
    for line in f: words.append(line)
    f.close()
def randomstring(n): return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(n))
def generate():
    word1 = str(random.choice(words).replace("\n", ""))
    if random.randint(1,2) == 1: word1 = word1.title()
    else: pass
    fy = f'{(word1)}{random.randint(10, 999)}'; print(fy); return(fy)
charm = webdriver.DesiredCapabilities.CHROME.copy();charm['goog:loggingPrefs'] = { 'performance':'ALL' };c = webdriver.ChromeOptions();c.add_argument("--incognito");c.add_experimental_option("detach", True)
def store_account_data(x): f = open("accounts.txt","a"); f.write(x + "\n"); f.close()
def makeacc():
    while True:
        try:
            x = True;y = requests.get('https://ws.growcasino.net/')
            if "Web server is down" in str(y.content): x = False
            if not x:print("[x] GrowCasino is currently down")
            else:break
        except:continue      
    global solution;account_details = [generate(), password, (randomstring(8) + "@" + randomstring(8) + ".com")]
    if len(account_details[0]) > 15: account_details[0] = generate()
    driver = webdriver.Chrome(".\\chromedriver.exe", options=c, desired_capabilities=charm);driver.get("https://growcasino.net/");driver.maximize_window();time.sleep(sleeptime);driver.find_element_by_class_name('btn-secondary').click()
    try:
        driver.find_element_by_class_name('form-check-input').click();driver.find_element_by_name("username").send_keys(account_details[0]);driver.find_element_by_name("password").send_keys(account_details[1]);driver.find_element_by_name("email").send_keys(account_details[2]);driver.find_element_by_name("refCode").send_keys(refcodes)
        store_account_data((str(account_details[0]) + ":" + str(account_details[1])))
    except Exception as e: print("[Error]", str(e))

if __name__ == '__main__':
    watermark()
    makeacc()