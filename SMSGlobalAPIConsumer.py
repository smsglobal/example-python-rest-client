#!/usr/bin/python

from optparse import OptionParser
import SMSGlobalAPI
import json

# Get the options
parser = OptionParser()
parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="Enable extra detail for debugging")
parser.add_option("-s", "--ssl", dest="ssl", action="store_true", default=False, help="Stored using SSL")
(options, args) = parser.parse_args()

# Do it, get the balance

apiWrapper = SMSGlobalAPI.Wrapper(args[0], args[1], "http", "api.smsglobal.com", 80, "v1", "", options.verbose, SMSGlobalAPI.Wrapper.TYPE_JSON)
groups = json.loads(apiWrapper.get("group"))
print json.dumps(groups, sort_keys=True, indent=4, separators=(',', ': '))

