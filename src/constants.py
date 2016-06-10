# CONSTANTS THAT ARE COMMON TO MULTIPLE SOURCE FILES
IMG_WIDTH = 400
IMG_HEIGHT = 400
IMG_PATCH_SIZE = 16
IMG_CONTEXT_SIZE = 32
IMG_BORDER_SIZE = int((IMG_CONTEXT_SIZE - IMG_PATCH_SIZE) / 2)
IMG_PATCH_STRIDE = 16
IMG_PATCH_HIGH_RES_SIZE = 4

PATCHES_MEAN_PATH = "../objects/patches_mean"

# post processing
DICT_PATCH_SIZE = (5, 5)
LOW_RANK_TARGET = 3 # desired rank of output