import json
import urllib

# Virustotal API call
# https://github.com/guelfoweb/knock/blob/4.1/knockpy/modules/virustotal_subdomains.py

def virustotal_api(domain, apikey):
	url = 'https://www.virustotal.com/vtapi/v2/domain/report'
	parameters = {'domain': domain, 'apikey': apikey}
	
	try:
		response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
		response_dict = json.loads(response)
		return response_dict['subdomains']

	except:
		return False