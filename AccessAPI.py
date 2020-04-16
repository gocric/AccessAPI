import requests
import sys

API_KEY = "at_zEVMpyAxxpOhvZy5c62YHZg0GJMky"
output_format = "json"
api_url = "https://api.macaddress.io/v1?apiKey={0}&output={1}&search={2}"
if sys.argv:
    if len(sys.argv) > 1:
        input = sys.argv[1]
        if input:
            response = requests.get(api_url.format(API_KEY,output_format,input))
            if response.status_code != 200:
                print("Error processing the given MAC address")
            else:
                json_data=  response.json()
                if json_data:
                    if "vendorDetails" in json_data:
                        vendorDetails = json_data['vendorDetails']
                        if 'companyName' in vendorDetails:
                            print("The MAC address {0} belongs to {1}".format(input,vendorDetails['companyName']))
    else:
        print("Please enter MAC address value")