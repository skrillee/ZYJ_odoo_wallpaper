#! -*- coding: utf-8 -*-
__author__ = 'Yan.zhe 2021.2.18'

# from script_collection.import_share import *
from start_the_service.app_instance import *
from script_collection.setting import *
import typing


class APPJointFrameStore(AppStore):
    """
        The frame test, app_type:
            photo、music、video、alarm、weather、calender、setting、wizard
    """

    def create_app(self, app_type) -> APPJointFrame:
        app: typing.Optional[APPJointFrame] = None

        # Start the Photo module's app
        if app_type == 'JointFrame':
            app = APPJointFrame()

        return app


class JointFrame(object):

    def __init__(self):
        # Instantiate app
        app_store = APPJointFrameStore()
        order_app_dict = app_store.order_app('JointFrame')
        # get frame driver
        self.frame_driver = order_app_dict['driver']
        self.app = order_app_dict['app']
        self.udid = order_app_dict['udid'][0]

    def joint_frame_login_page(self):
        self.app.joint_frame_login(self.frame_driver, self.udid)


if __name__ == '__main__':
    logger.info("Start JointFrame")
    joint_frame = JointFrame()
    joint_frame.joint_frame_login_page()
    logger.info("End setting")
