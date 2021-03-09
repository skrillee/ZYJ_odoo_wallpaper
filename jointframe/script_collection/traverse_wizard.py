#! -*- coding: utf-8 -*-
__author__ = 'Yan.zhe 2021.2.1'

# from script_collection.import_share import *
from start_the_service.app_instance import *
import typing


class JointFrameWizardFrameStore(AppStore):
    """
        The frame test, app_type:
            photo、music、video、alarm、weather、calender、setting、wizard
    """

    def create_app(self, app_type) -> APPWizard:
        app: typing.Optional[APPWizard] = None

        # Start the Photo module's app
        if app_type == 'traverse the wizard':
            app = APPWizard()

        return app


class TraverseWizard(object):

    def __init__(self):
        # Instantiate app
        app_store = JointFrameWizardFrameStore()
        order_app_dict = app_store.order_app('traverse the wizard')
        # get frame driver
        self.frame_driver = order_app_dict['driver']
        self.app = order_app_dict['app']

    def traverse_the_wizard_page(self):
        self.app.traverse_the_wizard(self.frame_driver)


if __name__ == '__main__':
    logger.info("The wizard app traversal begins")
    TraverseWizard().traverse_the_wizard_page()
    logger.info("The wizard app traversal ends")

