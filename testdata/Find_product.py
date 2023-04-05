import time

from appium.webdriver import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that

from Demo1.demo1 import des_cap
from caption_project_2.base.appium_listener import AppiumConfig


class TestAndroidDeviceLocal(AppiumConfig):
    def test_subscribe_python_basic(self):
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        #self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Skip for now']").click()
        time.sleep(20)
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Offers']").click()
        time.sleep(20)
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Beauty']").click()
        time.sleep(20)
        para_dic = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR,
                    "selector": 'UiSelector().text("Your Dermat for Dark Spots!")'}
        self.driver.execute_script("mobile: scroll", para_dic)
        self.driver.find_element(AppiumBy.ID, "com.fsn.nykaa:id/actionbar_icon").send_keys("shampoo").click()