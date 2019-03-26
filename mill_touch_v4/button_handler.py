

def drillOpHandleKeys(parent, button):
    #print(button.text())
    #print(parent.drillOpBtnGrp.checkedButton().objectName())
    #print(parent.drillOpBtnGrp.checkedButton().property('test'))
    entryPoint = parent.drillOpBtnGrp.checkedButton().property('labelName')
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


