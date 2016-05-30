import urllib.request
import webbrowser
site = [line.strip() for line in open('sites.txt')]

add_inf = input("Search:~# ")
print()
splitted = add_inf.split(";")
save = open("dox.txt","a")
for w in site:
    url_string = w
    for v in splitted:  
        req = urllib.request.Request(url_string+v)
        try:
            urllib.request.urlopen(req)
            print("Target:~# "+url_string+v)
            save.write(str(url_string+v)+"\n")
        except urllib.error.URLError as e:
            pass
        except KeyboardInterrupt as k:
            print(k.reason)
save.close()
