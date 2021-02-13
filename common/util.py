import base64
import json
import pickle
import string
import time
from os.path import dirname
from PIL import Image
import random
import logging
from logging import handlers
import datetime
import requests
# from libs.ShowapiRequest import ShowapiRequest


def get_authcode(driver, ele_id):
    """
    使用第三方接口获取当前页面的验证码文本，按需要下载第三方库(在/libs/文件下)
    """
    # 定义图片名和对应路径
    t = time.time()
    img_path = dirname(dirname(__file__))
    picture_name1 = img_path + '/screenshots/' + str(t) + '.png'
    driver.save_screenshot(picture_name1)

    # 根据元素ID，获取验证码图片的下载地址，下载图片并保存
    ele = driver.find_element_by_id(ele_id)
    left = ele.location['x']
    top = ele.location['y']
    right = ele.size['width'] + left
    height = ele.size['height'] + top

    # retina屏幕的图片坐标需要做额外处理，获取物理像素分辨率和CSS像素分辨率之比or一个像素之比
    dpr = driver.execute_script('return window.devicePixelRatio')
    im = Image.open(picture_name1)
    img = im.crop((left * dpr, top * dpr, right * dpr, height * dpr))

    # 普通屏幕用一般方法处理
    # im = Image.open(pictuer_name1)
    # # 抠图
    # img = im.crop((left, top, right, height))

    t = time.time()
    picture_name2 = img_path + '/screenshots/' + str(t) + '.png'
    img.save(picture_name2)

    # 使用showapi三方接口获取验证码图片中的验证码文本 https://www.showapi.com/
    # r = ShowapiRequest('http://route.showapi.com/184-4', '448149', '6fa3eec41298470ab4b76c28f0936388')
    # r.addFilePara('image', picture_name2)
    # r.addBodyPara('typeId', '34')
    # r.addBodyPara('convert_to_jpg', '0')
    # r.addBodyPara('needMorePrecise', '0')
    # res = r.post()
    # logger().info(res.text)
    # return res.json()["showapi_res_body"]["Result"]

    # 使用图鉴三方接口识别验证码 http://api.ttshitu.com
    with open(picture_name2, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    req = {"username": 495822910, "password": 123456, "image": b64}
    while True:
        result = json.loads(requests.post("http://api.ttshitu.com/base64", json=req).text)
        logger().info(result)
        if result["success"]:
            return result["data"]["result"]
        else:
            continue


def gen_random_str():
    """
    随机生成8为字母+数字的字符串
    """
    random_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return random_str


def gen_random_email():
    random_email = ''.join(random.sample(string.digits, 10))
    return random_email + '@qq.com'


def save_cookie(dirver, path):
    with open(path, 'rb') as filehandler:
        cookies = dirver.get_codkies()
        print(cookies)
        pickle.dump(cookies, filehandler)  # pickle，python的序列化和反序列化模块，和json模块类似


def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)


def logger():
    logger = logging.getLogger('Testlogger')
    logger.setLevel(logging.DEBUG)

    log_path = dirname(dirname(__file__)) + '/logs/'
    rf_handler = logging.handlers.TimedRotatingFileHandler(log_path + 'all.log',
                                                           when='midnight',
                                                           backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    f_handler = logging.FileHandler(log_path + 'error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s[%(lineno)d] - %(message)s'))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger


if __name__ == '__main__':
    print(gen_random_email())
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # 海象运算法，一个表达式同时完成赋值和判断(3.8+)
    if (n := len(a)) > 10:
        print(f"List is too long ({n} elements, expected <= 10)")

    print(random.choices(population=range(10), k=2))
    print(random.choice([1, 2, 3]))

