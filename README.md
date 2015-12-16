# Palo Alto Networks (PAN) Firewall Custom URL Category
---

`pan_custom_url.py` makes firewall administrator life easier by automating the URL category process.

#### Custom URL Categories
***Objects > Custom URL Categories***

> The custom URL categories feature allows you to create your own lists of URLs that can be selected in any URL filtering profile. Each custom category can be controlled independently and will have an action associated with it in each URL filtering profile (allow, block, continue, override, or alert).

### Usage
---

**Minimal**

`python pan_custom_url.py -i ipaddroffirewall -u username -p password -c abc -s www.xyz.com`

**All Options**

```
Usage: python pan_custom_url.py [-h] -i IP -u USER -p PASSWORD -c CATEGORY [-s SURL] [-f FILE]

optional arguments:
  -h, --help            				show this help message and exit
  -i IP, --ip IP        				IP address of firewall
  -u USER, --user USER  				Username to login firewall
  -p PASSWORD, --password PASSWORD 		Password to login firewall
  -c CATEGORY, --category CATEGORY 		Custom URL category name
  -s SURL, --surl SURL  				Single URL
  -f FILE, --file FILE  				List of URL's file
```

**Credit**

Madhu Akula - [http://www.madhuakula.com](http://www.madhuakula.com)

Tamaghna Basu - [http://www.tbasu.com](http://www.tbasu.com)

### References
---

[https://live.paloaltonetworks.com/docs/DOC-1500](https://live.paloaltonetworks.com/docs/DOC-1500)
