#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from fixture.group import GroupHelper
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        capabilities = DesiredCapabilities.CHROME
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--lang=en-US')
        chrome_options.add_argument('--disable-setuid-sandbox')
        chrome_options.add_argument('--no-sandbox')
        user_agent = "Chrome"
        chrome_options.add_argument('user-agent={user_agent}'
                                    .format(user_agent=user_agent))
        self.wd = WebDriver(desired_capabilities=capabilities, chrome_options=chrome_options)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://127.0.0.1:8802")

    def destroy(self):
        self.wd.quit()