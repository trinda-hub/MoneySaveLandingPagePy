import unittest
from selenium import webdriver

from test_data import TestData
from locators import Locators
from pages import HomePage, WelcomePage, AdvantagesPage, MainFeaturePage, SecurityPage, DownloadPage

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=TestData.CHROME)
        # self.driver.maximize_window()
        self.driver.set_window_size(1366, 768)

    def tearDown(self):
        self.driver.quit()

class RedirectSuccess(BaseTest):
    def test_redirect_page_success(self):
        # membuat objek homepage
        self.homepage = HomePage(self.driver)

        # Step 1 - click slider home page
        self.homepage.redirect_home_page_success()

        # Step 2 - Assertion
        element_text = self.homepage.get_text(Locators.HOME_PAGE_TITLE)
        self.assertEqual("Transaksi Mudah Tanpa Gundah", element_text)

        # membuat objek welcome page
        self.welcomepage = WelcomePage(self.driver)

        # Step 3 - click slider welcome page
        self.welcomepage.redirect_welcome_page_success()

        # Step 4 - Assertion
        element_text1 = self.welcomepage.get_text(Locators.WELCOME_PAGE_TITLE)
        self.assertEqual("Selamat Datang di MoneySave", element_text1)

        # membuat objek advantage page
        self.advantagespage = AdvantagesPage(self.driver)

        # Step 5 - click slider advantages page
        self.advantagespage.redirect_advantages_page_success()

        # Step 6 - Assertion
        element_text2 = self.advantagespage.get_text(Locators.ADVANTAGES_PAGE_TITLE)
        self.assertEqual("Keuntungan menggunakan MoneySave", element_text2)

        # membuat objek main feature page
        self.mainfeaturepage = MainFeaturePage(self.driver)

        # Step 7 - Click slider main feature page
        self.mainfeaturepage.redirect_main_feature_page_success()

        # Step 8 - Assertion
        element_text3 = self.mainfeaturepage.get_text(Locators.MAIN_FEATURE_PAGE_TITLE)
        self.assertEqual("Fitur Utama MoneySave", element_text3)

        # membuat objek security page
        self.securitypage = SecurityPage(self.driver)

        # Step 9 - Click Slider security page
        self.securitypage.redirect_security_page_success()

        # Step 10 - Assertion
        element_text4 = self.securitypage.get_text(Locators.SECURITY_PAGE_TITLE)
        self.assertEqual("Keamanan kita menggunakan yang terbaik", element_text4)

        # membuat objek download page
        self.downloadpage = DownloadPage(self.driver)

        # Step 11 - Click Slider Download Page
        self.downloadpage.redirect_download_page()

        # Step 12 - Assertion
        element_text5 = self.downloadpage.get_text(Locators.DOWNLOAD_PAGE_TITLE)
        self.assertEqual("Dapatkan Sekarang", element_text5)


if __name__ == "__main__":
    unittest.main()

