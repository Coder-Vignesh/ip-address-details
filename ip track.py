import requests,argparse,json

if __name__ =="__main__":
  parse =argparse.ArgumentParser()
  parse.add_argument("-i","--ipaddress",help="IP Address To Track")
  args =parse.parse_args()
  ip =args.ipaddress
  url ="http://ip-api.com/json/"+args.ipaddress
  req =requests.get(url)
  res =json.loads(req.content)
  print("[+] IP\t\t\t",res["query"])
  print("[+] City\t\t",res["city"])
  print("[+] Cont\t\t",res["country"])
  print("[+] ISP\t\t\t",res["isp"])
  print("[+] ZIP\t\t\t",res["zip"])
  print("[+] Tim\t\t\t",res["timezone"])
  print("[+] LAT\t\t\t",res["lat"])
  print("[+] LON\t\t\t",res["lon"])
  

