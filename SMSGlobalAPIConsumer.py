#!/opt/local/bin/python
from optparse import OptionParser
from SMSGlobalAPIWrapper import SMSGlobalAPIWrapper
import json

# Get the options
parser = OptionParser()
parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="Enable extra detail for debugging")
parser.add_option("-s", "--ssl", dest="ssl", action="store_true", default=False, help="Stored using SSL")
(options, args) = parser.parse_args()

# Do it, get the balance
try:
    apiWrapper = SMSGlobalAPIWrapper(args[0], args[1], "http", "api.smsglobal.com", 80, "v1", "", options.verbose, SMSGlobalAPIWrapper.TYPE_JSON)
    balance = json.loads(apiWrapper.get("balance"))
    print json.dumps(balance, sort_keys=True, indent=4, separators=(',', ': '))
except Exception:
    print "There's a problem accessing API"
