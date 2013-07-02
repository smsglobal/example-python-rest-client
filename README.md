Python example client for SMS Global REST API
================================

Requirements
--------------------------------
 - Python 2.7.5 or above


Preparation & Compile
--------------------------------
 - Install Python if you haven't :) http://www.python.org/getit/
 - Make sure your user has the right to execute the file SMSGlobalAPIConsumer.py if you intend to run it as a script
~~~
/> chmod u+x SMSGlobalAPIConsumer.py
~~~

Execution
--------------------------------
This file can be run as a python script and accepts 2 arguments and 2 optional options
~~~
/> ./SMSGlobalAPIConsumer.py [-v] [-s] <Key> <Secret>
/> ./SMSGlobalAPIConsumer.py -h
~~~
Usage:
 * \<APIKey\> : String (required) [2]
 * \<Secret\> : String (required) [2]
 * [-v] : turn on or off debugging (optional)
 * [-s] : turn on or off SSL mode (optional) [3]

Notes:
 * [1] Change the first line ```#!/usr/bin/python``` in SMSGlobalAPIConsumer to your local python path
 * [2] Find your \<APIKey\> and \<Secret\> from within MXT at http://mxt.smsglobal.com/api-key.
 * [3] We're disabling SSL Certificate Verification for ease of development and less braincells burned, please consider turn in it back on by commenting out the following line

The result would look like this 

~~~
    ./SMSGlobalAPIConsumer.py -h

    Usage: SMSGlobalAPIConsumer.py [options]

    Options:
      -h, --help     show this help message and exit
      -v, --verbose  Enable extra detail for debugging
      -s, --ssl      Stored using SSL
~~~

~~~
    ./SMSGlobalAPIConsumer.py -v 27a65kff3aec742ddca08e3d918f9ccd 1d27ea091399a98f6c20faf1108c6376


    send: 'GET /v1/balance HTTP/1.1\r\nHost: api.smsglobal.com\r\nAccept-Encoding: identity\r\nAccept: application/json\r\nAuthorization: MAC id="27a657ff3aec742ddca08e3d918f9ccd",ts="1372730113",nonce="bacd7eabff1864491e2071b2d3d6ae5f",mac="U8atdR0odGcTtmr2u7yaSvR7C1L1Qf3LjIZlqRn5MlM="\r\nUser-Agent: SMS Python Client\r\n\r\n'
    reply: 'HTTP/1.1 200 OK\r\n'
    header: Server: nginx
    header: Date: Tue, 02 Jul 2013 01:55:13 GMT
    header: Content-Type: application/json
    header: Content-Length: 107
    header: Connection: keep-alive
    header: Cache-Control: private
    header: X-UA-Compatible: IE=Edge,chrome=1
    header: Set-Cookie: NSC_MC_203.89.193.162=ffffffffc3a00f0e45525d5f4f58455e445a4a423660;expires=Tue, 02-Jul-2013 11:55:13 GMT;path=/;httponly
    {
        "balance": 5.744,
        "costPerMms": 0.38,
        "costPerSms": 0.1,
        "countryCode": "AU",
        "mmsAvailable": 15,
        "smsAvailable": 56
    }
~~~
