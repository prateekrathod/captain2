import pytest
from appium import webdriver

from caption_project_2.utilities import read_utils


class AppiumConfig:

    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        json_dic = read_utils.get_dic_from_json("../testdata/config.json")

        if json_dic["device"] == "local":
            des_cap = {
                "platformName": "Android",
                "deviceName": "samsung",
                "app": r"C:\Users\144139\Downloads\nykaa-3-1-6.apk",
                "noReset": True,
            }
        else:
            des_cap = {
                "app": "bs://e1cb3546b0247300fa3d2f026f0cff1858a932cb",
                "platformVersion": "9.2",
                "deviceName": "Samsung Galaxy M53",
                "bstack:options": {
                    "projectName": "Nykaa app Android Project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    # Set your access credentials
                    "userName": "prateek_mnRQ1A",
                    "accessKey": "yUfMaqx5UHC4xP66fMwF"
                }
            }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()