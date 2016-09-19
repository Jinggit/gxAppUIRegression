# -*- coding: utf-8 -*-

from appium.webdriver.common.touch_action import TouchAction
from AppiumLibrary import utils
from AppiumLibrary.locators import ElementFinder
from keywordgroup import KeywordGroup

class _TouchKeywords(KeywordGroup):

    def __init__(self):
        self._element_finder = ElementFinder()

    # Public, element lookups
    def zoom(self, locator, percent="200%", steps=1):
        """
        Zooms in on an element a certain amount.
        """
        driver = self._current_application()
        element = self._element_find(locator, True, True)
        driver.zoom(element=element, percent=percent, steps=steps)

    def pinch(self, locator, percent="200%", steps=1):
        """
        Pinch in on an element a certain amount.
        """
        driver = self._current_application()
        element = self._element_find(locator, True, True)
        driver.pinch(element=element, percent=percent, steps=steps)

    def swipe(self, start_x, start_y, end_x, end_y, duration=1000):
        """
        Swipe from one point to another point, for an optional duration.
        """
        driver = self._current_application()
        driver.swipe(start_x, start_y, end_x, end_y, duration)

    def swipe_to_unlock(self):
        """
        Swipe screen to unlock android phone.
        """
        driver = self._current_application()
        driver.swipe(0.1, 0.7, 0.9, 0.7, 2000)

    def scroll(self, start_locator, end_locator):
        """
        Scrolls from one element to another
        Key attributes for arbitrary elements are `id` and `name`. See
        `introduction` for details about locating elements.
        """
        el1 = self._element_find(start_locator, True, True)
        el2 = self._element_find(end_locator, True, True)
        driver = self._current_application()
        driver.scroll(el1, el2)

    def scroll_to(self, locator):
        """
        Scrolls to element of ios
        """
        el = self._element_find(locator, True, True)
        driver = self._current_application()
        driver.execute_script('mobile: scrollTo', {"element": el.id})

    def get_screen_size(self):
        """
        Scrolls to element of android
        """
        driver = self._current_application()
        return driver.get_window_size() 

    def long_press(self, locator):
        """ Long press the element """
        driver = self._current_application()
        element = self._element_find(locator, True, True)
        long_press = TouchAction(driver).long_press(element)
        long_press.perform()        
