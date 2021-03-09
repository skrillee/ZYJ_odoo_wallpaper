#! -*- coding: utf-8 -*-
__author__ = 'Yan.zhe 2021.2.8'

# from script_collection.import_share import *
from start_the_service.app_instance import *
import typing


class JointFrameSettingStore(AppStore):
    """
        The frame test, app_type:
            photo、music、video、alarm、weather、calender、setting、wizard
    """

    def create_app(self, app_type) -> APPSetting:
        app: typing.Optional[APPSetting] = None

        # Start the Photo module's app
        if app_type == 'Setting':
            app = APPSetting()

        return app


class SettingWifi(object):

    def __init__(self):
        # Instantiate app
        app_store = JointFrameSettingStore()
        order_app_dict = app_store.order_app('Setting')
        # get frame driver
        self.frame_driver = order_app_dict['driver']
        self.app = order_app_dict['app']
        self.udid = order_app_dict['udid'][0]

    def setting_wifi_page(self):
        self.app.check_hidden_wifi(self.frame_driver, self.udid)

    def setting_frame_page(self):
        self.app.app_change_date(self.frame_driver, self.udid, end_date='2020-02-18')


if __name__ == '__main__':
    logger.info("Start setting")
    setting = SettingWifi()

    setting.setting_wifi_page()
    logger.info("End setting")

