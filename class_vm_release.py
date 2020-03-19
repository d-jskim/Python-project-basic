"""
* 강의 플랫폼: 인프런 
* 강의명: 프로젝트를 통해 배우는 파이썬 프로그램 

클래스 실습 - 자판기 완성하기
"""

import sys

# 가격은 100원 단위이므로 PRICE_UNIT 상수값을 100으로 선언한다
PRICE_UNIT = 100

class texts:
    title           = "#### 클래스 %s 자판기입니다. ####"
    product         = "%s:%s(%s원)"
    insert_coin      = "동전을 넣어주세요"
    n_enough_coin   = "동전이 부족합니다. \n거스름돈은 %s원입니다."
    select_product  = "원하시는 상품번호를 선택하세요"
    select_fault    = "잘못 누르셨습니다."
    product_out     = "선택하신 %s 입니다. 거스름돈은 %s원입니다. \n감사합니다."   


class Product:
    # 제품 종류, 가격 데이터를 코드 변경 없이 추가하거나 변경할 수 있다.
    
    productType     = {"1" : "설탕커피", "2" : "프림커피", "3" : "원두커피"}
    productValue    = {"1" : "200", "2" : "300", "3" : "400"}


class CoffeeVM(Product):
    _name = "커피"

    def __init__(self):
        # 사용자가 자판기 종류를 선택하면 _name 출력한다
        print(texts.title %self._name)


    def run(self):
        
        while True:
            try: 
                inputCoin = float(input(texts.insert_coin))
            except ValueError:
                # 잘못된 값을 입력받으면 에러 메시지를 출력한다.
                print(tests.select_fault)
            else: #else절은 예외가 발생하지 않아 except가 실행되지 않았을 경우 실행되는 절
                self.selectProduct(inputCoin)


    def selectProduct(self, coin):
        # 제품 종류를 리스트로 선언하여 코드변경 없이 데이터를 동적으로 보여준다.
        description = ''
        for selection, item in Product.productType.items():
            # 제품 가격을 가져온다.
            price = self.getProductValue(selection)
            description += selection + ':' + item + '(' + str(price) + '원)'
        
        print(description)

        inputProduct = input(texts.select_product) #원하는 상품번호
        productValue = self.getProductValue(inputProduct)

        # 입력한 값에 해당하는 내용이 리스트에 없으면 0이 반환된다.
        if productValue:
            productName = self.getProductName(inputProduct)
        #잘못된 값을 입력받으면 에러 메시지를 출력하고 제품선택 메뉴로 이동한다.
        else:
            print(texts.select_fault) # "잘못 누르셨습니다."
            self.selectProduct(coin)

        
    def getProductValue(self, product):
        # product: 원하는 상품번호 inputProduct
        returnValue = 0
        for selection, name in Product.productValue.items():
            print("리스트 확인::::{} : {}".format(selection, name))
            if selection == product:
                returnValue = value
        
        return returnValue


    def getProductName(self, product):
        
        for selection, name in Product.productType.items():
            if selection == product:
                return name

    
    def payment(self, coin, name, value):
        
        coinValue = coin * PRICE_UNIT
        if coinValue >= value:
            balance = coinValue - value
            print(texts.product_out %(name, int(balance)))
        else:
            print(texts.n_enough_coin %int(coinValue))
        #값을 지불한 후 초기 메뉴로 이동한다.
        self.run()
    

vendingMachine = CoffeeVM()
vendingMachine.run()



            



