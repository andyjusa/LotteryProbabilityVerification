import urllib.request, json 
import matplotlib.pyplot as plt
import numpy as np

result = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="
# print(result.count())
x = np.arange(46)
plt.bar(x, result)
plt.xticks(x, range(0,46))

plt.show()
for i in range(1,1000):
    with urllib.request.urlopen(url+str(i)) as rl:
        da = json.load(rl)
        print(i)
    result[int(da["drwtNo1"])]+=1
    result[int(da["drwtNo2"])]+=1
    result[int(da["drwtNo3"])]+=1
    result[int(da["drwtNo4"])]+=1
    result[int(da["drwtNo5"])]+=1
    result[int(da["drwtNo6"])]+=1
    result[int(da["bnusNo"])]+=1
print(result)
x = np.arange(46)
plt.bar(x, result)
plt.xticks(x, range(0,46))

plt.show()
