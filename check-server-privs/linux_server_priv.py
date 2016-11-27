from pexpect import pxssh

def ssh_login(hostname, username, password):
    try: 
        ssh = pxssh.pxssh()
        ssh.login(hostname, username, password)
        print("Connecting to "+hostname+" with "+username+"...")
        ssh.sendline('sudo -l')
        ssh.prompt()
        
        print(ssh.before)
        ssh.logout()
        print("Logged out from "+hostname+"...")
    except Exception as error:
        print("SSH failed to login!")
        print(error)


def user_input():
    hostname = input("[+] HOSTNAME: ")
    username = input("[+] USERNAME: ")
    password = input("[+] PASSWORD:" )
    hostnames = hostname.split(",")
    for h in hostnames:
        ssh_login(h, username, password)


def main():
    user_input()


if __name__ == "__main__":
    main()
