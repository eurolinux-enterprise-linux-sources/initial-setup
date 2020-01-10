from pyanaconda.ui.gui.hubs import Hub
from pyanaconda.ui.gui.spokes import NormalSpoke as GUI_spoke_class
from initial_setup import product
from initial_setup import common

__all__ = ["InitialSetupMainHub"]


class InitialSetupMainHub(Hub):
    uiFile = "initial_setup.glade"
    builderObjects = ["summaryWindow"]
    mainWidgetName = "summaryWindow"
    translationDomain = "initial-setup"
    helpFile = "InitialSetupHub.xml"

    def __init__(self, *args):
        Hub.__init__(self, *args)

    def _collectCategoriesAndSpokes(self):
        return common.collectCategoriesAndSpokes(self, GUI_spoke_class)

    def _createBox(self):
        Hub._createBox(self)

        # override spokes' distribution strings set by the pyanaconda module
        for spoke in self._spokes.itervalues():
            spoke.window.set_property("distribution",
                                      product.product_title().upper())
