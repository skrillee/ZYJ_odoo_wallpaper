#! -*- coding: utf-8 -*-
__author__ = 'Yan.zhe 2021.2.8'

# from script_collection.import_share import *
from start_the_service.app_instance import *
import typing


class JointFrameClockSettingStore(AppStore):
    """
        The frame test, app_type:
            photo、music、video、alarm、weather、calender、setting、wizard
    """

    def create_app(self, app_type) -> APPClock:
        app: typing.Optional[APPClock] = None

        # Start the Photo module's app
        if app_type == 'clock setting':
            app = APPClock()

        return app


class ClockSetting(object):

    def __init__(self):
        # Instantiate app
        app_store = JointFrameClockSettingStore()
        order_app_dict = app_store.order_app('Clock Setting')
        # get frame driver
        self.frame_driver = order_app_dict['driver']
        self.app = order_app_dict['app']

    def clock_setting_page(self):
        self.app.clock_setting(self.frame_driver)


if __name__ == '__main__':
    logger.info("Start setting time")
    ClockSetting().clock_setting_page()
    logger.info("End setting time")

