# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\sdayani\Documents\GitHub\Xplore4CT\_DevelopingSandBox\Ui_files\ToolboxWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ToolboxWidget(object):
    def setupUi(self, ToolboxWidget):
        ToolboxWidget.setObjectName("ToolboxWidget")
        ToolboxWidget.resize(466, 660)
        self.verticalLayout = QtWidgets.QVBoxLayout(ToolboxWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ToolboxWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lbl_filename = QtWidgets.QLabel(ToolboxWidget)
        self.lbl_filename.setObjectName("lbl_filename")
        self.verticalLayout.addWidget(self.lbl_filename)
        self.widget = QtWidgets.QWidget(ToolboxWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Explore = QtWidgets.QWidget()
        self.tab_Explore.setObjectName("tab_Explore")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_Explore)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.X_spinbox = QtWidgets.QSpinBox(self.tab_Explore)
        self.X_spinbox.setObjectName("X_spinbox")
        self.gridLayout.addWidget(self.X_spinbox, 0, 1, 1, 1)
        self.T_spinbox = QtWidgets.QSpinBox(self.tab_Explore)
        self.T_spinbox.setObjectName("T_spinbox")
        self.gridLayout.addWidget(self.T_spinbox, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_Explore)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.Y_slider = QtWidgets.QSlider(self.tab_Explore)
        self.Y_slider.setEnabled(False)
        self.Y_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Y_slider.setObjectName("Y_slider")
        self.gridLayout.addWidget(self.Y_slider, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_Explore)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.Z_spinbox = QtWidgets.QSpinBox(self.tab_Explore)
        self.Z_spinbox.setObjectName("Z_spinbox")
        self.gridLayout.addWidget(self.Z_spinbox, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_Explore)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.T_slider = QtWidgets.QSlider(self.tab_Explore)
        self.T_slider.setEnabled(False)
        self.T_slider.setOrientation(QtCore.Qt.Horizontal)
        self.T_slider.setObjectName("T_slider")
        self.gridLayout.addWidget(self.T_slider, 3, 2, 1, 1)
        self.Y_spinbox = QtWidgets.QSpinBox(self.tab_Explore)
        self.Y_spinbox.setObjectName("Y_spinbox")
        self.gridLayout.addWidget(self.Y_spinbox, 1, 1, 1, 1)
        self.X_slider = QtWidgets.QSlider(self.tab_Explore)
        self.X_slider.setOrientation(QtCore.Qt.Horizontal)
        self.X_slider.setObjectName("X_slider")
        self.gridLayout.addWidget(self.X_slider, 0, 2, 1, 1)
        self.Z_slider = QtWidgets.QSlider(self.tab_Explore)
        self.Z_slider.setEnabled(False)
        self.Z_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Z_slider.setObjectName("Z_slider")
        self.gridLayout.addWidget(self.Z_slider, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_Explore)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_Explore)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.radio_X = QtWidgets.QRadioButton(self.groupBox)
        self.radio_X.setChecked(True)
        self.radio_X.setObjectName("radio_X")
        self.verticalLayout_5.addWidget(self.radio_X)
        self.radio_Y = QtWidgets.QRadioButton(self.groupBox)
        self.radio_Y.setObjectName("radio_Y")
        self.verticalLayout_5.addWidget(self.radio_Y)
        self.radio_Z = QtWidgets.QRadioButton(self.groupBox)
        self.radio_Z.setObjectName("radio_Z")
        self.verticalLayout_5.addWidget(self.radio_Z)
        self.radio_all = QtWidgets.QRadioButton(self.groupBox)
        self.radio_all.setObjectName("radio_all")
        self.verticalLayout_5.addWidget(self.radio_all)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_5.addWidget(self.textBrowser)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.gridLayout.addWidget(self.groupBox, 4, 1, 1, 2)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab_Explore, "")
        self.tab_rotate = QtWidgets.QWidget()
        self.tab_rotate.setObjectName("tab_rotate")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_rotate)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget.addTab(self.tab_rotate, "")
        self.tab_crop = QtWidgets.QWidget()
        self.tab_crop.setObjectName("tab_crop")
        self.tabWidget.addTab(self.tab_crop, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(ToolboxWidget)
        self.widget_2.setObjectName("widget_2")
        self.btn_apply = QtWidgets.QPushButton(self.widget_2)
        self.btn_apply.setGeometry(QtCore.QRect(50, 10, 75, 23))
        self.btn_apply.setObjectName("btn_apply")
        self.btn_cancel = QtWidgets.QPushButton(self.widget_2)
        self.btn_cancel.setGeometry(QtCore.QRect(150, 10, 75, 23))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_load_setting = QtWidgets.QPushButton(self.widget_2)
        self.btn_load_setting.setGeometry(QtCore.QRect(250, 10, 91, 21))
        self.btn_load_setting.setObjectName("btn_load_setting")
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(2, 10)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(ToolboxWidget)
        self.tabWidget.setCurrentIndex(0)
        self.radio_X.toggled['bool'].connect(self.X_slider.setEnabled)
        self.X_spinbox.valueChanged['int'].connect(self.X_slider.setValue)
        self.X_slider.valueChanged['int'].connect(self.X_spinbox.setValue)
        self.Y_spinbox.valueChanged['int'].connect(self.Y_slider.setValue)
        self.Y_slider.valueChanged['int'].connect(self.Y_spinbox.setValue)
        self.Z_spinbox.valueChanged['int'].connect(self.Z_slider.setValue)
        self.Z_slider.valueChanged['int'].connect(self.Z_spinbox.setValue)
        self.T_spinbox.valueChanged['int'].connect(self.T_slider.setValue)
        self.T_slider.valueChanged['int'].connect(self.T_spinbox.setValue)
        self.radio_Y.toggled['bool'].connect(self.Y_slider.setEnabled)
        self.radio_Z.toggled['bool'].connect(self.Z_slider.setEnabled)
        self.radio_all.toggled['bool'].connect(self.Z_slider.setEnabled)
        self.radio_all.toggled['bool'].connect(self.Y_slider.setEnabled)
        self.radio_all.toggled['bool'].connect(self.X_slider.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ToolboxWidget)

    def retranslateUi(self, ToolboxWidget):
        _translate = QtCore.QCoreApplication.translate
        ToolboxWidget.setWindowTitle(_translate("ToolboxWidget", "Form"))
        self.label.setText(_translate("ToolboxWidget", "Tool Box Pannel"))
        self.lbl_filename.setText(_translate("ToolboxWidget", "File Name : "))
        self.label_3.setText(_translate("ToolboxWidget", "Y"))
        self.label_5.setText(_translate("ToolboxWidget", "T"))
        self.label_4.setText(_translate("ToolboxWidget", "Z"))
        self.label_2.setText(_translate("ToolboxWidget", "X"))
        self.groupBox.setTitle(_translate("ToolboxWidget", "Viewing Options"))
        self.label_6.setText(_translate("ToolboxWidget", "Select desired View :"))
        self.radio_X.setText(_translate("ToolboxWidget", "X"))
        self.radio_Y.setText(_translate("ToolboxWidget", "Y"))
        self.radio_Z.setText(_translate("ToolboxWidget", "Z"))
        self.radio_all.setText(_translate("ToolboxWidget", "All (this needs multiple EPICS Viewers)"))
        self.textBrowser.setHtml(_translate("ToolboxWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600;\">Multiple View: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">to set up multiple slice view, please open more EPICS Viewers. Set up the channel names in </span><span style=\" font-size:8.25pt; font-style:italic; text-decoration: underline;\">setting</span><span style=\" font-size:8.25pt;\"> dialogue. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600;\">Note</span><span style=\" font-size:8.25pt;\">: It is recommended to use Y,Z and All View options, only when the volume is loaded in the RAM. Large HDF files tend to be slow when slicing.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Explore), _translate("ToolboxWidget", "Explore"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rotate), _translate("ToolboxWidget", "Rotate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_crop), _translate("ToolboxWidget", "Crop"))
        self.btn_apply.setText(_translate("ToolboxWidget", "Apply"))
        self.btn_cancel.setText(_translate("ToolboxWidget", "Cancel"))
        self.btn_load_setting.setText(_translate("ToolboxWidget", "Load Settings"))
