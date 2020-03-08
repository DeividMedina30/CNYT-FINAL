# CNYT-FINAL
El proyecto CNYT(Ciencias Naturales y Tecnolía)  es un repositorio creado por Deivid Medina donde ire subiendo diferentes archivos con ejemplos de algoritmos en el lenguaje de programación  Python enfocados a la computación cuantica.

## Funcionalidades
La libreria puede soportar las siguientes operaciones entre numeros complejos.

## Versión N°1: Operaciones Basicas con numeros complejos.
La versión 1 de la librería con el nombre LibreriaComplejos accepta las siguientes operaciones.
1. Suma.
2. Producto.
3. Resta.
4. División.
5. Módulo.
6. Conjugado.
7. Conversion entre representaciones polar y cartesiano.
8. Retornar la fase de un número complejo.
Las siguientes funcionalidades pueden ser probades desde el archivo Test.py

## Versión N°2: Operaciones para vectores y Matrices.
La versión 2 de la librería con el nombre LibreriaComplejo2 accepta las siguientes operaciones.

1. Adición de vectores complejos.
2. Inverso (aditivo) de un vector complejo.
3. Multiplicación de un escalar por un vector complejo.
4. Adición de matrices complejas.
5.  Inversa (aditiva) de una matriz compleja.
6. Multiplicación de un escalar por una matriz compleja.
7. Transpuesta de una matriz/vector
8. Conjugada de una matriz/vector
9. Adjunta (daga) de una matriz/vector
10. Producto de dos matrices (de tamaños compatibles)
11. Función para calcular la "acción" de una matriz sobre un vector.
12. Producto interno de dos vectores
13. Norma de un vector
14. Distancia entre dos vectores
15. Revisar si una matriz es unitaria
16 Revisar si una matriz es Hermitiana
17. Producto tensor de dos matrices/vectores

Las siguientes funcionalidades pueden ser probades desde el archivo Test2.py
Teniendo en cuenta que había un error a la hora de hacer el producto tensor entre matrices. Se sube una nueva version que es LibreriaComplejo3.py y Test3.py.
Al hacer uso de los Test mostrara un resultado como el sigueinte.

