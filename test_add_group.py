# -*- coding: utf-8 -*-

from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group


class TestAddGroup(unittest.TestCase):

    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_test_add_group(self):
        succes = True

        wd = self.wd

        self.open_home_page(wd)
        self.login(wd, username = "admin", password = "secret")
        self.create_group(wd, Group(name="testgroup", header="testheader", footer="testfooter"))
        self.return_to_groups_page(wd)
        self.logout(wd)
        self.assertTrue(succes)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://192.168.0.41:8580")

    def tearDown(self):
        self.wd.quit()

class test_simple_tests(unittest.TestCase):

    def test_failed(self):
        assert (1,2,3) == (1,2,3)

if __name__ == '__main__':
    unittest.main()
