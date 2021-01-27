from numpy import *
import numpy as np
import scipy.io as sio
import os
import matplotlib.pyplot as plt
from normalization.MinMaxNormalization import MinMaxNormalization
# from scipy.ndimage import zoom
from skimage.transform import resize, rescale, downscale_local_mean
import matplotlib.pyplot as plt
from collections import Counter
import cv2


class SyntheticCaseCreator:

    def __init__(self):
        self.generate_left();
        self.generate_right();
        self.generate_center();

    def generate_left(self):
        
        # 1
        a = dict()
        value_matrix = [[1,1,0,0,0], [0,1,1,0,0], [0,0,1,1,0], [0,0,0,1,1]];           
        a[str(11)] = value_matrix;
        sio.savemat("../data/synthetic_case/11.mat", a)
        print("11")
        plt.imshow(value_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/synthetic_case/11.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        #plt.show()
        
        # 2
        a = dict()
        value_matrix = [[1,1,1,0,0], [0,1,1,0,0], [0,0,1,1,0], [0,0,1,1,1]];           
        a[str(12)] = value_matrix;
        sio.savemat("../data/synthetic_case/12.mat", a)
        print("12")
        plt.imshow(value_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/synthetic_case/12.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        #plt.show()
        
        # 3
        a = dict()
        value_matrix = [[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]];           
        a[str(13)] = value_matrix;
        sio.savemat("../data/synthetic_case/13.mat", a)
        print("13")
        plt.imshow(value_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/synthetic_case/13.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        #plt.show()
        
        # 4
        a = dict()
        value_matrix = [[1,1,1,0,0], [0,1,1,0,0], [0,1,1,1,0], [0,0,0,1,1]];           
        a[str(14)] = value_matrix;
        sio.savemat("../data/synthetic_case/14.mat", a)
        print("14")
        plt.imshow(value_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/synthetic_case/14.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        #plt.show()
        
        # 5
        a = dict()
        value_matrix = [[1,1,0,0,0], [0,1,1,1,0], [0,0,1,1,0], [0,0,0,1,1]];           
        a[str(15)] = value_matrix;
        sio.savemat("../data/synthetic_case/15.mat", a)
        print("15")
        plt.imshow(value_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/synthetic_case/15.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        #plt.show()

    def generate_right(self):
        
        # 1
        a = dict()
        value_matrix = [[0,0,0,1,1], [0,0,1,1,0], [0,1,1,0,0], [1,1,0,0,0]];           
        a[str(21)] = value_matrix;
        sio.savemat("../data/synthetic_case/21.mat", a)
        print("21")
        plt.imshow(value_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/synthetic_case/21.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        #plt.show()
        
        # 2
        a = dict()
        value_matrix = [[0,0,1,1,1], [0,0,1,1,0], [0,1,1,0,0], [1,1,1,0,0]];           
        a[str(22)] = value_matrix;
        sio.savemat("../data/synthetic_case/22.mat", a)
        print("22")
        plt.imshow(value_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/synthetic_case/22.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        #plt.show()
        
        # 3
        a = dict()
        value_matrix = [[0,0,0,0,1], [0,0,0,1,0], [0,0,1,0,0], [1,1,0,0,0]];           
        a[str(23)] = value_matrix;
        sio.savemat("../data/synthetic_case/23.mat", a)
        print("23")
        plt.imshow(value_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/synthetic_case/23.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        #plt.show()
        
        # 4
        a = dict()
        value_matrix = [[0,0,1,1,1], [0,0,1,1,0], [0,1,1,1,0], [1,1,0,0,0]];            
                
        a[str(24)] = value_matrix;
        sio.savemat("../data/synthetic_case/24.mat", a)
        print("24")
        plt.imshow(value_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/synthetic_case/24.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        #plt.show()
        
        # 5
        a = dict()
        value_matrix = [[0,0,0,1,1], [0,1,1,1,0], [0,1,1,0,0], [1,1,0,0,0]];           
        a[str(25)] = value_matrix;
        sio.savemat("../data/synthetic_case/25.mat", a)
        print("25")
        plt.imshow(value_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/synthetic_case/25.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        #plt.show()
        
    def generate_center(self):
        
        # 1
        a = dict()
        value_matrix = [[0,0,0,0,0], [0,1,1,1,0], [0,1,1,1,0], [0,0,0,0,0]];           
        a[str(31)] = value_matrix;
        sio.savemat("../data/synthetic_case/31.mat", a)
        print("31")
        plt.imshow(value_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/synthetic_case/31.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        #plt.show()
        
        # 2
        a = dict()
        value_matrix = [[0,0,0,0,0], [0,0,1,1,0], [0,1,1,1,0], [0,0,0,0,0]];             
        a[str(32)] = value_matrix;
        sio.savemat("../data/synthetic_case/32.mat", a)
        print("32")
        plt.imshow(value_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/synthetic_case/32.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        #plt.show()
        
        # 3
        a = dict()
        value_matrix = [[0,0,0,0,0], [0,1,1,1,0], [0,1,1,0,0], [0,0,0,0,0]];            
        a[str(33)] = value_matrix;
        sio.savemat("../data/synthetic_case/33.mat", a)
        print("33")
        plt.imshow(value_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/synthetic_case/33.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        #plt.show()
        
        # 4
        a = dict()
        value_matrix = [[0,0,0,0,0], [0,1,1,1,0], [0,1,0,1,0], [0,0,0,0,0]];              
                
        a[str(34)] = value_matrix;
        sio.savemat("../data/synthetic_case/34.mat", a)
        print("34")
        plt.imshow(value_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/synthetic_case/34.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        #plt.show()
        
        # 5
        a = dict()
        value_matrix = [[0,0,0,0,0], [0,1,0,1,0], [0,1,1,1,0], [0,0,0,0,0]];              
        a[str(35)] = value_matrix;
        sio.savemat("../data/synthetic_case/35.mat", a)
        print("35")
        plt.imshow(value_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/synthetic_case/35.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        #plt.show()
    
    

 
def main():
    synthetic_case_creator = SyntheticCaseCreator()


if __name__ == "__main__":
    main()
