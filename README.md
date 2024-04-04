# pytest

`[-]` Pytest es una libraría simple de Python para realizar pruebas de penetración con Python desde cualquier sistema operativo.

`[-]` Instalación en `Linux:` 

```shell
pip3 install pytest
```

`[-]` Instalación en `Windows:`

```shell
pip install pytest
```

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
`[-]` Para ver si un `email y una contraseña` son válidos para `loggearse,` se puede hacer de la siguiente manera:

```python
from pytest import smtp_login  # Importamos el módulo necesario

smtp_login('soyelpatodonald@loquesea.com', 'contrseña')  # Indicamos el usuario y la contraseña
```

`[-]` Para intentar `realizar un ataque ssh` a una determinada `IP,` ejecutad el siguiente código:

```python
from pytest import brute_ssh  # Importamos el módulo necesario

brute_ssh('127.0.1.1', 'kali', '1234')  # Se indica la IP, el nombre de usuario y la contraseña
```

`[-]` Este código `verifica` si un determinado `puerto` de una `IP` está abierto:

```python
from pytest import test_port  # Importamos el módulo necesario

test_port('127.0.1.1', '8080')  # Se incluye la IP y el puerto a escanear
```

`[-]` Para enviar una `mensaje a Discord` a través de un `Webhook,` se utiliza el siguiente código:

```python
from pytest import discord_send_message  # Importamos el módulo necesario

discord_send_message('https://www.discord.webhook.com', 'hello')  # Se indican tanto la URL del Webhook como el mensaje a enviar 
```

`[-]` El siguiente código `muestra` si una `IP es válida` y existe o no:

```python
from pytest import validate_ip  # Importamos el módulo necesario

validate_ip('127.0.1.1')  # Se indica la IP a validar
```

`[-]` Para realizar un pequeño `ataque dos con Python,` ejecutad el siguiente código:

```python
from pytest import dos_attack  # Importamos el módulo necesario

dos_attack('127.0.1.1', '8080')  # Se espacifican tanto la IP por el puerto por el que realizar el ataque
```








