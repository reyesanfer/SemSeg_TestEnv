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

RUN git clone -b main https://github.com/SLDGroup/MERIT.git /merit
WORKDIR /merit
RUN pip install h5py
RUN pip install torch==1.11.0+cu113 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install torchvision==0.12.0+cu113 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install --no-cache-dir mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu113/torch1.11/index.html
RUN sed -i '/^torch==/d' requirements.txt
RUN sed -i '/^torchvision==/d' requirements.txt
RUN sed -i '/^mmcv-full==/d' requirements.txt
RUN echo "medpy" >> requirements.txt
RUN echo "h5py" >> requirements.txt
RUN pip install -r requirements.txt
RUN sed -i '1s/^/import time\n/' test_synapse.py
RUN mkdir -p /merit/pretrained_pth/maxvit/
RUN wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1zS9jbgH-a4_5R9Q8csSmEbLh2emGsffE' -O maxxvit_rmlp_small_rw_256_sw-37e217ff.pth
RUN mv maxxvit_rmlp_small_rw_256_sw-37e217ff.pth /merit/pretrained_pth/maxvit/