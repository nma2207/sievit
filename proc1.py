#encoding: utf-8
from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyABQaMw6rEeQZoPOI9Aqf_FsnUfyA41n0M"
my_cse_id = "nma2207"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=my_api_key)
    res = service.cse().list(q=search_term, cx=my_cse_id, **kwargs).execute()
    return res['items']

def main():
    listM = google_search(
        'music', my_api_key, my_cse_id, num=8)
    for k,v in listM.items():
        print(k,":", v)

if __name__=="__main__":
    main()
