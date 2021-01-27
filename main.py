import numpy as np
from process.ProcessGenerator import ProcessGenerator
import os


def main():
    dir_path = "./data/contrast/"
    file_names = []
    for file in os.listdir(dir_path):
        if file.endswith(".mat"):
            file_names.append(os.path.join(dir_path, file))
    print("process")
    process = ProcessGenerator(file_names, "Extended Jaccard", 5,"Momenta Tree", 2,"matfiles", True)
    njdismatrix = process.njdismatrix

    print(njdismatrix.matrix)


if __name__ == "__main__":
    main()
