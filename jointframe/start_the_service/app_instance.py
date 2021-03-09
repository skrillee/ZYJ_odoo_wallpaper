#! -*- coding: utf-8 -*-
__author__ = 'Yan.zhe 2021.2.1'

from start_the_service.motion_events import *
from start_the_service.start_the_service import *
import re


class APPWizard(App):
    """
        jointframe Wizard app,
        Usage:
            def skip_the_wizard_page():    Must be written, Otherwise you'll miss it
    """
    # app connection information
    app_name = "wizard"
    app_Activity = 'com.shenju.frame.wizard'
    app_Package = 'com.shenju.frame.wizard.ui.LanguageActivity'
    appWaitPackage = 'com.shenju.frame.wizard.ui.LanguageActivity'
    platformName = "Android"
    platformVersion = '9'
    resetKeyboard = "true"
    systemPort = 8200
    newCommandTimeout = 1000

    # select language page
    wizard_select_language_next = 'com.shenju.frame.wizard:id/btn_next'

    # install the application page
    wizard_install_the_application_next = 'com.shenju.frame.wizard:id/btn_next'

    # waiting for the internet page
    wizard_waiting_for_the_internet_next = 'com.shenju.frame.wizard:id/btn_next'
    wizard_wifi_list = 'com.shenju.frame.wizard:id/fragment_wifi'
    wizard_wifi_slip_start = 'android.widget.LinearLayout'
    wizard_add_network = 'Add network'
    wizard_wifi_name = 'Shenju300'
    wizard_wifi_password = 'shenju+300'
    wizard_password_field = 'com.shenju.frame.wizard:id/edit_password'
    wizard_password_field_connect = 'com.shenju.frame.wizard:id/btn_connect'

    # Welcome page
    wizard_end_button = 'com.shenju.frame.wizard:id/btn_finish'

    def traverse_the_wizard(self, driver):
        # instantiate method classes
        motion_events = MotionEvents(driver)
        # traverse language page
        motion_events.find_element_id(page_id=self.wizard_select_language_next).click()
        # Slide to the end of the page
        swipe_down_until_find_result = motion_events.swipe_down_until_find()
        swipe_down_until_find_result(text=self.wizard_wifi_name)
        # Find WiFi and click
        motion_events.find_element_text(text=self.wizard_wifi_name).click()
        # enter password
        motion_events.find_element_id(page_id=self.wizard_password_field).send_keys(self.wizard_wifi_password)
        motion_events.find_element_id(page_id=self.wizard_password_field_connect).click()
        # motion_events.find_element_id(page_id=self.wizard_select_language_next).click()
        # end wizard page
        motion_events.find_element_id(page_id=self.wizard_end_button).click()

    def skip_the_wizard_page(self):
        pass


"""
     def __init__(self, driver):
         instantiate method classes
         self.motion_events = MotionEvents(driver)
"""


class APPClock(App):
    """
        jointframe Wizard app,
        Usage:
            def skip_the_clock_page():
    """
    # app connection information
    app_name = "clock"
    app_Activity = 'com.shenju.frame.alarm'
    app_Package = 'com.shenju.frame.wizard.ui.LanguageActivity'
    appWaitPackage = 'com.shenju.frame.wizard.ui.LanguageActivity'
    platformName = "Android"
    platformVersion = '9'
    resetKeyboard = "true"
    systemPort = 8200
    newCommandTimeout = 1000

    # select language page
    wizard_select_language_next = 'com.shenju.frame.wizard:id/btn_next'

    # install the application page
    wizard_install_the_application_next = 'com.shenju.frame.wizard:id/btn_next'

    # waiting for the internet page
    wizard_waiting_for_the_internet_next = 'com.shenju.frame.wizard:id/btn_next'
    wizard_wifi_list = 'com.shenju.frame.wizard:id/fragment_wifi'
    wizard_wifi_slip_start = 'android.widget.LinearLayout'
    wizard_add_network = 'Add network'
    wizard_wifi_name = 'Shenju300'
    wizard_wifi_password = 'shenju+300'
    wizard_password_field = 'com.shenju.frame.wizard:id/edit_password'
    wizard_password_field_connect = 'com.shenju.frame.wizard:id/btn_connect'

    # Welcome page
    wizard_end_button = 'com.shenju.frame.wizard:id/btn_finish'


