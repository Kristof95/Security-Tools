import requests
from datetime import datetime
from sys import argv
import os


def url_parser(host):
    if not host.startswith("http://"):
        http_url = "http://" + host
        if not http_url.endswith("/"):
            ready_url = http_url + "/"
            return ready_url
    else:
        return host


def explore_directories(url):
    try:
        with open(argv[2], "r") as word_list:
            for i in word_list.readlines():
                req = requests.get(url + i.replace("\n", ""), None)
                resp = req.status_code
                if resp == 200:
                    print("[+] " + str(req.url))
    except KeyboardInterrupt as e:
        print(e)


def main():
    os.system("cls")
    welcome()
    try:
        parsed_url = url_parser(argv[1])
        print("URL: "+parsed_url + "\nStart scanning...")
        start = datetime.now()
        explore_directories(parsed_url)
        end = datetime.now()
        print("\n")
        print("Elapsed time:"+str(end-start))
    except IndexError:
        print("\n")
        print("You must add two argument!")
        print("\n")
    except requests.exceptions.ConnectionError:
        print("\n")
        print("Failed to establish this request!")
        print("\n")


def welcome():
    welcome_text = """
                    .
                  .'|       .-.          .-
                 <  |        \ \        / /
            __    | |         \ \      / /  __
         .:--.'.  | | .'''-.   \ \    / /.:--.'.
        / |   \ | | |/.'''. \   \ \  / // |   \ |
        `" __ | | |  /    | |    \ `  / `" __ | |
         .'.''| | | |     | |     \  /   .'.''| |
        / /   | |_| |     | |     / /   / /   | |_
        \ \._,\ '/| '.    | '.|`-' /    \ \._,\ '/
         `--'  `" '---'   '---''..'      `--'  `"
                    Release date: 2016.08.04

It is a security tool, you can explore the directories of an url.
Usage: python dirb.py 127.0.0.1 wordlist.txt
    """
    print(welcome_text)


if __name__ == "__main__":
    main()