철수가가진돈=[13,200,13]
환율표={"달러":1320, "엔":950, "위안":182}
a=(철수가가진돈[0]*환율표["달러"])
b=(철수가가진돈[1]*환율표["엔"])
c=(철수가가진돈[-1]*환율표["위안"])
d=(a+b+c)
print(type(철수가가진돈))
print("철수가 가지고 있는 돈의 원화 가치는",d,"원 입니다.")

