

import os
import readData

def collect_cie_file_paths(directory):
    cie_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.cie'):
                cie_paths.append(os.path.join(root, file))
    return cie_paths


if __name__=="__main__":
    cie_path = ''
    cie_path_list=collect_cie_file_paths(cie_path)
    for i in range(len(cie_path_list )):
        path =cie_path_list[i]
        out = readData.readModel(path)
        file_path=os.path.dirname(path)
        file_name=os.path.basename(path).split('.')[0]

        readData.write_points(out[0], os.path.join(file_path, f'{file_name}_points.txt'))
        readData.write_landmark(out[1], os.path.join(file_path, f'{file_name}_landmark.txt'))

