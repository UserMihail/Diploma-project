import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])
def test_step1():

    x_selector1 = '//*[@id="reg_email"]'
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("greenlemur28@gmail.com")
    # customer_login > div.u-column2.col-2 > form > p.woocommerce-FormRow.form-row > button
    btn_selector = "p.woocommerce-FormRow.form-row > button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_selector3 = '/html/body/main/section/div/div/div/div[3]/div[1]/ul/li/strong'
    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == "Ошибка:"

test_step1()