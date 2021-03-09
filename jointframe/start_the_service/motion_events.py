#! -*- coding: utf-8 -*-
__author__ = 'Yan.zhe 2021.2.1'

import cv2
import random
import json
import piexif
import requests
import subprocess
import numpy as np
from loguru import logger
from PIL import ImageFont, Image, ImageDraw
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import datetime
from dateutil import rrule


class MotionEvents(object):

    def __init__(self, driver):
        self.driver = driver
        self.screen_size = self.driver.get_window_size()

    def find_element_id(self, page_id, timeout=5):
        try:
            WebDriverWait(self.driver, timeout, 1).until(lambda driver: self.driver.find_element_by_android_uiautomator(
                'new UiSelector().resourceId("' + str(page_id) + '")').is_displayed())
            logger.info("Find the page element:{page_id}".format(page_id=page_id))
            return self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("' + str(page_id) + '")')
        except (AttributeError, TimeoutException)as e:
            logger.warning("Not find the page element:{page_id}".format(page_id=page_id))
            logger.error(e)

    def find_element_text(self, text, timeout=5):
        try:
            WebDriverWait(self.driver, timeout, 1).until(lambda driver: self.driver.find_element_by_android_uiautomator(
                'new UiSelector().text("' + str(text) + '")').is_displayed())
            logger.info("Find the page element:{page_text}".format(page_text=text))
            return self.driver.find_element_by_android_uiautomator('new UiSelector().text("' + str(text) + '")')
        except (AttributeError, TimeoutException)as e:
            logger.warning("Not find the page element:{page_text}".format(page_text=text))
            return None

    def swipe_down_until_find(self):

        def func(text):

            the_result_of_the_search = self.find_element_text(text)
            count = 0
            while count <= 10:
                if the_result_of_the_search is None:
                    self.driver.swipe(self.screen_size['width'] * 0.5, self.screen_size['height'] * 0.5,
                                      self.screen_size['width'] * 0.5, self.screen_size['height'] * 0.3, 200)
                else:
                    logger.info("{page_text} was spotted on the screen".format(page_text=text))
                    break
                count += 1
        return func

    def swipe_up_until_find(self):

        def func(text):

            the_result_of_the_search = self.find_element_text(text)
            count = 0
            while count <= 10:
                if the_result_of_the_search is None:
                    self.driver.swipe(self.screen_size['width'] * 0.5, self.screen_size['height'] * 0.3,
                                      self.screen_size['width'] * 0.5, self.screen_size['height'] * 0.5, 200)
                else:
                    logger.info("{page_text} was spotted on the screen".format(page_text=text))
                    break
                count += 1
        return func

    @staticmethod
    def send_cmd(cmd, encoding='utf-8'):
        res = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, encoding=encoding)
        com = res.communicate()
        value = com[0]
        res.terminate()
        return value

    def launch_app(self, udid, app_package, app_activity):
        try:
            cmd = "adb -s " + str(udid) + " shell am start -n " + str(app_package) + "/" + str(
                app_activity)
            res = self.send_cmd(cmd).strip()
            logger.info("start app：{cmd}----->{res}".format(cmd=cmd, res=res))
        except Exception as err:
            logger.info("start app failed {page_text}".format(page_text=err))
            raise Exception("start app failed：%s" % str(err))

    @staticmethod
    def picture_generator(picture_name):
        """
        :param picture_name: Name of picture file
        :return: Create images in the method directory
        """
        width = 500
        height = 500
        img = np.zeros([width, height, 3], dtype=np.uint8)
        for width in range(width):
            for height in range(height):
                img[width, height, :] = [width % 500, height % 500, (width + height) % 500]

        cv2.imwrite("{picture_name}.jpg".format(picture_name=picture_name), img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def write_picture(picture_name, picture_content, picture_time):
        """
        :param picture_time: Modify the time the image was taken,such as  "2013:12:19 10:10:10"
        :param picture_content: Add image content
        :param picture_name: It has to be the same as picture_generator parameters
                def picture_generator(picture_name):   write_picture(picture_name):
        """
        try:
            bk_img = cv2.imread("{picture_name}.jpg".format(picture_name=picture_name))
        except AttributeError as error:
            logger.warning("{picture_name} was not found, please confirm it again".format(picture_name=picture_name))
            return None

        # Sets the font you want to display
        font_path = "font/simsun.ttc"
        font = ImageFont.truetype(font_path, 32)
        img_pil = Image.fromarray(bk_img)
        draw = ImageDraw.Draw(img_pil)

        exif_ifd = {
            piexif.ExifIFD.DateTimeOriginal: picture_time,
            piexif.ExifIFD.DateTimeDigitized: picture_time,
        }
        exif_dict = {"Exif": exif_ifd}
        exif_bytes = piexif.dump(exif_dict)
        im = Image.open(picture_name)
        im.save(picture_name, exif=exif_bytes)
        draw.text((0, 0), picture_time, font=font, fill=(255, 255, 255))

        # Draw text message
        draw.text((0, 50), picture_content, font=font, fill=(255, 255, 255))
        bk_img = np.array(img_pil)
        cv2.waitKey()
        create_name = picture_content + ".jpg"
        cv2.imwrite(create_name, bk_img)

    @staticmethod
    def difference_value_month(start_date, end_date):
        """
        :param start_date:  for example 2021-02-18
        :param end_date:  for example 2020-02-18
        :return: Return absolute value
        """

        start_date_list = start_date.split('-')
        start_date_year = int(start_date_list[0])
        start_date_month = int(start_date_list[1])

        end_date_list = end_date.split('-')
        end_date_year = int(end_date_list[0])
        end_date_month = int(end_date_list[1])

        interval = (end_date_year - start_date_year) * 12 + (end_date_month - start_date_month)
        return abs(interval)

    @staticmethod
    def random_name():
        first_name = "严"
        boy = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'
        girl = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'
        last_name = '中笑贝凯歌易仁器义礼智信友上都卡被好无九加电金马钰玉忠孝'
        sex = random.choice(range(2))
        name_select = ''
        if sex > 0:
            girl_name = girl[random.choice(range(len(girl)))]
            if random.choice(range(2)) > 0:
                name_select = last_name[random.choice(range(len(last_name)))]
            name = [first_name, name_select+girl_name]
            return name
        else:
            boy_name = boy[random.choice(range(len(boy)))]
            if random.choice(range(2)) > 0:
                name_select = last_name[random.choice(range(len(last_name)))]
            name = [first_name, name_select+boy_name]
            return name

    @staticmethod
    def random_email(email_type=None, rang=None):
        """
        :param email_type:  email type qq.com
        :param rang:  random.randint(4, 10)
        :return: Return a random email
        """
        __email_type = ["@qq.com", "@163.com", "@126.com", "@189.com"]
        if email_type is not None:
            __randomEmail = email_type
        else:
            __randomEmail = random.choice(__email_type)
        if rang is not None:
            __rang = int(rang)
        else:
            __rang = random.randint(4, 10)
        __Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
        __randomNumber = "".join(random.choice(__Number) for i in range(__rang))
        _email = __randomNumber + __randomEmail
        return _email

    def binding_frame(self, frame_id):
        random_name = self.random_name()
        random_email = self.random_email()
        logger.success("The email address of this account is: {random_email}, password is ybc19940829".format(random_email=random_email))
        url_register = "https://vtop.aiframe.net/users/"
        data_register = {"email": random_email, "password": "ybc19940829", "firstName": random_name[0],
                         "lastName": random_name[1], "sex": "MALE"}
        token_register = ""
        headers_register = {"Content-Type": "application/json; charset=utf-8",
                            "Authorization": token_register}
        user_id = json.loads(requests.post(url=url_register, data=json.dumps(data_register), headers=headers_register).text)['id']

        # login ,get token
        url_login = "https://vtop.aiframe.net/uaa/oauth/token"
        data_login = {"username": random_email, "password": "ybc19940829", "grant_type": "password", "client_id": "app"}
        headers_login = {"Content-Type": "application/json; charset=utf-8",
                         "Authorization": ""}
        res = requests.post(url=url_login, params=data_login, headers=headers_login)
        result = res.json()
        token_type = result["token_type"].strip()
        access_token = result["access_token"].strip()
        token = token_type.title() + " " + access_token

        # binding
        url = "https://vtop.aiframe.net/frame/users/{}/frames".format(user_id)
        data = {"frameId": frame_id, "nickname": random_name[0] + " " + random_name[1]}
        headers = {"Content-Type": "application/json; charset=utf-8",
                   "Authorization": token}
        requests.post(url=url, data=json.dumps(data), headers=headers)
        return_token = {
                        "token": token,
                        "user_id": user_id,
                        "headers": headers,
                        "frame_id": frame_id
                        }
        return return_token

    @staticmethod
    def send_images(return_token=dict):
        user_id = return_token['user_id']
        token = return_token['token']
        headers = return_token['headers']
        frame_id = return_token['frame_id']
        url = "https://frame-versions.oss-cn-shenzhen.aliyuncs.com/test_pics/test_factory_1.jpg"
        # value_1 = '{' + '"descriptions":["{}"],"loginToken":"{}","pushId":"{}","uniqueId":"{}","uniqueNums":["{}"],'.format(
        #     "", token, "", user_id, frame_id)
        # value_2 = '"urls":["{}"]'.format(url) + '}'
        data = {
                'files': [{"url": url, "size": "100", "mimeType": "jpg", "md5": "1231131346"}],
                'userId': user_id,
                'frameIds': [frame_id],
                'loginToken': token
        }
        update_url = "https://vtop.aiframe.net/frame/medias/push"
        requests.post(url=update_url, data=json.dumps(data), headers=headers)

    def clean_text(self, text):
        self.driver.keyevent(123)
        for i in range(0, len(text)):
            self.driver.keyevent(67)
