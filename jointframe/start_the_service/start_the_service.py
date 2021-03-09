#! -*- coding: utf-8 -*-
__author__ = 'Yan.zhe 2021.2.1'


from abc import ABCMeta, abstractmethod
import subprocess
import re
import socket
from appium import webdriver
from urllib3.exceptions import MaxRetryError
from loguru import logger
__all__ = ['App', 'AppStore']


class App(object):
    """
        Include the name of the app and open the corresponding module before the operation is automated
        Usage:
            def prepare():          Open the service of appium
            def get_device_port():  Get the equipment
            def get_device_name():  Get device name
            def skip_the_wizard_page(): Skip the wizard page, optional
            def start_the_app():    Start the app
    """
    _instance = None

    app_name = None
    app_Activity = None
    app_Package = None
    newCommandTimeout = None
    platformName = None
    platformVersion = None
    host_appium = '127.0.0.1'
    port = 6000
    appium_port = 4723

    # Get the device name
    @staticmethod
    def devices_name() -> list:
        res = subprocess.Popen('adb devices', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, encoding='utf-8').communicate()[0]
        devices_name_list = re.findall("\n(.+?)\t", res, re.S)
        return devices_name_list

    # udid and deviceName have the same value
    @staticmethod
    def devices_udid() -> list:
        res = subprocess.Popen('adb devices', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, encoding='utf-8').communicate()[0]
        udid_list = re.findall("\n(.+?)\t", res, re.S)
        return udid_list

    # Check if appium starts
    def appium_check(self) -> None:
        socket_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            logger.info('Start checking to see if the service is started, Please Wait...')
            socket_socket.connect((self.host_appium, self.port))
        except OSError as e:
            logger.warning(e)
            logger.info('appium service is not started , start now, Please Wait...')
            self.prepare_appium()

    # Check to see if the device is bound
    def connect_check(self) -> None or object:
        connect_devices_name = self.devices_name()
        if connect_devices_name:
            logger.info('The device has been bound. Please continue')
        else:
            logger.info('Begin binding the device, Please wait...')
            driver = self.connect_equipment()
            return driver

    # start appium
    def prepare_appium(self) -> None:
        device_id = ''
        try:
            device_id = self.devices_udid()[0]
        except IndexError as e:
            logger.warning('The program did not detect that the device is connected to USB, Please check that the USB is connected correctly.')
            logger.error(e)
        cmd = r'start "' + str(device_id) + '" appium -p ' + str(
            self.port) + ' -bp ' + str(self.port + 1) + ' -U ' + str(
            device_id) + ' --session-override -a 127.0.0.1 --command-timeout 1000'
        try:
            subprocess.Popen(cmd, shell=True)
        except OSError as e:
            logger.error(e)

    def disconnect_equipment(self) -> None:
        port_list_cmd = r'netstat -ano | findstr "' + str(self.host_appium) + '"  '
        port_list = subprocess.Popen(port_list_cmd, shell=True)
        kill_port = port_list[4]
        kill_port_cmd = r'taskkill -PID "' + str(kill_port) + '"  '
        subprocess.Popen(kill_port_cmd, shell=True)

    # connect equipment
    def connect_equipment(self) -> object:
        udid = self.devices_udid()
        devices_name = self.devices_name()
        prepare_dict = dict(
            udid=udid[0],
            deviceName=devices_name[0],
            app_Activity=self.app_Activity,
            app_Package=self.app_Package,
            newCommandTimeout=self.newCommandTimeout,
            platformName=self.platformName,
            platformVersion=self.platformVersion
        )
        try:
            driver = webdriver.Remote(
                "http://{host_appium}:{port}/wd/hub".format(host_appium=self.host_appium, port=self.port),
                prepare_dict)
            if driver:
                logger.success("port %s open success" % str(self.host_appium))
                return driver, udid
        except MaxRetryError as e:
            logger.warning(e)

    # gets the device test port
    def get_device_port(self):
        pass

    # get device name
    def get_device_name(self):
        pass

    # skip the wizard page
    @classmethod
    def skip_the_wizard_page(cls):
        pass

    # start app
    def start_the_app(self):
        pass

    def __str__(self):
        return self.app_name


# class PhotoFramePhoto(App):
#     """
#         jointframe photo app
#     """
#     app_name = "settings"
#     app_Activity = ''


class AppStore(metaclass=ABCMeta):
    """

    AppStore are really abstract base classes
    Usage:
        app_type:           jointframe app name
        def create_app():   Must be written
        def order_app():    Must be written

    """

    @abstractmethod
    def create_app(self, app_type):
        """
        Every method that requires a subclass implementation throws a NotImplementeError
        :param app_type:
        :return: raise NotImplementedError()
        """
        raise NotImplementedError()

    def order_app(self, app_type):
        """
         Now pass in the app type to order_app()
         Usage:
            app.usb_check(): Check your USB connection
            app.appium_check(): Check if the appIum service is started, and if not, start the appIum service
            app.appium_check(): If there is no connection, try to connect, and if there is, return the driver
        """
        app = self.create_app(app_type)
        app.appium_check()
        # driver = app.connect_check()
        driver = app.connect_equipment()
        order_app_dict = {
            "driver": driver[0],
            "udid": driver[1],
            "app": app,
        }
        return order_app_dict