![Prueba Test3](https://user-images.githubusercontent.com/59977494/75004845-7a9a7280-543a-11ea-95e5-c5345c585f18.PNG)

## Versión N°3: Competencia de la doble rendija.
La versión N°3 es una simulación del experimento de la doble rendija. Donde podras ver como se comporta en la cuantia el laser y su interpretación en forma de matries.
### Competencia de la doble rendija
                                                 
                                                 
### Presenta
Deivid Sebastián Medina Rativa, Eduardo Ospina Mejía, Diego Macana Naranjo


### Docente
Luis Daniel Benavidez Navarro


### Asignatura
CNYT (Ciencias Naturales y Tecnología)

Colombia ciudad Bogotá D.C. Marzo 02 de 2020

### Experimento de la rendija.

El siguiente experimento se realizó por primera vez, utilizando luz por Thomas Young en 1801, que buscaba demostrar comportamiento ondulatorio de la luz y lo cual termino creando una nueva teoría completamente nueva, relacionada con la física cuántica y que muestra un fenómeno muy difícil de explicar.

### Como funciona:

Muchos explican este experimento como la interferencia entre las ondas que se generan al momento que la onda original pasa por la doble rendija, pero al momento en que se prueba con lanzar soltar de a un electrón a la doble rendija, nunca mandando más de uno a la vez, se vuelve a generar el mismo patrón, como sí se encontrara con algún tipo de interferencia al momento de pasar por las rendijas, la física cuántica explica esto como que el electrón interfiere consigo mismo en múltiples universos, entonces aun así se mande un único electrón se encontrar con interferencia propia y se creara el patrón de interferencia que conocemos y esperamos para este experimento.

### Experimentalmente:
Para realizar el experimento se debe seguir un procedimiento relativamente sencillo:
Lo primero que se debe hacer es diseñar el número de rendijas que se quieran probar, esta puede ser de 1, 2, hasta el número que físicamente uno sea capaz de crear, el resultado en cada una de ellas debería ser muy parecido si no es que el mismo.

Al ya tener las rendijas se crea una maqueta que tenga al fondo una pantalla para apreciar las imágenes que se generen enfrente de la pantalla se coloca la rendija que se quiera probar para el experimento, esta debe ser capaz de cambiar entre las rejillas, y por último, a una distancia que, cuando se prenda el laser cubra completamente las rejillas, se pone el laser para que se genera la imagen en la pantalla.

La dificultad a la hora de desarrollar el experimento es de poder crear las rendijas y que den la imagen que se busca.

### Materiales:

Para el experimento se requieren los siguientes materiales:
      
1. Papel aluminio o hojas blancas para crear las rendijas.
2. Marcador negro.
3. Marcador negro.
4. Marcador negro.

### Desarrollo:

En nuestro caso realizamos el experimento con 3 rendijas diferentes, de 1, 2 y 3 ranuras, y donde se espera que experimentalmente no de igual o muy parecida con cada una de ellas.

### Experimento con 1 rendija.

Para empezar, el primer montaje que se debe realizar es el de una rendija, en donde se busca ver el fenómeno físico que se produce cuando el láser atraviesa, teóricamente se espera:

En donde la dispersión del láser se disminuye, pero la trayectoria se mantiene constante, el primer montaje cuenta de la rendija única y el laser que genera la proyección otra forma de entender el experimento a través de grafos se podría ver de la siguiente manera:

![image](https://user-images.githubusercontent.com/59977494/76165304-e27fd700-6123-11ea-9c1c-9052d647a39a.png)

Y para verlo en forma de matriz se aprecia de la siguiente manera:

![image](https://user-images.githubusercontent.com/59977494/76165375-a7ca6e80-6124-11ea-82b7-0255e633a38f.png)

Esto nos demuestra que hay 100 % de probabilidad que entre por la rendija única y después un 25%  de tocar cualquiera de lo siguientes blancos y cada uno de los receptores es reflexivo consigo mismo.

### Experimento con 2 rendijas.
![image](https://user-images.githubusercontent.com/59977494/76165400-d34d5900-6124-11ea-9008-e04319d66a95.png)

![image](https://user-images.githubusercontent.com/59977494/76165405-dc3e2a80-6124-11ea-932b-5865a371aed2.png)

Una manera de poder entender este experimento en forma de grafos sería la siguiente, suponiendo que tenemos 6 receptores.
![image](https://user-images.githubusercontent.com/59977494/76165416-f0822780-6124-11ea-82a7-db84eb653a16.png)

![image](https://user-images.githubusercontent.com/59977494/76165425-faa42600-6124-11ea-9687-9ec58cf06263.png)

Y si lo quisiéramos ver en forma de una matriz sería de la siguiente manera.

![image](https://user-images.githubusercontent.com/59977494/76165433-10b1e680-6125-11ea-8bba-03dea8be3bc8.png)

Lo cual nos quiere decir que tenemos un 50% de probabilidad de que el rayo láser se vaya por alguna de las dos rendijas. Luego de pasar por alguna de las dos rendijas que vendrían a ser los estados 1 y 2 vemos que hay una probabilidad de 1/6 o 16.66 % de que toque alguno de los receptores.

### Experimento de 3 rendijas:
![image](https://user-images.githubusercontent.com/59977494/76165450-258e7a00-6125-11ea-8657-f365b6bd111f.png)

![image](https://user-images.githubusercontent.com/59977494/76165455-3212d280-6125-11ea-97df-49ee81eafd28.png)

![image](https://user-images.githubusercontent.com/59977494/76165459-3e972b00-6125-11ea-8587-03e0fa9bf9e4.png)

### Video de simulación del experimento.

[![https://youtu.be/omFa72tRSPc](http://img.youtube.com/vi/omFa72tRSPc/0.jpg)](http://www.youtube.com/watch?v=omFa72tRSPc "Experimento rendija")

### Simulación:

Dentro de lo que se esperaba para este experimento se planteó una simulación que representara este fenómeno físico.
Planteamos el programa de la siguiente manera:

![image](https://user-images.githubusercontent.com/59977494/76165587-43101380-6126-11ea-8f74-5a252eca99aa.png)

![image](https://user-images.githubusercontent.com/59977494/76165484-65edf800-6125-11ea-8250-9e40f42f90fa.png)

![image](https://user-images.githubusercontent.com/59977494/76165491-730ae700-6125-11ea-8ef4-d01a7bed6f39.png)

![image](https://user-images.githubusercontent.com/59977494/76165497-7d2ce580-6125-11ea-894e-0fe1e25572a4.png)

Estos 2 programas están diseñados para, el primer de número reales y el segundo para incluir números imaginarios, su funcionamiento es del modo en que comprueba que se puede realizar la operación de la matriz por el estado, si es posible, dependiendo del número de cliks, multiplica el estado por la matriz el numero de veces que se pida y entrega el resultado deseado.
Y la respuesta que da la simulación es para el caso de:

![image](https://user-images.githubusercontent.com/59977494/76165512-9a61b400-6125-11ea-8132-ee24f11a3359.png)

con respuesta:

![image](https://user-images.githubusercontent.com/59977494/76165525-b06f7480-6125-11ea-8df6-da07164eae0d.png)

La otra parte es la de crear la gráfica de probabilidad del estado final de la simulación:

![image](https://user-images.githubusercontent.com/59977494/76165531-c3824480-6125-11ea-96ce-8106bdd94dcb.png)

En donde se ingresa el vector de estado final de la simulación y genera una grafica de barras que lo representa para poder entender mejor el resultado que se busca.

### Como se ejecuta:

primero toca descargar Python para poder tener acceso a IDLE, y poder hacer llamado a la función definida.
Para la ejecución del programa toca tener 3 datos, la matriz inicial del sistema que se quiere, el estado inicial y el número de clicks que se desean operar, se descarga la librería y se abre el IDLE de Python, se ejecuta el programa y se llama a la función y se coloca los parámetros mencionados anteriormente. Este es un ejemplo de como usar el programa definido en la sección anterior y en este momento se coloca para la parte imaginaria.

![image](https://user-images.githubusercontent.com/59977494/76165550-ec0a3e80-6125-11ea-8cbd-36871d40e77a.png)

Esto dará la respuesta a la simulación y el resultado que buscamos encontrar.

![image](https://user-images.githubusercontent.com/59977494/76165552-fa585a80-6125-11ea-97a1-2aa77a93dd39.png)

## ¿Cómo usar la librería de experimento de la doble rendija?

Para poder hacer uso de la libreria del experimento de la doble rendija solo tendremos que descargar el archivo Experimento_CNYT.py el cual se encontrar en el mi guthub, de la misma manera se encontrara el archivo para realizar las respectivas pruebas, el cual se encuentra con nombre (Test de lo clasico a lo cuantico.py).

![image](https://user-images.githubusercontent.com/59977494/76165763-ad758380-6127-11ea-9464-3c7f8114a738.png)

![image](https://user-images.githubusercontent.com/59977494/76165771-bcf4cc80-6127-11ea-8d81-5cfcdde45394.png)

![image](https://user-images.githubusercontent.com/59977494/76165783-c9792500-6127-11ea-9f0b-fcbd025e0f1c.png)

Para poder descargarlo podremos hacerlo de la siguiente manera.
Lo primero que debes realizar es hacer un copia de el repositorio desde (cmd) el cual lo puedes ejecutar buscando desde el buscador de la computadora como cmd.
Despues escribes el siguiente comando git clone https://github.com/DeividMedina30/CNYT-FINAL.git

Cuando ya tengas la carpeta como los archivos clonados podras ejecutar la libreria desde el test (Test de lo clasico a lo cuantico.py).

1. Buscar cmd.

![cmd](https://user-images.githubusercontent.com/59977494/75005159-86d2ff80-543b-11ea-9d10-391a2e045fa9.PNG)

2. Especificar la ruta donde se va a  clonar el repositorio, en este ejemplo sera en el escritorio. Para eso usamos el comando cd y el nombre de la ruta donde queremos ir.

![cmd ruta](https://user-images.githubusercontent.com/59977494/75005307-f943df80-543b-11ea-81ea-9ae97daaa588.PNG)

3. Luego utilizamos el comando git clone y ponemos el siguiente link  https://github.com/DeividMedina30/CNYT-FINAL.git

![git clone](https://user-images.githubusercontent.com/59977494/75005420-622b5780-543c-11ea-9cdf-6d0005f85d03.PNG)

4. Al dirigirnos al escritorio en este caso que fue donde guardamos clonamos el repositorio nos aparecera la carpeta con el nombre del reposit y dentro de ella todos los archivos.

![image](https://user-images.githubusercontent.com/59977494/76165927-d9453900-6128-11ea-9598-1e3f8a45b7bf.png)

![image](https://user-images.githubusercontent.com/59977494/76165934-e8c48200-6128-11ea-84e3-903d5f1230c9.png)


5. A la hora de abrir algun archivo Test , podrea ejecutar dicho archivo ya sea dando F5 o  en Run(Run Module F5).Para finalmente mostrar el resultado de ejecutar dicho Test.

![image](https://user-images.githubusercontent.com/59977494/76165956-13163f80-6129-11ea-8018-790f8437d4e3.png)

![image](https://user-images.githubusercontent.com/59977494/76165984-3a6d0c80-6129-11ea-88d6-f383580b6741.png)

![image](https://user-images.githubusercontent.com/59977494/76166031-67b9ba80-6129-11ea-9c09-8ef4e051a421.png)



## ¿Cómo usar la librería?

### Pasos de descarga y uso de pruebas
Lo primero que debes realizar es hacer un copia de el repositorio desde (cmd) el cual lo puedes ejecutar buscando desde el buscador de la computadora como cmd.
Despues escribes el siguiente comando git clone https://github.com/DeividMedina30/CNYT-FINAL.git

Cuando ya tengas la carpeta como los archivos clonados podras ejecutar la libreria desde los test que son el archivo con nombre Test1.py, Test2.py y Test3.py .

1. Buscar cmd.

![cmd](https://user-images.githubusercontent.com/59977494/75005159-86d2ff80-543b-11ea-9d10-391a2e045fa9.PNG)

2. Especificar la ruta donde se va a  clonar el repositorio, en este ejemplo sera en el escritorio. Para eso usamos el comando cd y el nombre de la ruta donde queremos ir.

![cmd ruta](https://user-images.githubusercontent.com/59977494/75005307-f943df80-543b-11ea-81ea-9ae97daaa588.PNG)

3. Luego utilizamos el comando git clone y ponemos el siguiente link  https://github.com/DeividMedina30/CNYT-FINAL.git

![git clone](https://user-images.githubusercontent.com/59977494/75005420-622b5780-543c-11ea-9cdf-6d0005f85d03.PNG)

4. Al dirigirnos al escritorio en este caso que fue donde guardamos clonamos el repositorio nos aparecera la carpeta con el nombre del reposit y dentro de ella todos los archivos.

![Repositorio](https://user-images.githubusercontent.com/59977494/75005596-f0074280-543c-11ea-850e-13099733bed0.PNG)

![archivos](https://user-images.githubusercontent.com/59977494/75005663-16c57900-543d-11ea-86fe-c415a9f8e75d.PNG)

5. A la hora de abrir algun archivo Test , podrea ejecutar dicho archivo ya sea dando F5 o  en Run(Run Module F5).Para finalmente mostrar el resultado de ejecutar dicho Test.

![Test3](https://user-images.githubusercontent.com/59977494/75005816-994e3880-543d-11ea-951e-3b2ab6de313c.PNG)

![Correr Test](https://user-images.githubusercontent.com/59977494/75005862-c39ff600-543d-11ea-9ca0-537ac87e6d5f.PNG)

![Resultados](https://user-images.githubusercontent.com/59977494/75006055-783a1780-543e-11ea-9d92-7ab43d63c8b4.PNG)

## Desarrollado con
- Python - Lenguaje de Programación

## Autores 

* **Deivid Medina** - *  Trabajo Inicial*
* **Deivid Medina** - * Documentación*

## Expresiones de Gratitud 

* Mi profesor de CNYT  Luis Benavidez
* Compañeros que me guiaron a la hora de subir el proyecto.
* A la personas que estan leyendo este documento.
* Al repositori de Vladimir Correa Arroyave https://github.com/vlacor99/numeros_complejos por ayudarme a enterder el producto tensor

por [Deivid](https://gist.github.com/DeividMedina30)
