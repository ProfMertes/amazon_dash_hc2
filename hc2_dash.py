import logging
import urllib2
import base64
import requests

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from time import gmtime, strftime

def button_pressed_dash1():
  current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print 'SOMAT button pressed at ' + current_time
  request = urllib2.Request('http://{HC2_IP}:80/api/sceneControl?id={SCENE_ID}&action=start')
  base64string = base64.encodestring('%s:%s' % ("{USER}", "{PASSWORD}")).replace('\n', '')
  request.add_header("Authorization", "Basic %s" % base64string)
  result = urllib2.urlopen(request)

def button_pressed_dash2():
  current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print 'NERF button pressed at ' + current_time
  request = urllib2.Request("http://{HC2_IP}::80/api/sceneControl?id={SCENE_ID}&action=start")
  base64string = base64.encodestring('%s:%s' % ("{USER}", "{PASSWORD}")).replace('\n', '')
  request.add_header("Authorization", "Basic %s" % base64string)
  result = urllib2.urlopen(request)

def udp_filter(pkt):
  options = pkt[DHCP].options
  for option in options:
    if isinstance(option, tuple):
     if 'requested_addr' in option:
       # we've found the IP address, which means its the second and final UDP request, so we can trigger our action
       mac_to_action[pkt.src]()
       break

mac_to_action = {'{TH:IS:TH:EM:AC:XX}' : button_pressed_dash1,
                 '{TH:IS:TH:EM:AC:XX} : button_pressed_dash2}
mac_id_list = list(mac_to_action.keys())

print "Waiting for a button press..."
sniff(prn=udp_filter, store=0, filter="udp", lfilter=lambda d: d.src in mac_id_list)

if __name__ == "__main__":
  main()