from optparse import OptionParser
from SMSGlobalAPIWrapper import SMSGlobalAPIWrapper

# Get the options
parser = OptionParser()
parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="Enable extra detail for debugging")
parser.add_option("-s", "--ssl", dest="ssl", action="store_true", default=False, help="Stored using SSL")

(options, args) = parser.parse_args()
apiWrapper = SMSGlobalAPIWrapper(args[0], args[1], "http", "api.smsglobal.com", 80, "v1", "", options.verbose)
print apiWrapper.get("balance")