class APPSetting(App):
    """
        jointframe Wizard app,
        Usage:
            def skip_the_clock_page():
    """
    # app connection information
    app_name = "clock"
    app_Activity = 'com.shenju.frame.settings.MainActivity'
    app_Package = 'com.shenju.frame.settings'
    appWaitPackage = 'com.shenju.frame.settings'
    platformName = "Android"
    platformVersion = '9'
    resetKeyboard = "true"
    systemPort = 8200
    newCommandTimeout = 1000

    # setting page
    setting_device_sync = 'Device Sync'
    setting_wifi_page_text = 'WiFi'
    setting_frame_page_text = 'Frame'

    # setting-wifi page
    setting_wifi_name = 'Shenju300'
    setting_wifi_password = 'shenju+300'
    setting_wifi_forget = 'com.shenju.frame.settings:id/btn_forget'
    setting_wifi_add_network = 'Add network'
    setting_wifi_add_network_name = 'com.shenju.frame.settings:id/edit_ssid'
    setting_wifi_add_network_security = 'com.shenju.frame.settings:id/tv_security'
    setting_wifi_add_network_security_wpa_wpa2 = 'WPA/WPA2 PSK'
    setting_wifi_add_network_security_password = 'com.shenju.frame.settings:id/edit_password'
    setting_wifi_add_network_security_connect = 'com.shenju.frame.settings:id/btn_connect'
    setting_wifi_add_network_security_back = 'com.shenju.frame.settings:id/btn_close'
    # setting-wifi page
    setting_frame_language = 'com.shenju.frame.settings:id/frame_layout_language'
    setting_frame_auto_screen = 'com.shenju.frame.settings:id/frame_layout_onoff'
    setting_frame_sound = 'com.shenju.frame.settings:id/frame_layout_sound'
    setting_frame_display = 'com.shenju.frame.settings:id/frame_layout_display'
    setting_frame_date_time = 'com.shenju.frame.settings:id/frame_layout_datetime'
    setting_frame_data_time_auto_date_time = 'com.shenju.frame.settings:id/datetime_auto'
    setting_frame_date_time_date = 'com.shenju.frame.settings:id/datetime_date'
    setting_frame_date_time_next = 'android:id/next'
    setting_frame_date_time_year = 'android:id/date_picker_header_year'
    setting_frame_date_time_previous = 'android:id/prev'
    setting_frame_data_time_date_ok = 'android:id/button1'
    # setting devices sync page
    setting_device_sync_frame_id = 'com.shenju.frame.settings:id/devicesync_frameid'

    def check_hidden_wifi(self, driver, udid):
        # instantiate method classes
        motion_events = MotionEvents(driver)
        # start app
        motion_events.launch_app(udid=udid, app_package=self.app_Package, app_activity=self.app_Activity)
        # Jump to the WiFi page
        motion_events.find_element_text(text=self.setting_wifi_page_text).click()
        swipe_down_until_find_result = motion_events.swipe_down_until_find()
        swipe_down_until_find_result(text=self.setting_wifi_add_network)
        motion_events.find_element_text(text=self.setting_wifi_add_network).click()
        motion_events.find_element_id(page_id=self.setting_wifi_add_network_name).send_keys(self.setting_wifi_name)
        motion_events.find_element_id(page_id=self.setting_wifi_add_network_security).click()
        motion_events.find_element_text(text=self.setting_wifi_add_network_security_wpa_wpa2).click()
        motion_events.find_element_id(page_id=self.setting_wifi_add_network_security_password).send_keys(self.setting_wifi_password)
        motion_events.find_element_id(page_id=self.setting_wifi_add_network_security_connect).click()
        swipe_up_until_find_result = motion_events.swipe_up_until_find()
        swipe_up_until_find_result(text=self.setting_wifi_name)
        motion_events.find_element_text(text=self.setting_wifi_name).click()
        motion_events.find_element_id(page_id=self.setting_wifi_forget).click()

    def app_change_date(self, driver, udid, end_date=None):
        # instantiate method classes
        motion_events = MotionEvents(driver)
        # start app
        motion_events.launch_app(udid=udid, app_package=self.app_Package, app_activity=self.app_Activity)
        motion_events.find_element_text(text=self.setting_frame_page_text).click()
        motion_events.find_element_id(page_id=self.setting_frame_date_time).click()
        auto_date = motion_events.find_element_id(page_id=self.setting_frame_data_time_auto_date_time).get_attribute("checked")
        if auto_date is True:
            motion_events.find_element_id(page_id=self.setting_frame_data_time_auto_date_time).click()
        else:
            start_date = motion_events.find_element_id(page_id=self.setting_frame_date_time_date).text
            motion_events.find_element_id(page_id=self.setting_frame_date_time_date).click()
            previous_time = motion_events.difference_value_month(start_date, end_date)
            time = 0
            while time != previous_time:
                motion_events.find_element_id(page_id=self.setting_frame_date_time_previous).click()
                time += 1
            motion_events.find_element_text(text=end_date.split('-')[2]).click()
            motion_events.find_element_id(page_id=self.setting_frame_data_time_date_ok).click()

    def get_frame_id(self, driver, udid):
        # instantiate method classes
        motion_events = MotionEvents(driver)
        # start app
        motion_events.launch_app(udid=udid, app_package=self.app_Package, app_activity=self.app_Activity)
        motion_events.find_element_text(text=self.setting_device_sync).click()
        driver.implicitly_wait(20)
        frame_id_string_blank = motion_events.find_element_id(page_id=self.setting_device_sync_frame_id).text
        frame_id_string = ''.join(frame_id_string_blank.split())
        frame_id = re.findall(r"\d+\.?\d*", frame_id_string)
        if frame_id:
            return frame_id
        else:
            return None

    def connect_wifi(self, driver, udid):
        # instantiate method classes
        motion_events = MotionEvents(driver)
        # start app
        motion_events.launch_app(udid=udid, app_package=self.app_Package, app_activity=self.app_Activity)
        # Jump to the WiFi page
        motion_events.find_element_text(text=self.setting_wifi_page_text).click()
        swipe_down_until_find_result = motion_events.swipe_down_until_find()
        swipe_down_until_find_result(text=self.setting_wifi_add_network)
        motion_events.find_element_text(text=self.setting_wifi_add_network).click()
        motion_events.find_element_id(page_id=self.setting_wifi_add_network_name).send_keys(self.setting_wifi_name)
        motion_events.find_element_id(page_id=self.setting_wifi_add_network_security).click()
        motion_events.find_element_text(text=self.setting_wifi_add_network_security_wpa_wpa2).click()
        motion_events.find_element_id(page_id=self.setting_wifi_add_network_security_password).send_keys(self.setting_wifi_password)
        motion_events.find_element_id(page_id=self.setting_wifi_add_network_security_connect).click()


