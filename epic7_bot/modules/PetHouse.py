from time import sleep
from epic7_bot.modules.Module import Module


class PetHouse(Module):
    def __init__(self):
        super(self.__class__, self).__init__()

    def get_free_pet_summon(self):
        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=894, y1=848, x2=935, y2=879, action="Click on Screen to Ensure not on Sleep Mode")

        self.ScreenManager.click_middle_and_check_change_on_area_retry(
            x1=481, y1=795, x2=582, y2=877, action="Click on Pet House Button")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=1096, y1=795, x2=1197, y2=839, action="Click on First Adopt Button")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=810, y1=747, x2=923, y2=786, action="Click on Second Adopt Button")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=699, y1=841, x2=878, y2=879, action="Click on Tap to Close")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=699, y1=841, x2=878, y2=879, action="Click on Tap to Close Again")

        self.ScreenManager.click_middle_and_check_change_on_screen_retry(
            x1=34, y1=12, x2=225, y2=67, action="Go Back to Lobby")