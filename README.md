# M2_AI_project
Repositorio proyecto modulo 2 Inteligencia Artificial


## Selección del set de datos 
El proyecto se trata de reconocimiento de símbolos matemáticos escritos a mano usando machine learning.

El dataset original consta de alredor de 10,000 imagenes de 19 clases diferentes de simbolos matematicos (numeros del 0 al 9, punto decimal, +, -, /, *, =, x, y, z). 

Dataset original: https://www.kaggle.com/datasets/sagyamthapa/handwritten-math-symbols

Se programó un script (splitDataset.py) para crear las carpetas y hacer la separación de los sets de prueba y entrenamiento, este script dividió las imagenes del dataset aleatoriamente en 80% para train, y 20% para test.

## Preprocesado de los datos
Se programó dataAugmentation.ipynb para hacer data augmentation en las clases de train y test con el fin de balancear el dataset.  Primero se recorren train y test para encontrar la clase con mayor numero de imagenes (mayor numero en train y en test respectivamente). Una vez hecho esto se generan imagenes en cada una de las clases que tengan menos imagenes que la clase encontrada en el paso anterior. Así al teminar de correr el script todas las clases  train tienen el mismo numero de imagenes, y todas las clases en test tienen el mismo numero de imagenes (el dataset esta dividido aproximadente en 80% train y 20% test).
Tras hacer este data augmentation y balanceo el numero de imágenes del dataset ascendió a alrededor de 12,000 en total.

Para la generación de imágenes se configuró ImageDataGenerator de tal manera que las nuevas imagenes generadas solamente tuvieran variacion en el brillo y en el zoom ya que al trabajar con simbolos matematicos al girar o cambiar la posicion de la imagen se afecta la calidad de datos debido a que haciendo tal giro o cambio de posición se podria obtener un simbolo diferente al de la clase, lo cual ensuciaria los datos de tal clase.

## Implementación de Modelo 
Como modelo inicial se seleccionó Support Vector Machine (SVM) ya que es la técnica de reconocimiento más dominante en el área de Modelos de machine learning para el reconocimiento de símbolos matemáticos [1]. 

El framework seleccionado para la implementación del modelo es tensorflow ya que es un framework ampliamente adoptado y bien respaldado que proporciona un amplio conjunto de features para implementar y entrenar modelos de machine learning.

Se implementó un Support Vector Machine (SVM) classifier usando el kernel linear.

El modelo implementado utiliza un Support Vector Machine (SVM) classifier con un kernel linear para reconocer símbolos matemáticos escritos a mano. Se utiliza TensorFlow para el preprocesamiento y la carga de datos, mientras que la biblioteca sklearn proporciona el modelo SVM y las métricas de evaluación.

## Evaluación inicial del modelo
Se seleccionó accuracy como métrica ya que la tasa de reconocimiento de símbolos (accuracy) es la métrica que más frecuentemente se utiliza en modelos de este tipo [1].

El modelo logró un accuracy de 51% al reconocer los simbolos de los samples de test.
Al observar los resultados del modelo podemos ver que el rendimiento varía según las diferentes clases. Algunas clases, como "dec" (decimal), "div" (división), "eq" (igualdad), "mul" (multiplicación) y "sub" (resta) tienen una accuracy, recall y F1-score relativamente más altas. Por otro lado, clases como "x", "y" y "z" tienen puntajes más bajos, lo que indica que el modelo tuvo problemas para clasificar estos símbolos con precisión.

## Refinamiento del modelo 
Considerando que el dataset fue balanceado y que la calidad y el tamaño de las imagenes proporcionadas al modelo fueron los adecuados, el rendimiento del modelo se puede atribuir al uso del kernel linear para el clasificador ya que este asume que las clases pueden estar separadas por un límite de decisión lineal sin embargo, en el contexto de los símbolos matemáticos escritos a mano, es posible que algunos símbolos tengan patrones más complejos, lo que los hace menos separables linealmente. Esto puede resultar en una menor precisión. Además, El kernel lineal solo puede aprender límites de decisión lineales, mientras que algunos símbolos matemáticos pueden requerir límites de decisión más complejos para clasificarse con precisión, esto podría resultar en un rendimiento menor para ciertas clases que son no lineales.

Considerando estos factores y que el clasificador SVM con kernel linear tuvo problemas para lograr una mayor precisión y rendimiento en la tarea de reconocimiento de símbolos matemáticos escritos a mano se decidió explorar con un modelo CNN ya que es una arquitectura mas compleja lo cual lo puede hacer más apta para problemas como este, además, CNNs son los métodos más utilizados después de SVM [1].

La primer implementación del modelo CNN (cnnmodel.ipynb) consiste de una capa convolucional seguida de una capa flatten para procesar la entrada de la imagen. Luego, hay dos capas densas para una mayor extracción y clasificación de características. El modelo se entrena usando categorical cross-entropy loss y se optimiza usando RMSprop con una baja tasa de aprendizaje.

Con este modelo se logró un accuracy de 61% al reconocer los simbolos de los samples de test.
No obstante, según los resultados, el modelo parece tener overfitting en los datos de training, ya que logra una precisión del 100% en el set de training pero una precisión menor en el set de test. Puede ser que el modelo haya memorizado los data samples de test en lugar de aprender características generalizables. 
Por ende, para mejorar el rendimiento del modelo, se utilizaron técnicas de regularización además del ajuste de la arquitectura y los hiperparámetros del modelo.

En la segunda implementación del modelo CNN (cnnmodelReg.ipynb) se agregaron más capas convolucionales con max pooling, se introdujo regularización dropout y se cambió el optimizador y loss function. Estas modificaciones tienen como objetivo mejorar la capacidad del modelo para aprender y generalizar a partir de los datos de training, lo que podría conducir a un mejor rendimiento.

Este nuevo modelo logró un accuracy de 92% l reconocer los simbolos de los samples de test.
Con base los resultados, el modelo muestra un buen desempeño. Logra una alta accuracy en el set de training y un accuracy relativamente alta en el set de test. Esto indica que el modelo ha aprendido representaciones significativas y puede generalizar bien a datos no conocidos. Además, observando el classification report se ve que la mayoría de las clases tienen puntajes de accuracy, recall y F1-score altos, lo que indica un buen desempeño. 

Por lo tanto, el modelo que resultó ser más adecuado ya que ofrece varias ventajas, incluida su capacidad para aprender características complejas,
mayor capacidad del modelo por su arquitectura más compleja, regularización dropout, y en general su mayor capacidad para obtener características relevantes de las imágenes como parte de su proceso de training.


1. Kukreja, V., Sakshi Machine learning models for mathematical symbol recognition: A stem to stern literature analysis. Multimed Tools Appl 81, 28651–28687 (2022). https://doi.org/10.1007/s11042-022-12644-2