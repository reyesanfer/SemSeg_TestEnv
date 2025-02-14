ARG PYTORCH="1.11.0"
ARG CUDA="11.3"
ARG CUDNN="8"
ARG MMCV="2.0.1"

FROM pytorch/pytorch:${PYTORCH}-cuda${CUDA}-cudnn${CUDNN}-devel

ENV TORCH_CUDA_ARCH_LIST="6.0 6.1 7.0+PTX"
ENV TORCH_NVCC_FLAGS="-Xfatbin -compress-all"
ENV CMAKE_PREFIX_PATH="$(dirname $(which conda))/../"

RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub

RUN apt-get update && apt-get install -y git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6 libgl1-mesa-dev  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN apt update
RUN apt install -y wget
RUN apt install unzip -y
RUN apt-get install vim -y
RUN apt-get install -y curl
RUN conda clean --all

# Install MMCV
ARG PYTORCH
ARG CUDA
ARG MMCV
RUN ["/bin/bash", "-c", "pip install openmim"]
RUN ["/bin/bash", "-c", "mim install mmengine"]
RUN ["/bin/bash", "-c", "mim install mmcv==${MMCV}"]

# Install MMSegmentation
RUN git clone -b main https://github.com/open-mmlab/mmsegmentation.git /mmsegmentation
WORKDIR /mmsegmentation
ENV FORCE_CUDA="1"
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -e .

# Donwloading some configs 
RUN mkdir -p /mmsegmentation/work_dirs/
RUN mkdir -p /mmsegmentation/work_dirs/vaihingen/
RUN mim download mmsegmentation --config pspnet_r101-d8_4xb4-80k_vaihingen-512x512.py --dest /mmsegmentation/work_dirs/vaihingen/
RUN mkdir -p /mmsegmentation/work_dirs/isaid/
RUN mim download mmsegmentation --config pspnet_r50-d8_4xb4-80k_isaid-896x896 --dest /mmsegmentation/work_dirs/isaid/
RUN mkdir -p /mmsegmentation/work_dirs/cityscapes/
RUN mim download mmsegmentation --config mask2former_swin-b-in22k-384x384-pre_8xb2-90k_cityscapes-512x1024 --dest /mmsegmentation/work_dirs/cityscapes/
RUN mkdir -p /mmsegmentation/work_dirs/ade20k/
RUN mim download mmsegmentation --config mask2former_swin-l-in22k-384x384-pre_8xb2-160k_ade20k-640x640 --dest /mmsegmentation/work_dirs/ade20k/

#Download test data
RUN mkdir -p /mmsegmentation/data/vaihingen/
RUN wget https://zenodo.org/record/5706578/files/Test.zip
RUN unzip Test.zip -d data/postdam
RUN mkdir -p /mmsegmentation/data/isaid/
RUN wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1fwiTNqRRen09E-O9VSpcMV2e6_d4GGVK' -O part1.zip
RUN wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1wTwmxvPVujh1I6mCMreoKURxCUI8f-qv' -O part2.zip
RUN unzip /mmsegmentation/data/ade20k/part1 -d /mmsegmentation/data/isaid/
RUN unzip /mmsegmentation/data/ade20k/part2 -d /mmsegmentation/data/isaid/
RUN mkdir -p /mmsegmentation/data/cityscapes/
# Descargar imagenes sueltas desde https://www.kaggle.com/datasets/sakshaymahna/cityscapes-depth-and-segmentation/data
RUN mkdir -p /mmsegmentation/data/ade20k/
RUN wget http://data.csail.mit.edu/places/ADEchallenge/release_test.zip
RUN unzip release_test.zip -d /mmsegmentation/data/ade20k/
RUN rm *.zip

# Intalling some dependences
RUN pip install mmdet
RUN pip install pycuda
RUN pip install git+https://github.com/cocodataset/panopticapi.git
RUN pip install git+https://github.com/aleju/imgaug.git
RUN pip3 install imagecorruptions
RUN mkdir -p /mmsegmentation/results
COPY inference_demo.py /mmsegmentation/demo/