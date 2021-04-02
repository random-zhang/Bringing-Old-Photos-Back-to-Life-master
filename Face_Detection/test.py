import numpy as np
import matplotlib.pyplot as plt

def calculate_lookup(src_cdf, ref_cdf):
    """
    This method creates the lookup（检查） table
    :param array src_cdf: The cdf for the source image
    :param array ref_cdf: The cdf for the reference image
    :return: lookup_table: The lookup table
    :rtype: array
    """
    lookup_table = np.zeros(4)#256个0组成的数组
    lookup_val = 0
    for src_pixel_val in range(len(src_cdf)):
        lookup_val  #当用遍历src_cdf时 找到第一个大于ref_cdf值大于src_cdf 值的j 并用lookup_val记录j    最终形如lookup_table[i] = j
        for ref_pixel_val in range(len(ref_cdf)):
            if ref_cdf[ref_pixel_val] >= src_cdf[src_pixel_val]:#
                lookup_val = ref_pixel_val
                break
        lookup_table[src_pixel_val] = lookup_val
    return lookup_table
print( calculate_lookup([11,13,15,18],[222,14,110,19]))