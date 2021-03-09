#! -*- coding: utf-8 -*-
__author__ = 'Yan.zhe 2021.2.18'

# from script_collection.import_share import *
from start_the_service.app_instance import *
from script_collection.setting import *
import typing


class JointFrameGalleryStore(AppStore):
    """
        The frame test, app_type:
            photo、music、video、alarm、weather、calender、setting、wizard
    """

    def create_app(self, app_type) -> APPGallery:
        app: typing.Optional[APPGallery] = None

        # Start the Photo module's app
        if app_type == 'Gallery':
            app = APPGallery()

        return app


class Gallery(object):

    def __init__(self):
        # Instantiate app
        app_store = JointFrameGalleryStore()
        order_app_dict = app_store.order_app('Gallery')
        # get frame driver
        self.frame_driver = order_app_dict['driver']
        self.app = order_app_dict['app']
        self.udid = order_app_dict['udid'][0]

    def friends_photos(self, frame_id):
        self.app.bind_and_send_images(self.frame_driver, frame_id)


if __name__ == '__main__':
    logger.info("Start gallery time")
    setting = Setting()
    setting.setting_connect_wifi()
    photo_frame_id = []
    try:
        photo_frame_id = setting.setting_get_frame_id()[0]
    except IndexError as error:
        logger.warning("Unable to obtain frame id, has waited more than 20 seconds, please check network")
    Gallery().friends_photos(photo_frame_id)
    logger.info("End gallery time")

