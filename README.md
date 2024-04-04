# pytest

`[-]` Pytest es una libraría simple de Python para realizar pruebas de penetración con Python desde cualquier sistema operativo.

`[-]` Instalación en `Linux:` 

    pip3 install pytest
`[-]` Instalación en `Windows:`

    pip install pytest

#### 🏁 FUNCIONALIDADES 🏁

`[-]` Atención: para importar todos los módulos de Pytest, es necesario escribir el siguiente código:

```python
from pytest import *  # Se importan todos los módulos de pytest
```

`[-]` Se puede iniciar un proceso en tu `sistema`. En este caso, el `bloc` de notas de `Windows:`

```python
from pytest import start_process  # Se importa el módulo requerido de pytest

start_process('notepad.exe')
```

`[-]` También se puede `obtener información del sistema` con las siguientes `funciones:`

```python
from pytest import get_processor_name, get_processor_info, get_system, get_ip, get_hostname, get_date  # Se importan todos los módulos necesarios

get_processor_name()  # Para obtenerel tipo de procesador
get_processor_info()  # Para obtener información del procesador
get_system()  # Para obtener el nombre del sistema
get_ ip()  # Para obtener nuestra IP
get_hostname()  # Para obtener nuestro nombre de usuario
get_date()  # Para obtener la fecha actual
```
