import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])
def test_step1():

    x_selector1 = '//*[@id="username"]'
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("greenlemur28@gmail.com")
    x_selector2 = '//*[@id="password"]'
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("")
    btn_selector = "p:nth-child(3) > button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_selector3 = "/html/body/main/section/div/div/div/div[3]/div[1]/ul/li"
    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == "ОШИБКА: Вы не ввели пароль."


test_step1()