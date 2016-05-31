import re
import urllib.request
import urllib

def site_formatter(site):
    return site if site.startswith("http://") or site.startswith("https://") else "http://"+site

def main():
    try:
        URL = input("Please add an URL:")
        print("-"*60)
        print("\n")
        url_open = urllib.request.urlopen(site_formatter(URL))
        print("Collect links from "+site_formatter(URL).upper() +" content...")
        content = url_open.read()
        urls = re.findall(r'href=[\'"]?([^\'" >]+)', content.decode('ISO-8859-1','strict'))
        print('\n'.join(urls))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
