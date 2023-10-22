import logging
import math
import asyncio
from epic7_bot.utils.runInParallel import runInParallel
from epic7_bot.core.DeviceManager import DeviceManager
from epic7_bot.core.MathUtils import MathUtils
from epic7_bot.modules.Module import Module
from epic7_bot.templates.SecretShopTemplates import SecretShopTemplates
from epic7_bot.utils.fix_screen_size import ScreenSizeFixedFixer


class SecretShop(Module):
    def __init__(self, fastMode):
        super(self.__class__, self).__init__(fastMode)
        self.DeviceManager = DeviceManager()
        self.SecretShopTemplates = SecretShopTemplates()
        self.MathUtils = MathUtils()
        self.ScreenSizeFixer = ScreenSizeFixedFixer(1600, 900, 53, 30, 1546, 869)

        self.mystic_count = 0
        self.refreshes_count = 0
        self.covenant_count = 0

    def check_bookmarks(self, mask=None):
        logging.info("Check Mystic and Covenant Bookmarks")

        [mystic_pos, coven_pos] = runInParallel(
            lambda: self.ScreenManager.match_template_on_screen(
                self.SecretShopTemplates.mystic, mask=mask, log=True),
            lambda: self.ScreenManager.match_template_on_screen(
                self.SecretShopTemplates.covenant, mask=mask, log=True))

        if mystic_pos is not None:
            logging.info("Found Mystic Bookmark")
            x, y = self.ScreenManager.get_position_of_template_match(
                mystic_pos)

            width, height = self.SecretShopTemplates.mystic["image"].shape[::-1]

            x1 = x + math.floor(width / 2) + 580
            y1 = y + math.floor(height / 2) + 10
            x2 = x + math.floor(width / 2) + 800
            y2 = y + math.floor(height / 2) + 55

            self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
                x1=x1, y1=y1, x2=x2, y2=y2, action="Click on Buy")

            self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
                x1=761, y1=605, x2=1059, y2=660, action="Click on Confirm Buy")

            self.mystic_count += 1
            
            

        if coven_pos is not None:
            logging.info("Found Covenant Bookmark")
            x, y = self.ScreenManager.get_position_of_template_match(coven_pos)

            width, height = self.SecretShopTemplates.covenant["image"].shape[::-1]

            x1 = x + math.floor(width / 2) + 580
            y1 = y + math.floor(height / 2) + 10
            x2 = x + math.floor(width / 2) + 800
            y2 = y + math.floor(height / 2) + 55

            self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
                x1=x1, y1=y1, x2=x2, y2=y2, action="Click on Buy")

            self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
                x1=761, y1=605, x2=1059, y2=660, action="Click on Confirm Buy")

            self.covenant_count += 1
            
        

    def scroll(self):
        x1, y1 = self.ScreenSizeFixer.norm(
            *self.MathUtils.random_point_in_area(
                x1=750, y1=781, x2=1282, y2=845
            )
        )
        x2, y2 = self.ScreenSizeFixer.norm(
            *self.MathUtils.random_point_in_area(
                x1=701, y1=98, x2=1288, y2=174
            )
        )

        self.DeviceManager.device.shell(
            f"input touchscreen swipe {x1} {y1} {x2} {y2} 400")

    def check_store(self):
        self.check_bookmarks()
        self.scroll()
        self.ScreenManager.sleep(1)
        self.check_bookmarks(mask=self.SecretShopTemplates.mask4_6["image"])

    def refresh(self):
        self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
            x1=287, y1=808, x2=387, y2=838, action="Click on Refresh Button", premptive=False)
        self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
            x1=878, y1=537, x2=986, y2=568, action="Click on Confirm Button", premptive=False)

        self.refreshes_count += 1

    def show_stats(self):
        comment = f"\nTotal Covenant: {str(self.covenant_count)}{' '*30}" + \
            f"\nTotal Mystic: {str(self.mystic_count)}{' '*30}" + \
            f"\nTotal Refreshes: {str(self.refreshes_count)}{' '*30}\n\n\n"
        previus_line = "\033[F"
        if self.refreshes_count == 1:
            print(f"\r{previus_line*2}{comment}")
        else:
            print(f"\r{previus_line*7}{comment}")
        pass

    def start_auto_buy_secret_shop(self):
        while True:
            self.check_store()
            self.refresh()
            self.show_stats()

    def start_auto_buy_secret_shop_from_lobby(self):
        self.ScreenManager.ensure_not_on_sleep_mode_on_lobby()

        self.ScreenManager.random_click_on_area_and_check_change_on_screen_retry(
            x1=683, y1=204, x2=728, y2=246, action="Click on Bartender")
        self.start_auto_buy_secret_shop()
