from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

# Hide Window Title Bar
from PyQt5 import QtCore

# Setup Help Text
import mill_touch_v4.helptext as helptext

# Setup Button Handler
import mill_touch_v4.button_handler as btnHandler

# Smart G code thingy
import linuxcnc


class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)
        self.emcCommand = linuxcnc.command()

        # Hide Window Title Bar
        self.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint)
            # | QtCore.Qt.WindowStaysOnTopHint

        self.drillKeyPad.buttonClicked.connect(self.drillOpHandleKeys)
        self.controlBtnGrp.buttonClicked.connect(self.controlChangePage)
        self.droBtnGrp.buttonClicked.connect(self.droChangePage)
        self.mainBtnGrp.buttonClicked.connect(self.mainChangePage)
        self.mdiBackspace.clicked.connect(self.mdiHandleBackSpace)
        self.mdiBtnGrp.buttonClicked.connect(self.mdiHandleKeys)
        self.mdiHelpBtn.clicked.connect(self.mdiHelpPage)
        self.mdiEntryBtn.clicked.connect(self.mdiEntryPage)
        self.mdiLoad.clicked.connect(self.mdiSetLabels)
        self.smartGcodeBtnGrp.buttonClicked.connect(self.smartChangePage)
        self.loadGcode.clicked.connect(self.loadSmartGcode)


    def drillOpHandleKeys(self, button):
        btnHandler.drillOpHandleKeys(self, button)

    def mainChangePage(self, button):
        self.mainStack.setCurrentIndex(button.property('page'))

    def controlChangePage(self, button):
        self.controlStack.setCurrentIndex(button.property('page'))

    def droChangePage(self, button):
        self.droStack.setCurrentIndex(button.property('page'))

    def smartChangePage(self, button):
        self.smartStack.setCurrentIndex(button.property('page'))

    def mdiHelpPage(self, button):
        self.mdiStack.setCurrentIndex(1)

    def mdiEntryPage(self, button):
        self.mdiStack.setCurrentIndex(0)

    def mdiHandleKeys(self, button):
        char = str(button.text())
        text = self.mdiEntry.text() or '0'
        if text != '0':
            text += char
        else:
            text = char
        self.mdiEntry.setText(text)

    def mdiSetLabels(self):
        # get smart and figure out what axes are used

        text = self.mdiEntry.text() or '0'
        if text != '0':
            words = helptext.gcode_words()
            if text in words:
                self.mdiClear()
                for index, value in enumerate(words[text], start=1):
                    getattr(self, 'gcodeParameter_' + str(index)).setText(value)
            else:
                self.mdiClear()
            titles = helptext.gcode_titles()
            if text in titles:
                self.gcodeDescription.setText(titles[text])
            else:
                self.mdiClear()
            self.gcodeHelpLabel.setText(helptext.gcode_descriptions(text))
        else:
            self.mdiClear()

    def mdiClear(self):
        for index in range(1,8):
            getattr(self, 'gcodeParameter_' + str(index)).setText('')
        self.gcodeDescription.setText('')
        self.gcodeHelpLabel.setText('')

    def mdiHandleBackSpace(self):
        if len(self.mdiEntry.text()) > 0:
            text = self.mdiEntry.text()[:-1]
            self.mdiEntry.setText(text)



    def loadSmartGcode(self):
        self.emcCommand.program_open('/tmp/qtpyvcp.ngc')

    def on_exitBtn_clicked(self):
        self.app.quit()

