import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import numpy as np

#import all Ui files 

from Ui_files.ToolboxWidget_ui import Ui_ToolboxWidget


#import other modules
from importExport import ImportFile
from imageJ_viewer import ImageJViewer

import os


class toolBoxWidget(qtw.QWidget):

    #create Signals : 
    #test signal for recieving data : 
    send_data_signal = qtc.pyqtSignal(str)


    #signal for emiting clicked item data : 
    


    def __init__(self, appSetting, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #your code will go here 

        #create builder for the imported ui
        self.ui = Ui_ToolboxWidget()
        self.ui.setupUi(self)
        
        
        #creating variables : 


        

        

        #connecting signals and signals 
        self.send_data_signal.connect(self.recieve_data)
        self.ui.X_slider.valueChanged.connect(self.Explore)
        self.ui.Y_slider.valueChanged.connect ( self.Explore)
        self.ui.Z_slider.valueChanged.connect ( self.Explore)

        #FOR TESTING PURPOSE :
        #create test data :
        self.create_test_data(Type = "3DHDF"  , path=r"E:\sdayani\reco\572_221019_0148_00001.h5")
        #create EPICS channels : 
        self.ImageJViewer = ImageJViewer("Xplore")
        #self.ImageJViewer.send_image(image)
        

        #your code ends here 
        self.show()

    #HELPER FUNCTIONS : 
    def set_range(self, qtWidget , limit):
        #set slider or spin box limits 
        # limit : tuple 
        #
        qtWidget.setMinimum(limit[0])
        qtWidget.setMaximum(limit[1])


    #when recieving data needs to be processed first here :
    @qtc.pyqtSlot(str)
    def recieve_data(self,dataobject):
        # this function checkes type of recieved data: 

        #a. one HDF 3D data on hard disk
        #b. a series of HDF 3D data on hard disk (4D)
        #c. one 3D dataset in RAM
        #d. an array of 3D data in RAM (4D)

        #each data type needs to be processed individually
        print(dataobject)

        if dataobject == "3DHDF":
            self.dataType = "3DHDF"
            print("recieved data ")
            print(self.vol_proxy.shape)
            #update scroll bars and their limits : 
            x,y,z = self.vol_proxy.shape
            
            print (x,y,z)
            for widget in [self.ui.X_spinbox,self.ui.X_slider]:
                self.set_range(widget , (0,x))
                
            for widget in [self.ui.Y_spinbox,self.ui.Y_slider]:
                self.set_range(widget , (0,y))
                
            for widget in [self.ui.Z_spinbox,self.ui.Z_slider]:
                self.set_range(widget , (0,z))


    def create_test_data (self,**kwarg):
        #this function is for testing purpose only
        #please delete this function when product is final 

        #this function creates data to test functionalities within this class. 
        #openning an hdf5 file 
        #reading settings and dimensions of the hdf5 file
        #create setting object : 
        #   create EPICS channel names , for XY , XZ and YZ plane 
        if ("Type" in kwarg) and( kwarg["Type"] == "3DHDF"):
            self.path = kwarg["path"] 
            importer = ImportFile(self.path)
            importer.openFile(volume = "Volume" )
            self.vol_proxy = importer.vol_proxy
            self.send_data_signal.emit("3DHDF")
            


        # Volume in RAM : 
        # create a small volume for working with data stored in RAM 

        # 4D data hdf5 

        # 4D data , RAM 


    def Explore(self):
        #when a slider is changed , this function is called 
        #depending on the following conditions , this function updates canvases 
        
        #a. one HDF 3D data on hard disk
        #b. a series of HDF 3D data on hard disk (4D)
        #c. one 3D dataset in RAM
        #d. an array of 3D data in RAM (4D)

        #reslicing in X, Y, Z direction, or all of them 

        if self.dataType == "3DHDF" : 
            if self.ui.radio_all.isChecked() == False :
                slice=self.reslice_volume_3dHdf()
                self.send_image(slice)
            elif self.ui.radio_all.isChecked() == True : 
                print ("we need to set up 3 EPICS windows...")
                print( " this is not implemented yet please chosse another mode")
        






    def reslice_volume (self,volume, slice_no, axis ="x"):
        print("fetching ... slice {} ".format(slice_no))
        if axis == "x":
            slice=volume[slice_no,:,:]
        elif axis == "y":
            slice=volume[:,slice_no,:]
        elif axis == "z":
            slice=volume[:,:,slice_no]

        print("successfully fetched")
        return slice



    def reslice_volume_3dHdf(self):
        #calculation for reslicing an HDF 3D volume 
        slice = np.zeros((100,100))
        x_slice = self.ui.X_slider.value()
        y_slice = self.ui.Y_slider.value()
        z_slice = self.ui.Z_slider.value()
        
        if self.ui.radio_X.isChecked() == True:
            slice= self.reslice_volume(self.vol_proxy ,x_slice, axis = "x")
            
        elif self.ui.radio_Y.isChecked() == True: 
            slice=self.reslice_volume(self.vol_proxy ,y_slice, axis = "y")

        elif self.ui.radio_Z.isChecked() == True:
            slice=self.reslice_volume(self.vol_proxy ,z_slice, axis = "z")

        return slice


        

    def send_image(self,image):
        self.ImageJViewer.send_image(image)





if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    appSetting = "sampleSetting which is not real "
    w = toolBoxWidget(appSetting)
    sys.exit(app.exec_())

