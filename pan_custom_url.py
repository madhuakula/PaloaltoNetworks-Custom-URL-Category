#!/usr/bin/python
# PAN Custom URL Category Script by Madhu Akula - http://www.madhuakula.com
import sys
import httplib
import argparse
import logging
import re

logging.basicConfig(filename="output.log", level=logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s")

def make_parser():
	"""Constructin the command line parser and return args"""
	logging.info("Constructing Parser")
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--ip',required=True,help="IP address of firewall")
	parser.add_argument('-u','--user',required=True,help="Username to login firewall")
	parser.add_argument('-p','--password',required=True,help="Password to login firewall")
	parser.add_argument('-c','--category',required=True,help="Custom URL category name")
	parser.add_argument('-s','--surl',required=False,help="Single URL")
	parser.add_argument('-f','--file',required=False,help="List of URL's file")
	arguments=parser.parse_args()
	# To print arguments
	arguments=vars(arguments) 
	return arguments

def key_grab(ip,user,password):    
        """Take in input IP Address, uname and password and retrieve API key from firewall"""
        logging.debug("In API key gen routine")
        conn = httplib.HTTPSConnection(ip)
        try:
                conn.request("GET", "/api/?type=keygen&user=" + user + "&password=" + password)
        except IOError:
                print "Unable to get the device's API key as the connection was refused. Please check connectivity."
                logging.debug("Error occured when trying to retrieve API key")
                raise SystemExit(1)
        r1 = conn.getresponse()
        data1 = r1.read()
        m = re.search(r"(<key>)(\w+)", data1)
        try:
                api_key = m.group(2)
        except AttributeError:
                print "No API key was returned, possibly incorrect credentials given?"
                logging.debug("Possible insufficient/incorrect attributes")
                conn.close()
                raise SystemExit(1)
        conn.close()
        return api_key

def isNotEmpty(s):
    return bool(s and s.strip());

def send_request(ip, url_to_be_filtered, http_method, api_key):
	conn = httplib.HTTPSConnection(ip)
	try:
		url_server = "/api/?type=config&key=" + api_key + "&action=set&xpath=/config/devices/entry/vsys/entry[@name='vsys1']/profiles/custom-url-category/entry[@name='" + custom_category + "']/list&element=<member>" + str(url_to_be_filtered).rstrip() + "</member>";
		conn.request(http_method, url_server);
	except IOError:
	        print "Connection was refused. Please check connectivity."
	        logging.debug("Error occured when trying to send block request")
	        raise SystemExit(1)
	r1 = conn.getresponse()
	data1 = r1.read()
	print "############# RESPONSE RECEIVED ################"
	print data1;
	conn.close()	

def main():
	logging.debug("Starting main Function")
	parser=make_parser()
	ip_address = parser['ip'];
	user_name = parser['user'];
	password = parser['password'];
	single_url = parser['surl'];
	file_name = parser['file'];
	custom_category = parser['category']


	print "############# Generating API Key ################"
	api_key=key_grab(ip_address,user_name,password);
	# print apikey;

	if(file_name != None ):
		if('\\' in file_name or '/' in file_name):
			print ('\n Please only provide filename, paths are not supported here');
			sys.exit(1);
		f = open(file_name);
		for line in f:
			if(isNotEmpty(line)):
				print "############# SENDING URL BLOCK REQUEST FOR - " + str(line).rstrip() + " ################"
				send_request(ip_address, str(line).rstrip(), "GET", api_key);
		f.close();
	
	if(isNotEmpty(single_url)):
		print "############# SENDING URL BLOCK REQUEST FOR - " + str(single_url).rstrip() + " ################"
		send_request(ip_address, str(single_url).rstrip(), "GET", api_key);
	
if __name__ == '__main__':
	main();
