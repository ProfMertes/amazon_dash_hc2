# amazon_dash_hc2
Hacked amazon dash buttons connected to fibaro hc2

 1. adapt hc2_dash.py:
		 change
* {HC2_IP}
* {SCENE_ID}
* {USER}
* {PASSWORD}
* {TH:IS:TH:EM:AC:XX}
and multiply on demand
 2. docker build -t amzn_dash_hc2 .
 
 3. docker run **--net host** -d amzn_dash_hc2
