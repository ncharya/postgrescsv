import os

lts_dict =[{}, {'surveyid':'char','ipadd':'109.90.10.10'}, {'surveyid':'char','ipadd':'109.90.10.10'}, {'surveyid':'char1','ipadd':'100.90.10.10'}, 
           {}, {'surveyid':'char2','ipadd':'109.90.10.11'} ]
res = [i for n, i in enumerate(lts_dict) if i not in lts_dict[:n]]
#method 2
mres = []
for i in lts_dict:
    if i not in mres:
        mres.append(i)
while {} in mres:
    mres.remove({})
print(str(res))
print(str(mres))