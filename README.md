# GraphProject🚀
 Data Structure 2021-1 Ucaldas

## Proyecto

_La montaña “Acme” tiene una serie de cuevas conectadas por diferentes rutas, como se muestra en el siguiente ejemplo:_

![CuevaAcme](https://user-images.githubusercontent.com/49491301/124370224-958a1300-dc3a-11eb-9724-05f5be364e37.png)

_Como se puede observar cada una de las cuevas están conectadas por un camino donde se puede observar la distancia entre ellas, el centro de recursos dispone de los diferentes insumos para las cuevas (martillos, hachas, palas, picas, agua, etc..). Este centro de recursos se encarga de suministrar a toda la red de cuevas, los recursos que requieran mediante sus camiones de reparto_

## Comenzando 🚀
_Se desea simular todo el sistema, teniendo en cuenta:_

### 1. Cargar la red inicial.
* de cuevas que se muestra en la gráfica, mediante un archivo XML, TXT o JSON.
* El sistema debe permitir la creación de nuevas cuevas y conectarlas a la red.
* El sistema debe dar la opción de la conexión a la red (dirigida o No dirigida).
* El sistema debe verificar si la red de cuevas está fuertemente conectada o no.
* El sistema debe verificar si en la red de cuevas, hay cuevas que no tiene conexiones a otras cuevas(Pozos).
* El sistema debe mostrar por cueva, cuantas conexiones entrantes y salientes tiene (grado de los vértices).

### 2. Como la montaña es muy inestable, en ciertas ocasiones algunos caminos se van a encontrar obstruidos.
* El sistema debe permitir obstruir uno o varios caminos.
* El sistema debe ofrecer la posibilidad de cambiar el sentido de cualquier ruta de cuevas.
* El sistema debe simular la ruta de los camiones, partiendo desde un origen recorrer todas las cuevas realizando la entrega de los diferentes insumos. por exigencias del centro de recursos debe contar con los dos tipos de recorridos básicos(Anchura y profundidad).
* Si al cambiar la dirección de las conexiones en las cuevas, alguna cueva queda inaccesible, el sistema debe listar las cuevas a las que no pudo llegar. Además de brindar una posible solución.

### 3. Por consideraciones del ingeniero del centro de centro de recursos el sistema debe permitir, realizar los siguientes recorridos.
* El sistema debe permitir visualizar, en la red de cuevas cual son las rutas o acceso a las cuevas mínimas para visitar toda la red, obtenido inicialmente la conexión menor” Árbol de expansión mínimo”.
* El sistema debe permitir visualizar, en la red de cuevas cual son las rutas o acceso a las cuevas mínimas para visitar toda la red, partiendo desde una cueva en específico” Árbol de expansión mínimo”.
* El sistema debe permitir visualizar, en la red de cuevas cual son las rutas o acceso a las cuevas mínimas para visitar toda la red, partiendo en el orden de las cuevas creadas” Árbol de expansión mínimo”.

### 4. Por último, el sistema debe contemplar lo siguiente.
* Tener una interfaz grafica en phyton, que simule todo el sistema y que muestre el recorrido de los camiones, cuando se realice un recorrido tradicional.
* Tener una interfaz grafica en phyton, que simule todo el sistema y que muestre el recorrido de los camiones, cuando se realice un recorrido del punto ( 3 ).
* Realizar el recorrido de menor distancia desde una cueva “origen” a una cueva “destino”.

## Criterios de Evaluación:
* Calidad y elegancia del código de la aplicación. Uso adecuado de la orientación a objetos. Gestión de errores adecuada.
* Patrón MVC, o mínimamente a 2 capas.
* Facilidad de uso de la aplicación y presentación adecuada de la información en las distintas vistas.
* No olvidar que la tecnología debe ser phyton.
Por último, la correcta implementación de alguna función avanzada te permitirá obtener 0.5 décimas más. Si el profesor considera especialmente meritoria tu implementación de una función avanzada, esta podría compensar parcialmente la puntuación perdida por algunos errores en la implementación de la funcionalidad o si no implementas alguna de las funciones, cubrir la puntuación perdida por no hacerlo. 
Durante la entrevista, cada grupo compilará el código de su aplicación, mostrará al profesor su funcionamiento. Es necesario que el día de la entrevista cada grupo disponga de suficientes datos cargados para poder probar la aplicación. Un estudiante elegido por el profesor realizará la sustentación (creación o validación de un componente nuevo o existente) del proyecto y esa será la nota del grupo.



## Construido con 🛠️
* **Python**
* **Pygame**
* **Pycharm**


## Autores ✒️
_Todos aquellos que ayudaron a levantar el proyecto desde sus inicios_
