import os
current_path = os.path.dirname(os.path.realpath(__file__)) + '/'

from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QDataWidgetMapper


def open_db(parent):
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(current_path + 'sfc.db')
    db.open()
    formModelInit(parent)
    sptmModelInit(parent)
    return db

def formModelInit(parent):
    parent.formMapper = QDataWidgetMapper(parent)
    parent.formModel = QSqlQueryModel(parent)
    parent.formModel.setQuery('SELECT DISTINCT form FROM threads')
    parent.formMapper.setModel(parent.formModel)
    parent.formMapper.addMapping(parent.threadFormLbl, 0, b'text')
    parent.formMapper.toLast()
    parent.formsLast = parent.formMapper.currentIndex()
    parent.formMapper.toFirst()
    classModelInit(parent)

def formNext(parent):
    if parent.formMapper.currentIndex() != parent.formsLast:
        parent.formMapper.toNext()
    else:
        parent.formMapper.toFirst()
    classModelInit(parent)

def formPrevious(parent):
    if parent.formMapper.currentIndex() != 0:
        parent.formMapper.toPrevious()
    else:
        parent.formMapper.toLast()
    classModelInit(parent)

def classModelInit(parent):
    parent.classMapper = QDataWidgetMapper(parent)
    parent.classModel = QSqlQueryModel(parent)
    form = parent.threadFormLbl.text()
    classSelect = "SELECT DISTINCT class FROM threads WHERE form = '{}'".format(form)
    parent.classModel.setQuery(classSelect)
    parent.classMapper.setModel(parent.classModel)
    parent.classMapper.addMapping(parent.threadClassLbl, 0, b'text')
    parent.classMapper.toLast()
    parent.classLast = parent.classMapper.currentIndex()
    parent.classMapper.toFirst()
    sizeModelInit(parent)

def classNext(parent):
    if parent.classMapper.currentIndex() != parent.classLast:
        parent.classMapper.toNext()
    else:
        parent.classMapper.toFirst()
    sizeModelInit(parent, parent.sizeMapper.currentIndex())

def classPrevious(parent):
    if parent.classMapper.currentIndex() != 0:
        parent.classMapper.toPrevious()
    else:
        parent.classMapper.toLast()
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
    parent.sizeMapper.toLast()
    parent.sizeLast = parent.sizeMapper.currentIndex()
    parent.sizeMapper.setCurrentIndex(index)

def sizeNext(parent):
    if parent.sizeMapper.currentIndex() != parent.sizeLast:
        parent.sizeMapper.toNext()
    else:
        parent.sizeMapper.toFirst()
    sptmCalculations(parent)

def sizePrevious(parent):
    if parent.sizeMapper.currentIndex() != 0:
        parent.sizeMapper.toPrevious()
    else:
        parent.sizeMapper.toLast()
    sptmCalculations(parent)

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

def sptmModelInit(parent):
    print('sptm model init')
    parent.sptmMapper = QDataWidgetMapper(parent)
    parent.sptmModel = QSqlQueryModel(parent)
    parent.sptmModel.setQuery('SELECT * FROM sptm')
    parent.sptmMapper.setModel(parent.sptmModel)
    parent.sptmMapper.addMapping(parent.sptmSizeLbl, 0, b'text')
    parent.sptmMapper.addMapping(parent.sptmDiameterLbl, 1, b'text')
    parent.sptmMapper.addMapping(parent.sptmCrestLbl, 2, b'text')
    parent.sptmMapper.addMapping(parent.sptmMaxDepthLbl, 3, b'text')
    parent.sptmMapper.addMapping(parent.sptmNeckDiaLbl, 5, b'text')
    parent.sptmMapper.toLast()
    parent.sptmLast = parent.sptmMapper.currentIndex()
    parent.sptmMapper.toFirst()
    sptmCalculations(parent)

def sptmNext(parent):
    if parent.sptmMapper.currentIndex() != parent.sptmLast:
        parent.sptmMapper.toNext()
    else:
        parent.sptmMapper.toFirst()
    sptmCalculations(parent)

def sptmPrevious(parent):
    if parent.sptmMapper.currentIndex() != 0:
        parent.sptmMapper.toPrevious()
    else:
        parent.sptmMapper.toLast()
    sptmCalculations(parent)

def sptmCalculations(parent):
    majorDia = float(parent.majorDiameterLbl.text())
    minorDia = float(parent.minMinorDiameterLbl.text())
    standardPDO = majorDia - minorDia
    parent.sptmStandardPDOLbl.setText(str(standardPDO))


"""
sptmDiameterLbl
sptmStandardPDOLbl
majorDiameterLbl
"""






