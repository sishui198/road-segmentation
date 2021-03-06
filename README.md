# Road Extraction from Aerial Images
This repository contains the submission for the student project in the "Computational Intelligence Lab" course at ETH Zürich in spring 2017. The goal of the projects was to find a novel solution to a satellite imagery segmentation problem.

### Authors

* [Florian Chlan](https://github.com/flock0)
* [Samuel Kessler](https://github.com/skezle)
* [Yu-chen Tsai](https://github.com/paramoecium)

### Project Report
Can be found [here](https://github.com/paramoecium/road-segmentation/blob/master/docs/report.pdf)

### Acknowledgements

This repo was cloned from https://github.com/mato93/road-extraction-from-aerial-images.

### Dependencies

* Python 3.5.3+
* Tensorflow 1.1.0
* Numpy
* scikit-learn
* scikit-image
* Pillow
* Matplotlib
* Tqdm
* scipy

### How to run
1. Create the `./data/` directory.
2. Add the unzipped kaggle training and test_set to the `./data/` directory.
3. Run the following commands:
```bash
bash setup.sh
cd src
python3 run.py
```
### Results

The result of running the above will create two submission csv files. submission_cae_patchsize24.csv includes the final results of the median frequency class balancing (MFCB) CNN and the denoising convolutional autoencoder, and the submission_no_postprocessing.csv contains the predictions of the MFCB CNN only.

### Folder Structure

|-- **src** <br>
&ensp;&ensp;|-- **baseline** <br>
&ensp;&ensp;&ensp;&ensp;|-- **model_baseline1.py**: defines the first baseline for the project. Provided by CIL TAs. <br>
&ensp;&ensp;&ensp;&ensp;|-- **model_baseline2.py**: defines the second baseline. Provided by previous group, cloned from [here](https://github.com/mato93/road-extraction-from-aerial-images). <br>
&ensp;&ensp;|-- **constants_baseline2.py**: defines the constants used for second baseline. Provided by previous group, cloned from [here](https://github.com/mato93/road-extraction-from-aerial-images). <br>
&ensp;&ensp;|-- **data_loading_module.py**: helper functions for baseline 2 and CNN with weighted loss. Provided by previous group, cloned from [here](https://github.com/mato93/road-extraction-from-aerial-images). <br>
&ensp;&ensp;|-- **patch_extraction_module.py**: helper functions for baseline 2 and CNN with weighted loss. Provided by previous group, cloned from [here](https://github.com/mato93/road-extraction-from-aerial-images). <br>
&ensp;&ensp;|-- **model_weightedloss.py**: defines the median frequency class balancing CNN. Adapted from [previous group](https://github.com/mato93/road-extraction-from-aerial-images). <br>
&ensp;&ensp;|-- **median_frequency_balancing.py**: helper function for the median frequcny class balancing CNN. <br>
&ensp;&ensp;|-- **constants.py**: config for the median frequency class balancing CNN. <br>
&ensp;&ensp;|-- **autoencoder** <br>
&ensp;&ensp;&ensp;&ensp;|-- **model.py**: defines the model of the autoencoder. <br>
&ensp;&ensp;&ensp;&ensp;|-- **ae_config.py**: defines the constants for the autoencoder. <br>
&ensp;&ensp;&ensp;&ensp;|-- **denoise_autoencoder.py**: runs the autoencoder. <br>
&ensp;&ensp;|-- **cnn_autoencoder** <br>
&ensp;&ensp;&ensp;&ensp;|-- **model.py**: defines the convolutional autoencoder model. <br>
&ensp;&ensp;&ensp;&ensp;|-- **cnn_ae_config.py**: defines the config for the convolutional autoencoder. <br>
&ensp;&ensp;&ensp;&ensp;|-- **denoise_cnn_autoencoder.py**: runs the convolutional autoencoder. <br>
&ensp;&ensp;|-- **mask_to_submission.py**: Converts test images to submission csv file. Provided by CIL TAs. <br>
|-- **notebooks** <br>
&ensp;&ensp; |-- **ImgCorruptionSandbox.ipynb**: Notebook which demonstrates the corruption process for the denoising autoencoders. <br>
