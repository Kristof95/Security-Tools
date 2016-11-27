import paramiko

def ssh_login(host, user, pwd):
    try:
        port = 22
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, user, pwd)
        print("Connecting to "+host+"...\n")
        stdin, stdout, stderr = ssh.exec_command("service --status-all | grep \"+\"")
        stdin.write(pwd+"\n")
        stdin.flush()
        outlines = stdout.readlines()
        response = ''.join(outlines)
        print("Output:\n"+response)
        ssh.close()
        print("Connection closed!\n")
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        print(e)
    except TimeoutError as err:
        print(err)


def usr_input():
    host = input("[+] HOSTNAME: ")
    if host == "":
        default()
    user = input("[+] USERNAME: ")
    pwd = input("[+] PASSWORD: ")
    hosts = host.split(",")
    for h in hosts:
        ssh_login(h, user, pwd)

def default():
    print("The script will be use the default credentials.")
    ssh_login("192.168.0.104", "devops", "king")
    exit(0)

if __name__ == "__main__":
    usr_input()
