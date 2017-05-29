# amazon_dash_hc2
Hacked amazon dash buttons connected to fibaro hc2

- adapt hc2_dash.py (change: {HC2_IP}, {SCENE_ID}, {USER}, {PASSWORD}, {TH:IS:TH:EM:AC:XX}' and multiply on demand)
- docker build -t amzn_dash_hc2 .
- docker run --net host -d amzn_dash_hc2
