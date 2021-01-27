from numpy import *
import numpy as np
import scipy.io as sio
import os
import matplotlib.pyplot as plt
from skimage.transform import resize, rescale, downscale_local_mean
import matplotlib.pyplot as plt
from collections import Counter
import cv2


class SyntheticDataCreator:

    def __init__(self):
        self.original_matrix = np.full((60, 60), 29)

        min_value = np.nanmin(self.original_matrix)
        max_value = np.nanmax(self.original_matrix)
        self.norm_matrix = self.normalize(self.original_matrix, min_value, max_value,
                                                                 1, 10.0)
        self.norm_matrix = np.nan_to_num(self.norm_matrix)


    def normalize(self, matrix, old_min, old_max, new_min, new_max):
        div = old_max - old_min
        if div==0:
            div = 0.0001
        norm_matrix = [(((x - old_min) * (new_max - new_min)) / div) + new_min for x in matrix]
        return norm_matrix

    def generate_example1(self):

        a = dict()
        a[str("ex1_A")] = self.norm_matrix
        sio.savemat("../data/rebuttal_examples/ex1_A.mat", a)
        plt.imshow(self.norm_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/rebuttal_examples/ex1_A.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        plt.show()

        a = dict()
        a[str("ex1_B")] = self.norm_matrix
        sio.savemat("../data/rebuttal_examples/ex1_B.mat", a)
        plt.imshow(self.norm_matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/rebuttal_examples/ex1_B.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        plt.show()



        a = dict()
        matrix = self.norm_matrix.copy()
        shape = matrix.shape
        matrix[0][shape[1]-1]= matrix[0][shape[1]-1]* 2
        matrix[0][shape[1]-2]= matrix[0][shape[1]-2]* 2
        matrix[0][shape[1]-3]= matrix[0][shape[1]-3]* 2
        matrix[1][shape[1]-1]= matrix[1][shape[1]-1]* 2
        matrix[1][shape[1]-2]= matrix[1][shape[1]-2]* 2
        matrix[1][shape[1]-3]= matrix[1][shape[1]-3]* 2
        matrix[2][shape[1]-1]= matrix[2][shape[1]-1]* 2
        matrix[2][shape[1]-2]= matrix[2][shape[1]-2]* 2
        matrix[2][shape[1]-3]= matrix[2][shape[1]-3]* 2
        print(shape)
        a[str("ex1_C")] = matrix
        sio.savemat("../data/rebuttal_examples/ex1_C.mat", a)
        plt.imshow(matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/rebuttal_examples/ex1_C.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        plt.show()



        a = dict()
        matrix = self.norm_matrix.copy()
        shape = matrix.shape

        for x in range(int(shape[1]/4)*1, int(shape[1]/4)*3, 1):
            for y in range(int(shape[1]/4)*1, int(shape[1]/4)*3, 1):
                matrix[x][y]= matrix[0][0]* 2
        print(shape)
        a[str("ex1_C")] = matrix
        sio.savemat("../data/rebuttal_examples/ex1_D.mat", a)
        plt.imshow(matrix, cmap='nipy_spectral', vmin=0.0, vmax=10.0,  interpolation='nearest')
        # plt.colorbar()
        plt.axis('off')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.savefig("../data/rebuttal_examples/ex1_D.png",  bbox_inches='tight', pad_inches=0, transparent=True)
        plt.show()





def main():
    synthetic_data_creator = SyntheticDataCreator()
    synthetic_data_creator.generate_example1()


if __name__ == "__main__":
    main()
