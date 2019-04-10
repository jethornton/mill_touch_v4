from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

# Hide Window Title Bar
from PyQt5 import QtCore

# Setup Button Handler
import mill_touch_v4.button_handler as btnHandler

# Setup the G code Generator
import mill_touch_v4.gcode_gen as gcodeGen

# Setup the Threads Database
import mill_touch_v4.threads as threadData


import linuxcnc

import mill_touch_v4.resources.resources_rc

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        # Hide Window Title Bar
        self.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint)
            # | QtCore.Qt.WindowStaysOnTopHint

        btnHandler.loadGcodeList(self)

        self.holeKeyPad.buttonClicked.connect(self.holeOpsHandleKeys)
        self.drillBackspace.clicked.connect(self.drillHandleBackspace)
        self.coordListAddBtn.clicked.connect(self.coordListAppend)
        self.coordListBkspBtn.clicked.connect(self.coordHandleBackspace)
        self.coordListMoveUpBtn.clicked.connect(self.coordHandleMoveUp)
        self.coordListMoveDownBtn.clicked.connect(self.coordHandleMoveDown)
        self.coordListClearBtn.clicked.connect(self.coordHandleClear)
        self.coordListRemoveBtn.clicked.connect(self.coordHandleRemoveLine)
        self.gcodeListPageUpBtn.clicked.connect(self.gcodeHandleMoveUp)
        self.gcodeListPageDownBtn.clicked.connect(self.gcodeHandleMoveDown)
        self.preambleAddBtn.clicked.connect(self.preambleAdd)
        self.holeOpAppendBtn.clicked.connect(self.holeOpAppend)
        self.mdiAppendBtn.clicked.connect(self.mdiAppend)
        self.gcodeLoadBtn.clicked.connect(self.gcodeLoad)
        self.gcodeSaveBtn.clicked.connect(self.gcodeSave)
        self.clearGcodeBtn.clicked.connect(self.clearGcode)
        self.controlBtnGrp.buttonClicked.connect(self.controlChangePage)
        self.droBtnGrp.buttonClicked.connect(self.droChangePage)
        self.mainBtnGrp.buttonClicked.connect(self.mainChangePage)
        self.mdiBackspace.clicked.connect(self.mdiHandleBackSpace)
        self.mdiBtnGrp.buttonClicked.connect(self.mdiHandleKeys)
        self.mdiNavGroup.buttonClicked.connect(self.mdiChangePage)
        self.mdiLoad.clicked.connect(self.mdiSetLabels)
        self.smartGcodeBtnGrp.buttonClicked.connect(self.smartChangePage)
        self.reloadProgramBtn.clicked.connect(self.reloadProgram)
        self.g5xKeypad.buttonClicked.connect(self.g5xHandleKeys)
        self.g5xBkspBtn.clicked.connect(self.g5xHandleBackSpace)
        self.g92Keypad.buttonClicked.connect(self.g92HandleKeys)
        self.g92BkspBtn.clicked.connect(self.g92HandleBackSpace)

        self.formNextBtn.clicked.connect(self.formNext)
        self.formPreviousBtn.clicked.connect(self.formPrevious)
        self.sizeNextBtn.clicked.connect(self.sizeNext)
        self.sizePreviousBtn.clicked.connect(self.sizePrevious)
        self.classNextBtn.clicked.connect(self.classNext)
        self.classPreviousBtn.clicked.connect(self.classPrevious)
        self.sptmNextBtn.clicked.connect(self.sptmNext)
        self.sptmPreviousBtn.clicked.connect(self.sptmPrevious)

        #self.appendSPTMBtn.clicked.connect(self.appendSPTM)

        if not threadData.open_db(self):
            print('Failed to Open Database')


    def reloadProgram(self):
        gcodeGen.reloadProgram(self)

    def holeOpsHandleKeys(self, button):
        btnHandler.holeOpsHandleKeys(self, button)

    def drillHandleBackspace(self):
        btnHandler.drillOpBackspace(self)

    def coordListAppend(self):
        btnHandler.coordListAddRow(self)

    def coordHandleBackspace(self):
        btnHandler.coordListBackspace(self)

    def coordHandleMoveUp(self):
        btnHandler.coordListMoveUp(self)

    def coordHandleMoveDown(self):
        btnHandler.coordListMoveDown(self)

    def coordHandleClear(self):
        btnHandler.coordListClear(self)

    def coordHandleRemoveLine(self):
        btnHandler.coordListRemoveLine(self)

    def gcodeHandleMoveUp(self):
        btnHandler.gcodeListMoveUp(self)

    def gcodeHandleMoveDown(self):
        btnHandler.gcodeListMoveDown(self)

    def preambleAdd(self):
        gcodeGen.preambleAdd(self)

    def holeOpAppend(self):
        gcodeGen.holeOpAppend(self)

    def mdiAppend(self):
        gcodeGen.mdiAppend(self)

    def gcodeLoad(self):
        gcodeGen.gcodeLoad(self)

    def gcodeSave(self):
        gcodeGen.gcodeSave(self)

    def clearGcode(self):
        gcodeGen.clearGcode(self)

    def g5xHandleKeys(self, button):
        btnHandler.g5xHandleKeys(self, button)

    def g5xHandleBackSpace(self):
        btnHandler.g5xHandleBackSpace(self)

    def g92HandleKeys(self, button):
        btnHandler.g92HandleKeys(self, button)

    def g92HandleBackSpace(self):
        btnHandler.g92HandleBackSpace(self)

    def mdiHandleKeys(self, button):
        btnHandler.mdiHandleKeys(self, button)

    def mdiHandleBackSpace(self):
        btnHandler.mdiHandleBackSpace(self)

    def mdiSetLabels(self):
        btnHandler.mdiSetLabels(self)

    def mdiChangePage(self, button):
        self.mdiStack.setCurrentIndex(button.property('page'))

    def mainChangePage(self, button):
        self.mainStack.setCurrentIndex(button.property('page'))

    def controlChangePage(self, button):
        self.controlStack.setCurrentIndex(button.property('page'))

    def droChangePage(self, button):
        self.droStack.setCurrentIndex(button.property('page'))

    def formNext(self):
        threadData.formNext(self)

    def formPrevious(self):
        threadData.formPrevious(self)

    def sizeNext(self):
        threadData.sizeNext(self)

    def sizePrevious(self):
        threadData.sizePrevious(self)

    def classNext(self):
        threadData.classNext(self)

    def classPrevious(self):
        threadData.classPrevious(self)

    def sptmNext(self):
        threadData.sptmNext(self)

    def sptmPrevious(self):
        threadData.sptmPrevious(self)

    def smartChangePage(self, button):
        #self.pushButton_58.setChecked(True)
        #self.pushButton_113.setAutoExclusive(False)
        #self.pushButton_113.setChecked(False)
        #self.pushButton_113.setAutoExclusive(True)
        #checkedBtn = self.holeOpBtnGrp.checkedButton()
        #checkedBtn.setChecked(False)
        self.smartStack.setCurrentIndex(button.property('page'))
        if button.property('buttonName'):
            getattr(self, button.property('buttonName')).setChecked(True)

    def on_exitBtn_clicked(self):
        self.app.quit()

