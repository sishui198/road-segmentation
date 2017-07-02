"""
CIL-Road-Segmentation
Matej Hamas, Taivo Pungas, Delio Vicini
Team: DataMinions

This script computes the output for the road segmentation task. If the necessary
are not found cached on the disk, this script automatically trains them
(which can take several hours, depending on machine configuration)


"""
import glob
from masks_to_submission import masks_to_submission
import model_weightedloss as cnn
import postprocessing as pp
from cilutil import resizing

# Train CNN
cnn.main()

# Upsample predictions for both training and test set
UPSAMPLE = True
if UPSAMPLE:
    training_filenames = glob.glob("../results/CNN_Output/training/*/*.png")
    test_filenames = glob.glob("../results/CNN_Output/test/*/*.png")
    resizing.upsample_training(training_filenames)
    resizing.upsample_test(test_filenames)

# Apply post processing to CNN output
pp.generate_output()

# Create submission file for Kaggle from denoised mask
submission_filename = 'submission_cae_ethan_patchsize24.csv'
image_filenames = []
for i in range(1, 51):
    ##image_filename = '../results/CNN_Output/test/high_res_raw/raw_test_' + '%.1d' % i + '_pixels.png' # baseline
    image_filename = '../results/CNN_Autoencoder_Output/test/cnn_ae_test_' + '%.1d' % i + '.png' # cae
    print(image_filename)
    image_filenames.append(image_filename)
masks_to_submission(submission_filename, *image_filenames)
