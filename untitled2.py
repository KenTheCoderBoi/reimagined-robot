class parent():
    def __init__():
        print("who's candice?")
    def menu(item):
        if item=="Burger":
            print("Burger:order with a side of candice/dicecans")
        if item=="Among us":
            print("Among us:order with a side of sus/usu")
    def order(item,side):
        if item=="Burger":
            if side=="candice":
                print("your total is 800000000000000 rupees")
            if side=="dicecans":
                print("your total is 80000000 rupees")
        elif item=="Among us":
            if side=="sus":
                print("your total is 9 bitcoin")
            if side=="usu":
                print("your total is 600 NFT tokens")
class menu(parent):
    def __init__(self,item):
        self.menu_dish=item
    def get_item(self):
        parent.menu(self.menu_dish)
class order(parent):
    def __init__(self,menu_dish,addons):
        self.dish=menu_dish
        self.condiments=addons
    def get(self):
        parent.order(self.dish,self.condiments)
test1 = menu("Burger")
test1.get_item()
test2 = order("Burger","candice")
test2.get()