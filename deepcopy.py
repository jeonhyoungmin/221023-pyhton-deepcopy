import copy # 파이썬에서는 복사를 위한 내장 모듈이 별도로 마련되어있다.
# deep copy
a = [1, 2, 3, 4]
b = copy.deepcopy(a) # 모듈의 메서드로 지원하는 깊은 복사 함수
b.append(5) # 자바스크립트의 .push()와 같은 .append()
print(a == b) # 자바스크립트의 === 일치 비교연산자이다.
print(a)
print(b)
# shallow copy
c = [ "a", "b", "c" ]
d = c # "c"를 가리키는 변수 d는 '같은 메모리 주소'를 가키리고 있다.
# 파이썬에서 지원하는 참조 타입은 종류가 다양하다. 변하는(mutable) 타입과 불변하는(immutable) 타입을 별도로 지원한다.
# 자바스크립트에서도 불변하는 새로운 데이터 타입인 symbol 타입이 유용하게 활용되고 있지만, 직관성면에서는 파이썬이 앞선다.
d.append("d")
print(c == d)
print(c)
print(d)