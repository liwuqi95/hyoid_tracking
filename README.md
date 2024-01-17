# Hyoid_Tracking

Automatic Tracking of Hyoid Bone Displacement and Rotation Relative to Cervical Vertebrae in Videofluoroscopic Swallow
Studies using Deep Learning

This repo contains the inference code of the automatic localization of Inferior Posterior of C2 and C4, and Hyoid Bone
Anterior and Posterior.

## How to Use

1. Clone this project
2. Install necessary pip packages.

```commandline
pip install -r requirements.txt
```
3. Download the pretrained weight file from https://drive.google.com/file/d/1qMUqc9sfOt7a9o7Au0_Rnw054qXcdnpM/view?usp=sharing
4. Move the weight into ./weights folder

5. Run the inference code

Example:

```
python main.py --model_path ./weights/fhrnet.pt --data_dir ./source --output_dir ./outputs
```

--model_path The path of the pretrained model

--data_dir The folder contains VFSS Images

--output_dir The results folder