class APPGallery(App):
    """
        jointframe Album app,
    """
    # app connection information
    app_name = "album"
    app_Activity = 'com.shenju.frame.gallery.ui.GalleryListActivity'
    app_Package = 'com.shenju.frame.gallery'
    appWaitPackage = 'com.shenju.frame.gallery'
    platformName = "Android"
    platformVersion = '9'
    resetKeyboard = "true"
    systemPort = 8200
    newCommandTimeout = 1000

    gallery_back = "com.shenju.frame.gallery:id/btn_back"

    # setting-wifi page
    gallery_all = 'All'
    gallery_friends = 'Friends'
    gallery_favorites = "Favorites"
    gallery_private = "Private"

    def check_photo_exist(self, driver, udid):
        pass

    @staticmethod
    def bind_and_send_images(driver, frame_id):
        motion_events = MotionEvents(driver)
        return_token = motion_events.binding_frame(frame_id)
        motion_events.send_images(return_token)


class APPJointFrame(App):
    """
        jointframe  app,
    """
    app_name = "Joint Frame"
    app_Activity = 'com.shenju.frame.ui.SplashActivity'
    app_Package = 'com.shenju.frame.dev'
    appWaitPackage = 'com.shenju.frame.dev'
    platformName = "Android"
    platformVersion = '10'
    resetKeyboard = "true"
    systemPort = 8200
    newCommandTimeout = 1000

    # login page
    joint_frame_login_logo = 'android.widget.TextView'
    joint_frame_login_email = 'com.shenju.frame.dev:id/et_user_name'
    joint_frame_login_password = 'com.shenju.frame.dev:id/et_psw'
    joint_frame_login_login = 'com.shenju.frame.dev:id/btn_login'
    joint_frame_login_create_account = 'com.shenju.frame.dev:id/tv_register'
    joint_frame_login_forgot_password = 'com.shenju.frame.dev:id/tv_find_psw'
    joint_frame_login_version = 'com.shenju.frame.dev:id/tv_version'

    joint_frame_login_email_content = '1979736774@qq.com'
    joint_frame_login_password_content = 'yanzhe1994'
    
    def joint_frame_login(self, driver, udid):
        # instantiate method classes
        motion_events = MotionEvents(driver)
        # start app
        motion_events.launch_app(udid=udid, app_package=self.app_Package, app_activity=self.app_Activity)
        existing_email = motion_events.find_element_id(page_id=self.joint_frame_login_email).text
        motion_events.clean_text(existing_email)
        motion_events.find_element_id(page_id=self.joint_frame_login_email).send_keys(self.joint_frame_login_email_content)
        motion_events.find_element_id(page_id=self.joint_frame_login_password).send_keys(self.joint_frame_login_password_content)
        motion_events.find_element_id(page_id=self.joint_frame_login_login).click()
