import json
import digitalocean
import requests

with open('../deploy/harbor.json') as f:
	secrets = json.loads(f.read())

token = secrets['token']
domain = secrets['domain']
record_id = secrets['record_id']
record = digitalocean.Record(domain_name=domain, token=token)
ip_address = requests.get('https://api.ipify.org/').text

r = record.get_object(token, domain, record_id)
r.data = ip_address
r.save()