
# ¿Que es la segmentación semántica?




## Despliegue

Primero debemos crear la imagen de docker haciendo uso del `Dockerfile` que se encuentra en la carpeta `MMSegmentation`
```bash
docker build -t mmsegmentation .\MMSegmentation\
```
Una vez se ha creado la imagen correctamente podemos crear un contenedor de docker usando esa imagen. La ruta del `bind-mount` nos permite tener una ruta compartida entre el `host` y el `contenedor` para visualizar los resultados facilmente
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

[]()

### Referencias

[MMSegmentation](https://github.com/open-mmlab/mmsegmentation/tree/main)

[The Beginner’s Guide to Semantic Segmentation](https://www.v7labs.com/blog/semantic-segmentation-guide)

[The Ultimate Guide to Medical Image Annotation](https://www.v7labs.com/blog/medical-image-annotation-guide)
## Autores

- [@reyesanfer](https://github.com/reyesanfer)

