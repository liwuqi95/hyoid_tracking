# Hyoid Tracking

Automatic Tracking of Hyoid Bone Displacement and Rotation Relative to Cervical Vertebrae in Videofluoroscopic Swallow
Studies using Deep Learning. [Paper](https://link.springer.com/article/10.1007/s10278-024-01039-4)


This repo contains the inference code of the automatic localization of Inferior Posterior of C2 and C4, and Hyoid Bone
Anterior and Posterior. 

![alt text](https://github.com/liwuqi95/hyoid_tracking/blob/main/static/VFSS_Image.png)

## How to Use

1. Clone this project.
2. Install necessary pip packages.

```commandline
pip install -r requirements.txt
```
3. Download the pretrained weight file from https://drive.google.com/file/d/1qMUqc9sfOt7a9o7Au0_Rnw054qXcdnpM/view?usp=sharing

4. Run the inference code

Example:

```
python main.py --model_path ./weights/fhrnet.pt --data_dir ./source --output_dir ./outputs
```

Parameters:

--model_path 

The path of the pretrained model.

--data_dir 

The folder contains input VFSS Images.

--output_dir 

The folder where the results will be saved.

## Contact
wuqi.li@mail.utoronto.ca

## Citation

If you find this repository useful please give it a star 🌟 or consider citing our work:

```
@ARTICLE{Li2024-ad,
  title     = "Automatic tracking of hyoid bone displacement and rotation
               relative to cervical vertebrae in videofluoroscopic swallow
               studies using deep learning",
  author    = "Li, Wuqi and Mao, Shitong and Mahoney, Amanda S and Coyle, James
               L and Sejdi{\'c}, Ervin",
  journal   = "J Digit Imaging. Inform. med.",
  publisher = "Springer Science and Business Media LLC",
  month     =  feb,
  year      =  2024,
  copyright = "https://www.springernature.com/gp/researchers/text-and-data-mining",
  language  = "en"
}
```