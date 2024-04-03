from subprocess import Popen
import platform, smtplib

date = hora = datetime.datetime.now() 
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

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
  







