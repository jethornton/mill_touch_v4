
def holeOpsHandleKeys(parent, button):
    #print(button.text())
    #print(parent.drillOpBtnGrp.checkedButton().objectName())
    print(parent.holeOpBtnGrp.checkedButton().property('labelName'))
    entryPoint = parent.holeOpBtnGrp.checkedButton().property('labelName')
    drillLabel = getattr(parent, entryPoint)
    # drillOpBtnGrp
    #print(dir(parent.sender().button))
    char = str(button.text())
    text = drillLabel.text() or '0'
    if text != '0':
        text += char
    else:
        text = char
    drillLabel.setText(text)

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


def coordListClear(parent):
    parent.coordListWidget.clear()

def coordListRemoveLine(parent):
    #QListWidget.clear()
    #QListWidget.takeItem(index)
    #setCurrentRow(row)
    #count()
    parent.coordListWidget.takeItem(parent.coordListWidget.currentRow())

