# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy


class BaseSpider(scrapy.Spider):
    name = 'base'
    states = {'AL': {'name': 'Alabama', 'long': '-86.90229799999997', 'lat': '32.3182314'},
              'AK': {'name': 'Alaska', 'long': '-149.4936733', 'lat': '64.2008413'},
              'AS': {'name': 'American Samoa', 'long': '', 'lat': ''},
              'AZ': {'name': 'Arizona', 'long': '-111.09373110000001', 'lat': '34.0489281'},
              'AR': {'name': 'Arkansas', 'long': '-91.8318334', 'lat': '35.20105'},
              'CA': {'name': 'California', 'long': '-119.41793239999998', 'lat': '36.778261'},
              'CO': {'name': 'Colorado', 'long': '-105.78206740000002', 'lat': '39.5500507'},
              'CT': {'name': 'Connecticut', 'long': '-73.08774900000003', 'lat': '41.6032207'},
              'DE': {'name': 'Delaware', 'long': '-75.52766989999998', 'lat': '38.9108325'},
              'DC': {'name': 'District Of Columbia', 'long': '-77.03687070000001', 'lat': '38.9071923'},
              'FM': {'name': 'Federated States Of Micronesia', 'long': '150.55081199999995', 'lat': '7.425554'},
              'FL': {'name': 'Florida', 'long': '-81.51575350000002', 'lat': '27.6648274'},
              'GA': {'name': 'Georgia', 'long': '-82.90007509999998', 'lat': '32.1656221'},
              'GU': {'name': 'Guam', 'long': '144.79373099999998', 'lat': '13.444304'},
              'HI': {'name': 'Hawaii', 'long': '-155.58278180000002', 'lat': '19.8967662'},
              'ID': {'name': 'Idaho', 'long': '-114.74204079999998', 'lat': '44.0682019'},
              'IL': {'name': 'Illinois', 'long': '-89.39852830000001', 'lat': '40.6331249'},
              'IN': {'name': 'Indiana', 'long': '-86.13490189999999', 'lat': '40.2671941'},
              'IA': {'name': 'Iowa', 'long': '-93.09770200000003', 'lat': '41.8780025'},
              'KS': {'name': 'Kansas', 'long': '-98.48424649999998', 'lat': '39.011902'},
              'KY': {'name': 'Kentucky', 'long': '-84.27001789999997', 'lat': '37.8393332'},
              'LA': {'name': 'Louisiana', 'long': '-91.96233269999999', 'lat': '30.9842977'},
              'ME': {'name': 'Maine', 'long': '-69.44546889999998', 'lat': '45.253783'},
              'MH': {'name': 'Marshall Islands', 'long': '171.184478', 'lat': '7.131474'},
              'MD': {'name': 'Maryland', 'long': '-76.6412712', 'lat': '39.0457549'},
              'MA': {'name': 'Massachusetts', 'long': '-71.38243740000001', 'lat': '42.4072107'},
              'MI': {'name': 'Michigan', 'long': '-85.60236429999998', 'lat': '44.3148443'},
              'MN': {'name': 'Minnesota', 'long': '-94.68589980000002', 'lat': '46.729553'},
              'MS': {'name': 'Mississippi', 'long': '-89.39852830000001', 'lat': '32.3546679'},
              'MO': {'name': 'Missouri', 'long': '-91.8318334', 'lat': '37.9642529'},
              'MT': {'name': 'Montana', 'long': '-110.36256579999997', 'lat': '46.8796822'},
              'NE': {'name': 'Nebraska', 'long': '-99.90181310000003', 'lat': '41.4925374'},
              'NV': {'name': 'Nevada', 'long': '-116.41938900000002', 'lat': '38.8026097'},
              'NH': {'name': 'New Hampshire', 'long': '-71.57239529999998', 'lat': '43.1938516'},
              'NJ': {'name': 'New Jersey', 'long': '-74.4056612', 'lat': '40.0583238'},
              'NM': {'name': 'New Mexico', 'long': '-105.87009009999997', 'lat': '34.5199402'},
              'NY': {'name': 'New York', 'long': '-74.0059728', 'lat': '40.7127753'},
              'NC': {'name': 'North Carolina', 'long': '-79.01929969999998', 'lat': '35.7595731'},
              'ND': {'name': 'North Dakota', 'long': '-101.00201190000001', 'lat': '47.5514926'},
              'MP': {'name': 'Northern Mariana Islands', 'long': '145.6739', 'lat': '15.0979'},
              'OH': {'name': 'Ohio', 'long': '-82.90712300000001', 'lat': '40.4172871'},
              'OK': {'name': 'Oklahoma', 'long': '-97.09287699999999', 'lat': '35.0077519'},
              'OR': {'name': 'Oregon', 'long': '-120.55420119999997', 'lat': '43.8041334'},
              'PW': {'name': 'Palau', 'long': '134.58251999999993', 'lat': '7.514979999999999'},
              'PA': {'name': 'Pennsylvania', 'long': '-77.19452469999999', 'lat': '41.2033216'},
              'PR': {'name': 'Puerto Rico', 'long': '-66.590149', 'lat': '18.220833'},
              'RI': {'name': 'Rhode Island', 'long': '-71.4774291', 'lat': '41.5800945'},
              'SC': {'name': 'South Carolina', 'long': '-81.1637245', 'lat': '33.836081'},
              'SD': {'name': 'South Dakota', 'long': '-99.90181310000003', 'lat': '43.9695148'},
              'TN': {'name': 'Tennessee', 'long': '-86.5804473', 'lat': '35.5174913'},
              'TX': {'name': 'Texas', 'long': '-99.90181310000003', 'lat': '31.9685988'},
              'UT': {'name': 'Utah', 'long': '-111.09373110000001', 'lat': '39.3209801'},
              'VT': {'name': 'Vermont', 'long': '-72.57784149999998', 'lat': '44.5588028'},
              'VI': {'name': 'Virgin Islands', 'long': '-64.89633500000002', 'lat': '18.335765'},
              'VA': {'name': 'Virginia', 'long': '-78.65689420000001', 'lat': '37.4315734'},
              'WA': {'name': 'Washington', 'long': '-120.7401385', 'lat': '47.7510741'},
              'WV': {'name': 'West Virginia', 'long': '-80.45490259999997', 'lat': '38.5976262'},
              'WI': {'name': 'Wisconsin', 'long': '-88.78786780000001', 'lat': '43.7844397'},
              'WY': {'name': 'Wyoming', 'long': '-107.29028390000002', 'lat': '43.0759678'},
              }