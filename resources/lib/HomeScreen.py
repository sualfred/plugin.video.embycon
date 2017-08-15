import xbmc
import xbmcaddon
import xbmcgui

from simple_logging import SimpleLogging

log = SimpleLogging(__name__)

class HomeScreen(xbmcgui.WindowXML):

    def __init__(self, *args, **kwargs):
        log.error("HomeScreen: __init__")
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        log.error("HomeScreen: onInit")
        self.action_exitkeys_id = [10, 13]

        self.listControl = self.getControl(3000)
        self.listControl.addItems(self.getListItems())
        self.setFocus(self.listControl)

    def onFocus(self, controlId):
        pass

    def doAction(self, actionID):
        pass

    def onClick(self, controlID):
        log.error("HomeScreen: Control ID:" + str(controlID))
        if (controlID == 3000):
            log.error("HomeScreen: List was clicked")
            library_id = self.listControl.getSelectedItem().getProperty("library_id")
            log.error("HomeScreen: Selected Library ID:" + str(library_id))


    def getListItems(self):
        listItems = []

        li = xbmcgui.ListItem("List Item 01")
        li.setProperty('menu_id', 'menu_01')

        listItems.append(li)

        li2 = xbmcgui.ListItem("List Item 02")
        li2.setProperty('menu_id', 'menu_02')
        listItems.append(li2)

        return listItems
