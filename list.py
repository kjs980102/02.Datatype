fruits=["사과","바나나","딸기"]
print(fruits,type(fruits))

jinsu=["김진수","27","010-4559-1866"]
name=jinsu[0]
age=jinsu[1]
phone=jinsu[-1]
print(jinsu,type(jinsu))
print(name)
print(age)
print(phone)

names=[['강수경', '강혜나','김민석'],['20','21','22'],['010-0000-0000','010-1111-1111','010-2222-2222']]
print(names[0][0:2])

numbers=[1,2,3,4,5]
c=numbers[2]+numbers[-1]
print(c)

print(len(numbers))
print(len(names[0]))

#리스트에 요소 추가하기
last=[1,2,3]
last.append(30)
print(last)
last.remove(3)
print(last)
print(type(last))
