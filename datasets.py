import functools
import glob
import numpy as np
from stl import mesh
import SimpleITK as sitk
import util
import torch
from torchvision import transforms

@functools.lru_cache(1)
def getStlInfoList(requireOnDisk_bool=True):
    stl_list = # import from folder "stls" when it has all stls necessary



class Stl:
    def __init__(self):
        stl_path = glob.glob('stls/{}.stl')

        # model_stl = mesh.Mesh.from_file(stl_path)
        # model_arr = np.array(model_stl.points, dtype=np.float32)

        model_stl = sitk.ReadImage(stl_path)
        model_arr = np.array(sitk.GetArrayFromImage(model_stl), dtype=np.float32)

        
        self.origin_xyz = util.xyztuple(*model_stl.GetOrigin())
        self.vxSize_xyz = util.xyztuple(*model_stl.GetSpacing())
        self.direction_a = np.array(model_stl.GetDirection()).reshape(3, 3)



    def getRawModel(self, center_xyz, width_irc):
        center_irc = util.xyz2irc(
            center_xyz,
            self.origin_xyz,
            self.vxSize_xyz,
            self.direction_a
        )

        slice_list = []
        for axis, center_val in enumerate(center_irc):
            start_ndx = int(round(center_val - width_irc[axis]/2))
            end_ndx = int(start_ndx + width_irc[axis])
            slice_list.append(slice(start_ndx, end_ndx))

        model_chunk = self.hu_a[tuple(slice_list)]

        return model_chunk, center_irc


def __getitem__(self, ndx):
    width_irc = (32, 48, 48)
    model_a, center_irc = getCtRawModel

    return (
        model_t, 1((CO10-1)) pos_t, 
        torch.tensor(center_irc)
    )


