#Can be imported from local file/folder
import paramiko

def get_files (hostname_filled, ip_filled, username_filled, password_filled,ssh_client):
    ssh_client.connect(hostname=hostname_filled,username=username_filled,password=password_filled)
     #For retrieving file list
     #file_in_folder = ssh_client.exec_command ('ls')
     #Transfer files, Path as an example
    ftp_client=ssh_client.open_sftp()
    #PAth as an example
    ftp_client.get('/home/alex/Documents/archive.tar','/tmp/1.tar')
    ftp_client.close()
def main ():
    ssh_client =paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #As example
    #Can use a list, then use for when calling function
    Mega_Server = {'hostname':'localhost','ip':'127.0.0.1', 'username':'alex','password':'alex'}
    get_file_from_Mega_Server = get_files(Mega_Server['hostname'],Mega_Server['ip'],Mega_Server['username'],Mega_Server['password'],ssh_client)

main()



"""
MEGA = {}



for net_device in (MEGA, NUR, BEELINE):
    file_system = net_device.pop('file_system')

    # Create the Netmiko SSH connection
    ssh_conn = ConnectHandler(**net_device)
    transfer_dict = file_transfer(ssh_conn,
                                  source_file=source_file, 
                                  dest_file=dest_file,
                                  file_system=file_system, 
                                  direction=direction,
                                  overwrite_file=True)
   transfer_dict = file_transfer(ssh_conn,
                                  source_file=source_file, 
                                  dest_file=dest_file,
                                  file_system=file_system, 
                                  direction=direction,
                                  overwrite_file=True)
"""