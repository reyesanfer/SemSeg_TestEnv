# ¿Que es la segmentación semántica?

La segmentación semántica es una técnica que permite asignar una etiqueta o categoría a cada píxel de una imagen, lo que permite crear regiones dentro de la imagen y atribuir un significado semántico a cada una de ellas.

Por ejemplo, en una imagen de un paisaje, la segmentación semántica puede colorear los píxeles de los árboles de un color, los de los ríos de otro, y los de las nubes de otro color más.

Esta técnica es muy utilizada en aplicaciones como la conducción autónoma, donde los vehículos necesitan identificar objetos como vehículos, peatones, señales de tráfico y aceras.
También se emplea en aplicaciones médicas para ayudar a los médicos a analizar imágenes de pacientes y realizar diagnósticos.

## Despliegue

### Ejecución con Google Colab
- Nootebook sobre métodos clásicos [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/reyesanfer/SemSeg_TestEnv/blob/main/tecnicas_clasicas/tecnicas_clasicas_segmentacion.ipynb)
- Nootebook sobre métodos de Deep Learning [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/reyesanfer/SemSeg_TestEnv/blob/main/deep_learning/modelos_de_deep_learning.ipynb)

<h3>Entorno con Docker <img src="https://static-00.iconduck.com/assets.00/docker-icon-2048x2048-5mc7mvtn.png" style="width: 1em; height: 1em; vertical-align: middle;"></h3>

Primero debemos crear la imagen de docker haciendo uso del `Dockerfile` que se encuentra en la carpeta `MMSegmentation`
```bash
docker build -t mmsegmentation .\MMSegmentation\
```
Una vez se ha creado la imagen correctamente podemos crear un contenedor de docker usando esa imagen. La ruta del `bind-mount` nos permite tener una carpeta compartida entre el `host` y el `contenedor` para visualizar los resultados facilmente
```bash
docker run -d --gpus all --shm-size=8g -it -v [bind-mount-route-for-results]:/mmsegmentation/results --name [container-name] [image-name]
```
Con el contenedor ya creado podemos acceder a el con el comando `attach` o arrancarlo con `start` en caso de que estuviera parado
```bash
docker attach [id-contenedor] o docker start -ai [id-contenedor]
```
## Uso/Ejemplos

Con el contenedor ya en funcionamiento se pueden realizar pruebas de inferencia con imágenes usando este script de python
```bash
python -W ignore demo/inference_demo.py [images_folder] [config_file] [checkpoint] [out_folder_name] --with-labels [boolean_value]
```
Ejemplo:
```bash
python -W ignore demo/inference_demo.py data/ade20k/ work_dirs/ade20k/mask2former...py [checkpoint] [out_folder_name] --with-labels [boolean_value]
```


## Referencias

### Enlaces de interés

- [Segmentación de imágen médica](https://huggingface.co/spaces/kbressem/MRSegmentator)
- [Segmentador para conducción autónoma](https://huggingface.co/spaces/Rohit8y/Semantic-Segmentation)
- [Segmentador selectivo](https://huggingface.co/spaces/SkalskiP/florence-sam)
- [Entorno de pruebas multimodal](https://huggingface.co/spaces/shi-labs/OneFormer)
- [SAM Demo](https://segment-anything.com/demo)
- [Entorno multi proposito](https://huggingface.co/spaces/EPFL-VILAB/4M)

### Referencias

- [MMSegmentation](https://github.com/open-mmlab/mmsegmentation/tree/main)

- [The Beginner’s Guide to Semantic Segmentation](https://www.v7labs.com/blog/semantic-segmentation-guide)

- [The Ultimate Guide to Medical Image Annotation](https://www.v7labs.com/blog/medical-image-annotation-guide)
## Autores

- [Fernando Sanfiel Reyes](https://github.com/reyesanfer)

