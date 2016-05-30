#python34
import requests
import json

def main():
    ip = input("Please add an ip address:")
    print("\n")
    try:
        ip_info = []

        response = requests.get('http://ipinfo.io/'+ip)
        json_resp = json.loads(response.text)
        
        print("Hostname: "+json_resp["hostname"])
        print("Location: "+json_resp["loc"])
        print("IP Address: "+json_resp["ip"])
        print("City: "+json_resp["city"])
        print("Postal: "+json_resp["postal"])
        print("Region: "+json_resp["region"])
        print("Org: "+json_resp["org"])
        print("Country: "+json_resp["country"])
        
        print("\n")
        print("Saved Ip address information to txt file!")
        ip_info.append("Hostname: "+json_resp["hostname"] + "\n" +"Location: "+json_resp["loc"] + "\n" +"IP Address: "+json_resp["ip"]+ "\n" +"City: "+json_resp["city"]+ "\n" +"Postal: "+json_resp["postal"]+ "\n" +"Region: "+json_resp["region"]+ "\n" +"Org: "+json_resp["org"]+ "\n" +"Country: "+json_resp["country"])
    
        save_to_txt(ip_info)    
    except Exception as e:
        print(e.reason)
    


def save_to_txt(info):
    with open("ip_info.txt", "a") as file:
        for i in info:
            file.write(str(i) + "\n")

if __name__ == "__main__":
    main()
