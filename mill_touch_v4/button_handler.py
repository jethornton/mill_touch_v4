# Setup Help Text
import mill_touch_v4.helptext as helptext

def loadGcodeList(parent):
    titles = helptext.gcode_titles()
    #for index, value in enumerate(titles):
    #    parent.gcodeHelpListWidget.addItem(value)

    for key in sorted(titles.iterkeys()):
        parent.gcodeHelpListWidget.addItem(key + titles[key])

def holeOpsHandleKeys(parent, button):
    #print(button.text())
    #print(parent.drillOpBtnGrp.checkedButton().objectName())
    print(parent.holeOpBtnGrp.checkedButton().property('labelName'))
    entryPoint = parent.holeOpBtnGrp.checkedButton().property('labelName')
    drillLabel = getattr(parent, entryPoint)
    # drillOpBtnGrp
    #print(dir(parent.sender().button))
    char = str(button.text())
    text = drillLabel.text() or 'null'
    if text != 'null':
        text += char
    else:
        text = char
    drillLabel.setText(text)

def mdiHandleKeys(parent, button):
    char = str(button.text())
    text = parent.mdiEntry.text() or 'null'
    if text != 'null':
        text += char
    else:
        text = char
    parent.mdiEntry.setText(text)

def mdiSetLabels(parent):
    # get smart and figure out what axes are used

    text = parent.mdiEntry.text() or 'null'
    print(text)
    if text != 'null':
        words = helptext.gcode_words()
        if text in words:
            mdiClear(parent)
            for index, value in enumerate(words[text], start=1):
                print(value)
                getattr(parent, 'gcodeParameter_' + str(index)).setText(value)
        else:
            mdiClear(parent)
        titles = helptext.gcode_titles()
        if text in titles:
            parent.gcodeDescription.setText(titles[text])
        else:
            mdiClear(parent)
        parent.gcodeHelpLabel.setText(helptext.gcode_descriptions(text))
    else:
        mdiClear(parent)
        print('No Match')

def mdiClear(parent):
    for index in range(1,8):
        getattr(parent, 'gcodeParameter_' + str(index)).setText('')
    parent.gcodeDescription.setText('')
    parent.gcodeHelpLabel.setText('')

def mdiHandleBackSpace(parent):
    if len(parent.mdiEntry.text()) > 0:
        text = parent.mdiEntry.text()[:-1]
        parent.mdiEntry.setText(text)

def drillOpBackspace(parent):
    entryPoint = parent.holeOpBtnGrp.checkedButton().property('labelName')
    drillLabel = getattr(parent, entryPoint)
    if len(drillLabel.text()) > 0:
        text = drillLabel.text()[:-1]
        drillLabel.setText(text)

def coordListAddRow(parent):
    coords = ''
    if len(parent.coordListX.text()) > 0:
       coords = 'X' + parent.coordListX.text() + ' '
       parent.coordListX.setText('')
    if len(parent.coordListY.text()) > 0:
       coords += 'Y' + parent.coordListY.text() + ' '
       parent.coordListY.setText('')
    if len(parent.coordListZ.text()) > 0:
       coords += 'Z' + parent.coordListZ.text()
       parent.coordListZ.setText('')
    parent.coordListWidget.addItem(coords)

def coordListBackspace(parent):
    entryPoint = parent.coordListBtnGrp.checkedButton().property('labelName')
    coordLabel = getattr(parent, entryPoint)
    if len(coordLabel.text()) > 0:
        text = coordLabel.text()[:-1]
        coordLabel.setText(text)

def coordListMoveDown(parent):
    rows = parent.coordListWidget.count()-1
    currentRow = parent.coordListWidget.currentRow()
    if currentRow < rows:
        parent.coordListWidget.setCurrentRow(currentRow + 1)
    else:
        parent.coordListWidget.setCurrentRow(0)


def coordListMoveUp(parent):
    rows = parent.coordListWidget.count()-1
    currentRow = parent.coordListWidget.currentRow()
    if currentRow > 0:
        parent.coordListWidget.setCurrentRow(currentRow - 1)
    else:
        parent.coordListWidget.setCurrentRow(rows)

def gcodeListMoveDown(parent):
    rows = parent.gcodeHelpListWidget.count()-1
    currentRow = parent.gcodeHelpListWidget.currentRow()
    if currentRow < rows:
        if (currentRow + 25) < rows:
            parent.gcodeHelpListWidget.setCurrentRow(currentRow + 25)
        else:
            parent.gcodeHelpListWidget.setCurrentRow(rows)
    else:
        parent.gcodeHelpListWidget.setCurrentRow(0)


def gcodeListMoveUp(parent):
    rows = parent.gcodeHelpListWidget.count()-1
    currentRow = parent.gcodeHelpListWidget.currentRow()
    if currentRow > 0:
        if currentRow > 25:
            parent.gcodeHelpListWidget.setCurrentRow(currentRow - 25)
        else:
            parent.gcodeHelpListWidget.setCurrentRow(0)
    else:
        parent.gcodeHelpListWidget.setCurrentRow(rows)

def coordListClear(parent):
    parent.coordListWidget.clear()

def coordListRemoveLine(parent):
    #QListWidget.clear()
    #QListWidget.takeItem(index)
    #setCurrentRow(row)
    #count()
    parent.coordListWidget.takeItem(parent.coordListWidget.currentRow())

def g5xHandleKeys(parent, button):
    char = str(button.text())
    text = parent.g5xOffsetLbl.text() or 'null'
    if text != 'null':
        text += char
    else:
        text = char
    parent.g5xOffsetLbl.setText(text)

def g5xHandleBackSpace(parent):
    if len(parent.g5xOffsetLbl.text()) > 0:
        text = parent.g5xOffsetLbl.text()[:-1]
        parent.g5xOffsetLbl.setText(text)

def g92HandleKeys(parent, button):
    char = str(button.text())
    text = parent.g92OffsetsLbl.text() or 'null'
    if text != 'null':
        text += char
    else:
        text = char
    parent.g92OffsetsLbl.setText(text)

def g92HandleBackSpace(parent):
    if len(parent.g92OffsetsLbl.text()) > 0:
        text = parent.g92OffsetsLbl.text()[:-1]
        parent.g92OffsetsLbl.setText(text)



