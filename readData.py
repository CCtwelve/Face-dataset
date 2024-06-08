import os.path
import struct
import numpy as np


def readModel(path_cie):

    if (os.path.exists(path_cie) and os.path.exists(path_cie)) == False:
        print("The path does not exist.")
        return None

    f = open(path_cie, 'rb+')
    bytestring = f.read(16)
    length = struct.unpack("4I", bytestring)
    if length == 0: return None

    vert_xyz = np.zeros([3, length[0]], dtype=float)
    vertnorm = np.zeros([3, length[0]], dtype=float)

    for i in range(length[0]):
        bytestring = f.read(64)
        tmp = struct.unpack("3fc3fc8f", bytestring)

        vert_xyz[0, i] = tmp[0]
        vert_xyz[1, i] = tmp[1]
        vert_xyz[2, i] = tmp[2]

        vertnorm[0, i] = tmp[4]
        vertnorm[1, i] = tmp[5]
        vertnorm[2, i] = tmp[6]

    faces = np.zeros([4, length[1]], dtype=int)
    bytestring = f.read(4 * length[1] * 4)  #
    tmp = struct.unpack(str(length[1] * 4) + "i", bytestring)

    for i in range(length[2]):
        faces[0, i] = tmp[i * 4 + 0]
        faces[1, i] = tmp[i * 4 + 1]
        faces[2, i] = tmp[i * 4 + 2]
        faces[3, i] = tmp[i * 4 + 3]

        # f.seek(4 * tt00[1] * 4, 1)

    facesEx = np.zeros([4, length[2]], dtype=np.float32)
    bytestring = f.read(4 * length[2] * 4)  #
    tmp = struct.unpack(str(length[2] * 4) + "f", bytestring)
    for i in range(length[2]):
        facesEx[0, i] = tmp[i * 4 + 0]
        facesEx[1, i] = tmp[i * 4 + 1]
        facesEx[2, i] = tmp[i * 4 + 2]
        facesEx[3, i] = tmp[i * 4 + 3]

    fkp = np.zeros(length[3], dtype=int)
    bytestring = f.read(4 * length[3])  #
    tmp = struct.unpack(str(length[3]) + "i", bytestring)
    fkpXYZ = np.zeros([3, length[3]], dtype=float)
    for i in range(length[3]):
        fkp[i] = tmp[i]
        fkpXYZ[0, i] = vert_xyz[0, fkp[i]]
        fkpXYZ[1, i] = vert_xyz[1, fkp[i]]
        fkpXYZ[2, i] = vert_xyz[2, fkp[i]]


    return vert_xyz, fkpXYZ


def write_points(xyz, path):
    with open(path, 'w+', encoding='utf-8') as f:
        for i in range(xyz.shape[1]):
            sstr = str(format(xyz[0, i], '.3f')) + ' ' + \
                   str(format(xyz[1, i], '.3f')) + ' ' + \
                   str(format(xyz[2, i], '.3f')) + ' ' +   '\n'

            f.write(sstr)

def write_landmark(xyz, path):
    with open(path, 'w+', encoding='utf-8') as f:
        for i in range(xyz.shape[1]):
            sstr = str(format(xyz[0, i], '.3f')) + ' ' + \
                   str(format(xyz[1, i], '.3f')) + ' ' + \
                   str(format(xyz[2, i], '.3f')) + '\n'
            f.write(sstr)
