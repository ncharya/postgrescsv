data = {"sensors":
        {"-KqYN_VeXCh8CZQFRusI":
            {"bathroom_temp": 16,
             "date": "02/08/2017",
             "fridge_level": 8,
             "kitchen_temp": 18,
             "living_temp": 17,
             "power_bathroom": 0,
             "power_bathroom_value": 0,
             "power_kit_0": 0
        },
        "-KqYPPffaTpft7B72Ow9":
            {"bathroom_temp": 20,
             "date": "02/08/2017",
             "fridge_level": 19,
             "kitchen_temp": 14,
             "living_temp": 20,
             "power_bathroom": 0,
             "power_bathroom_value": 0
        },
        "-KqYPUld3AOve8hnpnOy":
            {"bathroom_temp": 23,
             "date": "02/08/2017",
             "fridge_level": 40,
             "kitchen_temp": 11,
             "living_temp": 10,
             "power_bathroom": 1,
             "power_bathroom_value": 81,
        }
    }
}

kitchen_temp = data["sensors"]["-KqYN_VeXCh8CZQFRusI"]["kitchen_temp"]
print(kitchen_temp)

data1 ={
  "main1": {
    "sub1": {
      "prop1": "name1",
      "prop2": "name2"
    },
    "sub2": {
      "prop1": "name1",
      "prop2": "name2"
    },
  },
  "main2": {
    "sub1": {
      "prop1": "name1",
      "prop2": "name2"
    },
    "sub2": {
      "prop1": "name1",
      "prop2": "name2"
    },
  },
}

for key,item in data1['main1'].items():
  if item['prop1'] == 'name1' or item['prop2'] == 'name1':
    print(item.values)
    print ('found one')