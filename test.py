months="JanFebMarAprMayJunJulAugSepOctNovDec"
n=input("请输入（月分数）：")
pos=(int(n)-1)*3
monthAbbrev=months[pos:pos+3]
print("月份简写是"+monthAbbrev+".")