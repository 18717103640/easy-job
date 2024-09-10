from DrissionPage import ChromiumPage, ChromiumOptions


class drissionpage():
    def __init__(self):
        self.driver = ChromiumPage()

    def listen(self, match_url):
        self.driver.listen.start(match_url)

