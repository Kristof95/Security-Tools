import requests


def site_formatter(site):
    return site if site.startswith("http://") or site.startswith("https://") else "http://"+site


def directory_scanner(url):
    try:
        active_dirs = []
        dirs =  [i.rstrip() for i in open("dirs.txt")]
        
        for i in dirs:
            response = requests.get(site_formatter(url)+i)
            if response.status_code  == 200:
                active_dirs.append(i)
                print("===> DIRECTORY")
                print("[+] "+site_formatter(url)+i)
                save_result_to_file(site_formatter(url)+i)
            else:
                print("[-] "+site_formatter(url)+i)
    except Exception as e:
        print(e)
                
                
def save_result_to_file(dr):
    with open("siteDirs.txt","a") as file:
        file.write(dr+"\n")
        


def main():
    url = input("Please add an URL:")
    directory_scanner(url)


if __name__ == "__main__":
    main()
