import os
current_path = os.path.dirname(os.path.realpath(__file__)) + '/'

from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QDataWidgetMapper


def open_db(parent):
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(current_path + 'sfc.db')
    db.open()
    formModelInit(parent)
    return db

def formModelInit(parent):
    parent.formMapper = QDataWidgetMapper(parent)
    parent.formModel = QSqlQueryModel(parent)
    parent.formModel.setQuery('SELECT DISTINCT form FROM threads')
    parent.formMapper.setModel(parent.formModel)
    parent.formMapper.addMapping(parent.threadFormLbl, 0, b'text')
    #parent.formMapper.currentIndexChanged.connect(parent.formChanged)
    parent.formMapper.toLast()
    parent.formsLast = parent.formMapper.currentIndex()
    parent.formMapper.toFirst()
    #parent.formIndexLbl.setText('{}'.format(parent.formMapper.currentIndex()))
    classModelInit(parent)

def formNext(parent):
    #print('before {}'.format(parent.mapper.currentIndex()))
    if parent.formMapper.currentIndex() != parent.formsLast:
        parent.formMapper.toNext()
    else:
        parent.formMapper.toFirst()
    #parent.formIndexLbl.setText('{}'.format(parent.formMapper.currentIndex()))
    #print('after {}'.format(parent.mapper.currentIndex()))
    classModelInit(parent)

def formPrevious(parent):
    if parent.formMapper.currentIndex() != 0:
        parent.formMapper.toPrevious()
    else:
        parent.formMapper.toLast()
    #parent.formIndexLbl.setText('{}'.format(parent.formMapper.currentIndex()))
    classModelInit(parent)

def formChanged(parent):
    # is fired before the change is complete
    pass

def classModelInit(parent):
    print('class update')
    parent.classMapper = QDataWidgetMapper(parent)
    parent.classModel = QSqlQueryModel(parent)
    form = parent.threadFormLbl.text()
    print(form)
    classSelect = "SELECT DISTINCT class FROM threads WHERE form = '{}'".format(form)
    parent.classModel.setQuery(classSelect)
    parent.classMapper.setModel(parent.classModel)
    parent.classMapper.addMapping(parent.threadClassLbl, 0, b'text')
    #parent.classMapper.currentIndexChanged.connect(parent.formChanged)
    parent.classMapper.toLast()
    parent.classLast = parent.classMapper.currentIndex()
    parent.classMapper.toFirst()
    #parent.classIndexLbl.setText('{}'.format(parent.classMapper.currentIndex()))
    sizeModelInit(parent)

def classNext(parent):
    #print('before {}'.format(parent.mapper.currentIndex()))
    if parent.classMapper.currentIndex() != parent.classLast:
        parent.classMapper.toNext()
    else:
        parent.classMapper.toFirst()
    #parent.classIndexLbl.setText('{}'.format(parent.classMapper.currentIndex()))
    #print('after {}'.format(parent.mapper.currentIndex()))
    sizeModelInit(parent, parent.sizeMapper.currentIndex())

def classPrevious(parent):
    if parent.classMapper.currentIndex() != 0:
        parent.classMapper.toPrevious()
    else:
        parent.classMapper.toLast()
    #parent.classIndexLbl.setText('{}'.format(parent.classMapper.currentIndex()))
    sizeModelInit(parent, parent.sizeMapper.currentIndex())


def sizeModelInit(parent, index = 0):
    parent.sizeMapper = QDataWidgetMapper(parent)
    parent.sizeModel = QSqlQueryModel(parent)
    form = str(parent.threadFormLbl.text())
    fit = parent.threadClassLbl.text()
    sizeSelect = "SELECT * FROM threads WHERE form = '{}' AND class = '{}'".format(form, fit)
    parent.sizeModel.setQuery(sizeSelect)
    parent.sizeMapper.setModel(parent.sizeModel)
    parent.sizeMapper.addMapping(parent.threadSizeLbl, 0, b'text')
    parent.sizeMapper.addMapping(parent.threadPitchLbl, 3, b'text')
    parent.sizeMapper.addMapping(parent.majorDiameterLbl, 4, b'text')
    parent.sizeMapper.addMapping(parent.maxMajorDiameterLbl, 5, b'text')
    parent.sizeMapper.addMapping(parent.minMajorDiameterLbl, 6, b'text')
    parent.sizeMapper.addMapping(parent.pitchDiameterLbl, 7, b'text')
    parent.sizeMapper.addMapping(parent.maxPitchDiameterLbl, 8, b'text')
    parent.sizeMapper.addMapping(parent.minPitchDiameterLbl, 9, b'text')
    parent.sizeMapper.addMapping(parent.minMinorDiameterLbl, 10, b'text')
    #parent.sizeMapper.currentIndexChanged.connect(parent.formChanged)
    parent.sizeMapper.toLast()
    parent.sizeLast = parent.sizeMapper.currentIndex()
    parent.sizeMapper.setCurrentIndex(index)
    #parent.sizeMapper.toFirst()
    #parent.sizeIndexLbl.setText('{}'.format(parent.sizeMapper.currentIndex()))

def sizeNext(parent):
    #print('before {}'.format(parent.mapper.currentIndex()))
    if parent.sizeMapper.currentIndex() != parent.sizeLast:
        parent.sizeMapper.toNext()
    else:
        parent.sizeMapper.toFirst()
    #parent.sizeIndexLbl.setText('{}'.format(parent.sizeMapper.currentIndex()))
    #print('after {}'.format(parent.mapper.currentIndex()))

def sizePrevious(parent):
    if parent.sizeMapper.currentIndex() != 0:
        parent.sizeMapper.toPrevious()
    else:
        parent.sizeMapper.toLast()
    #parent.sizeIndexLbl.setText('{}'.format(parent.sizeMapper.currentIndex()))

def appendSPTM(parent):
    query = QSqlQuery()
    query.prepare("INSERT INTO sptm (size, diameter, crest, max_depth) \
    VALUES (:size, :diameter, :crest, :max_depth)")
    query.bindValue(":size", parent.sptmSizeEntry.text())
    query.bindValue(":diameter", parent.sptmDiameterEntry.text())
    query.bindValue(":crest", parent.sptmCrestEntry.text())
    query.bindValue(":max_depth", parent.sptmMaxDepthEntry.text())
    if query.exec_():
        print("Successful")
        parent.sptmSizeEntry.setText('')
        parent.sptmDiameterEntry.setText('')
        parent.sptmCrestEntry.setText('')
        parent.sptmMaxDepthEntry.setText('')
        parent.statusBar.showMessage("Database Insert Successful",5000)
    else:
        print("Error: ", query.lastError().text())

