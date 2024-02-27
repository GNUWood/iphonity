import requests
import re
from bs4 import BeautifulSoup

request_header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; rv:121.0) Gecko/20100101 Firefox/121.0"
}

def as_info(ASN):
    if not ASN == re.search("^AS|^as", ASN):
        try:
            req = requests.get(f"https://ipinfo.io/{ASN}",headers=request_header)
        
        except:
            print("iphonity: Failed to get ASN INFO.")
            return
        
        soup = BeautifulSoup(req.text, "html.parser")
        
        table = soup.find("div", {"class":"card card-details mt-0"})
        asname = table.find("h2").get_text()

        table = soup.find("tbody")

        summary = []
        for i in table.find_all("td"):
            summary.append(re.sub(r"[\r\n]|\s{2,}",'', i.text))

        result = {
            "org":asname,
            "country":summary[1],
            "website":summary[3],
            "hosted_domains":summary[5],
            "numipv4":summary[7],
            "numipv6":summary[9],
            "asn_type":summary[11],
            "registry":summary[13],
            "allocated":summary[15],
            "updated":summary[17]
        }

        return result
    
    else:
        print("iphonity: Invalid ASN.")
        return
    

def ip_range(ASN):
    if re.search(r"^AS|^as", ASN):
        try:
            req = requests.get(f"https://ipinfo.io/{ASN}",headers=request_header)
        
        except:
            print("iphonity: Failed to get IP list.")
            return

        soup = BeautifulSoup(req.text, "html.parser")
        ips = soup.select("#ipv4-data > table > tbody > tr > td > a")

        ip = []
        for elem in ips:
            ip.append(elem.contents[0])

        return ip
    
    else:
        print("iphonity: Invalid ASN.")    
        return


def ip_info(ip):
    if re.search(r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$", ip):
        try:
            req = requests.get(f"https://ipinfo.io/{ip}",headers=request_header)
        
        except:
            print("iphonity: Failed to get IP info.")
            return
        
        soup = BeautifulSoup(req.text, "html.parser")
        table = soup.find("tbody")

        summary = []
        for i in table.find_all("td"):
            summary.append(re.sub(r"[\r\n]|\s{2,}",'', i.text))

        result = {
            "asn":summary[1],
            "hostname":summary[3],
            "range":summary[5],
            "company":summary[7],
            "hosted_domains":summary[9],
            "privacy":summary[11],
            "anycast":summary[13],
            "asn_type":summary[15],
            "abuse_contact":summary[17]
        }

        return result
    
    else:
        ("iphonity: Invalid IP.")
        return
    

def locate(ip):
    if re.search(r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$", ip):
        try:
            req = requests.get(f"https://ipinfo.io/{ip}",headers=request_header)
        
        except:
            print("iphonity: Failed to get IP info.")
            return
        
        soup = BeautifulSoup(req.text, "html.parser")
        table = soup.find("table", {"class": "table table-borderless table-xs geo-table"})

        summary = []
        for i in table.find_all("td"):
            summary.append(re.sub(r"[\r\n]|\s{2,}",'', i.text))

        result = {
            "city":summary[1],
            "state":summary[3],
            "country":summary[5],
            "postal":summary[7],
            "local_time":summary[9],
            "timezone":summary[11],
            "coordinates":summary[13],
        }

        return result
    
    else:
        ("iphonity: Invalid IP.")
        return