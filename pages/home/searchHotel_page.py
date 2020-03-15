from base.selenium_driver import SeleniumDriver
from time import sleep
class searchHotel_page(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

     # Locator
    _location_sel = "location"  #By.NAME
    _hotels_sel = "hotels" #By.NAME
    _roomType_sel = "room_type" #By.NAME
    _numRooms_sel = "room_nos" #By.NAME
    _checkInDate_field = "datepick_in" #By.NAME
    _checkOutDate_field = "datepick_out" #By.NAME
    _adultPerRoom_sel = "adult_room" #By.NAME
    _childPerRoom_sel = "child_room" #By.NAME
    _search_btn = "Submit" #By.NAME
    _reset_btn = "Reset" #By.NAME
    _userNameShow_txt = "username_show" #By.NAME
    _checkInSpan_msg = "checkin_span" #By.ID

    #Action
    def verifyLoginSuccessful(self):
        self.waitForElement(locator=self._location_sel, locatorType="name", timeout=20)
        result = self.isElementPresent(locator=self._location_sel, locatorType="name")
        return result

    def selectLocation(self, location):
        self.selectByText(locator=self._location_sel, locatorType="name", visibletext=location)

    def selectHotel(self, hotel):
        self.selectByText(locator=self._hotels_sel,locatorType="name", visibletext=hotel)

    def selectRoomtype(self, roomtype):
        self.selectByText(locator=self._roomType_sel, locatorType="name", visibletext=roomtype)

    def selectNoOfRoom(self, noroom):
        self.selectByText(locator=self._numRooms_sel, locatorType="name", visibletext=noroom)

    def enterCheckInDate(self, checkindate):
        self.clearField(locator=self._checkInDate_field, locatorType="name")
        self.sendKeys(checkindate, locator=self._checkInDate_field, locatorType="name")

    def enterCheckOutDate(self,checkoutdate):
        self.clearField(locator=self._checkOutDate_field, locatorType="name")
        self.sendKeys(checkoutdate, locator=self._checkOutDate_field, locatorType="name")

    def selectAdultsPerRoom(self, adultNum):
        self.selectByText(locator=self._adultPerRoom_sel, locatorType="name", visibletext=adultNum)

    def selectChildrenPerRoom(self, childNum):
        self.selectByText(locator=self._childPerRoom_sel, locatorType="name", visibletext=childNum)

    def clickSearchButton(self):
        self.elementClick(locator=self._search_btn, locatorType="name")

    def clickResetButton(self):
        self.elementClick(locator=self._reset_btn, locatorType="name")

    def verifyCheckInDateFailed(self):
        result = self.isElementPresent(self._checkInSpan_msg, locatorType= "id")
        return result
        
    def inputSearchPageData(self, location, hotel, roomtype, roomNum, checkin, checkout, adultRoom, childRoom):
        self.selectLocation(location)
        self.log.info("Selected Location - " + location)
        sleep(1)
        self.selectHotel(hotel)
        self.log.info("Selected Hotel - " + hotel)
        sleep(1)
        self.selectRoomtype(roomtype)
        self.log.info("Selected Room Type - " + roomtype)
        sleep(1)
        self.selectNoOfRoom(roomNum)
        self.log.info("Selected Room Number - " + roomNum)
        sleep(1)
        self.enterCheckInDate(checkin)
        self.log.info("Typed Check In date - " + checkin)
        sleep(1)
        self.enterCheckOutDate(checkout)
        self.log.info("Typed Check Out date - " + checkout)
        sleep(1)
        self.selectAdultsPerRoom(adultRoom)
        self.log.info("Selected Adults Per Room - " + adultRoom)
        sleep(1)
        self.selectChildrenPerRoom(childRoom)
        self.log.info("Selected Children Per Room - " + childRoom)
