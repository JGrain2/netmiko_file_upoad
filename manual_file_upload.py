import netmiko
from netmiko import SCPConn
from getpass import getpass

def transfer_file(net_connect,file):
   net_connect.enable()
   net_connect.config_mode()
  
#Assumes SCP server isn't already enabled
   net_connect.send_command('ip scp server enable')
   scp_conn = SCPConn(net_connect)
  
#Source file - Enter File Path
   s_file = '/x/x/x/x.xx'
  
#Destination file
   d_file = 'flash:/cat3k_caa-universalk9.16.12.10a.SPA.bin'
   scp_conn.scp_transfer_file(s_file, d_file)
  
#Takes SCP server back off the device
   net_connect.send_command('no ip scp server enable')
   net_connect.send_command('show version')
   net_connect.exit_config_mode()
   print('Copy Complete')

#Password input for both password and secret
password = getpass()
username = input()

#Device Type, IP, UN, PW, S
netinfo = {
            'device_type': 'cisco_ios', 
            'ip': 'x.x.x.x', 
            'username': username, 
            'password': password, 
            'secret': password
}

net_connect = netmiko.ConnectHandler(**netinfo) 

print(f'Connecting')

print(f'Now copying')

#File Transfer
transfer_file(net_connect,"cat3k_caa-universalk9.16.12.10a.SPA.bin")
