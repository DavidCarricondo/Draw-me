# Draw-me

*   **Descripción de proyecto:**

Reemplazar en una imagen la cara, mano o pies por un dibujo a mano alzada (o con una gui tipo paint)

Primero, con un dataset de dibujos simples de objetos, entrenaría un red neuronal para reconocer dibujos de caras, manos, pies...
Después entrenaría otra red multi-label para reconocer caras manos, pies de una imagen real. La aplicación substituiría, por ejemplo, la cara de la imagen real por la cara dibujada..

Niveles:

    l1: Clasificación de dibujos (igual solo caras al principio)
    l2: Reconocimiento de cara, manos, pies en una imagen (empezar con caras)
    l3: Substituir lo reconocido en l2 por un dibujo clasificado en l1
    l4: Crear una gui con dos ventanas, una tipo paint, otra con la imagen input y que el modelo lo cambie de forma automática.
    l5. Que la imagen real sea video de la webcam
    l6. Introducir reconocimiento de pies, manos, etc..
    l4: Montar una app en la nube
Datos:

Dibujos dataset : https://github.com/googlecreativelab/quickdraw-dataset

*   **Tecnología**

Para la clasificación de dibujos: Red neuronal propia multi label (reduciendo el numero de labels del data set original a tres o cuatro clases)

Para el reconocimiento de caras: VGGFace2 de keras (https://machinelearningmastery.com/how-to-perform-face-recognition-with-vggface2-convolutional-neural-network-in-keras/)

Para face swapping: https://life-in-a-monospace-typeface.tumblr.com/post/28495219189/quick-and-dirty-automatic-face-replacement-with



Para la gui: tkinker and PIL (https://www.youtube.com/watch?v=OdDCsxfI8S0, https://www.youtube.com/watch?v=rhvJ_M218EQ)