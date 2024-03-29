from requests import get
import ipinfo
import requests

def ip_address(): #Subprogram to obtain the users IP address
  ip = get('https://api.ipify.org').text
  return ip

def ip_location(ip): #Subprogram to find the location linked to the users IP
  access_token = 'abe318631b66d7'
  handler = ipinfo.getHandler(access_token)
  details = handler.getDetails(ip)
  print(details.loc)
  location = details.loc
  city = details.city
  print(city)
  return location

def weather(location): #Subprogram to query the weather API.
  params = {
    'access_key': '63d3a62502dd2f601a7850aea8ff8259',
    'query': location
  }

  api_result = requests.get('http://api.weatherstack.com/current', params) #Processes the JSON file
  api_response = api_result.json()
  print(api_result)
  print(api_response['current']['temperature'])
  return api_response['current']['temperature']

  #alternative API key: 470079b4af413c15752a14605b899fde
  
  
  

