# load predicting model
from sklearn.cluster import k_means # necessary for loading the pickled model
import pandas as pd
import pickle
import warnings

warnings.filterwarnings("ignore")

with open("../res_model/kmeans_cluster_10_10_ingredient.pkl", 'rb') as pkl:
    clf = pickle.load(pkl)


# ShoppingCart物件
class ShoppingCart:
    """
    # static member variables
    cols = ["Pepper" ,"Egg" , "Salt", "Oil", "Soy sauce", "Onion", "Sugar", "Cream", "Flour", "Meat"]

    把拿到的 shopping_cart_raw_data 轉成模型要吃的格式

    進來的資料格式
    {"Line_userID": {"material_name":[quantity, unit_price, subtotal, material_model_order], # [int]
                     "material_name":[quantity, unit_price, subtotal, material_model_order],
                     "material_name":[quantity, unit_price, subtotal, material_model_order],
                     "material_name":[quantity, unit_price, subtotal, material_model_order],
                     "material_name":[quantity, unit_price, subtotal, material_model_order],
                     "material_name":[quantity, unit_price, subtotal, material_model_order],
                     "material_name":[quantity, unit_price, subtotal, material_model_order],
                     "material_name":[quantity, unit_price, subtotal, material_model_order],
                     "material_name":[quantity, unit_price, subtotal, material_model_order],
                     "material_name":[quantity, unit_price, subtotal, material_model_order]
                    }
    }

    # shopping_cart_raw_data EXAMPLE:

    # shopping_cart_raw_data = {"Line_userID": {"Cream":[2, 100, 0, 8], # [int]
                                                "Egg":[1, 50, 0, 2],
                                                "Flour":[1, 50, 0, 9],
                                                "Meat":[2, 90, 0, 10],
                                                "Oil":[0, 150, 0, 4],
                                                "Onion":[4, 75, 0, 6],
                                                "Pepper":[3, 40, 0, 1],
                                                "Salt":[0, 30, 0, 3],
                                                "Soy sauce":[0, 170, 0, 5],
                                                "Sugar":[3, 120, 0, 7]
                                                }
                                }

    使用方法:

    sc = ShoppingCart(shopping_cart_raw_data=input_data,model=clf)
    sc.makePredictionForm().predict()

    或

    sc = ShoppingCart(shopping_cart_raw_data=input_data,model=clf)
    sc.makePredictionForm()
    sc.predict()

    """

    cols = ["Pepper", "Egg", "Salt", "Oil", "Soy sauce", "Onion", "Sugar", "Cream", "Flour", "Meat"]

    def __init__(self, shopping_cart_raw_data={"line_user_id": {"material_name": [0, 0, 0, 0]}}, model=None):
        self.shopping_cart_raw_data = shopping_cart_raw_data
        self.shopping_cart_list = []
        self.one_hot_encoding_list = [0 for i in range(10)]
        self.model = model
        self.pred = None

    def __toShoppingCartList(self):
        for line_user_id in self.shopping_cart_raw_data:
            for key in self.shopping_cart_raw_data[line_user_id]:
                decode_list = self.shopping_cart_raw_data[line_user_id].get(key)
                if decode_list[0] > 0:
                    for i in range(decode_list[0]):
                        self.shopping_cart_list.append(key)
        return self

    def __toOneHotEncoding(self):
        for num, item in enumerate(ShoppingCart.cols):
            if item in self.shopping_cart_list:
                self.one_hot_encoding_list[num] = 1
        return self

    # pandas.DataFrame(two_dimension_array, columns=columns)
    # 第一個參數必須給二維陣列，若給一維陣列(list)，會變成 1 column * n rows 的 DataFrame
    def __toDataFrame(self):
        self.DataFrame = pd.DataFrame([self.one_hot_encoding_list], columns=ShoppingCart.cols)
        return self

    def makePredictionForm(self):
        self.__toShoppingCartList().__toOneHotEncoding().__toDataFrame()
        return self

    def predict(self):
        self.pred = self.model.predict(self.DataFrame)
        return self.pred


if __name__ == "__main__":
    test_shopping_cart_raw_data = {"Line_userID": {"Cream": [2, 100, 0, 8],  # [int]
                                                   "Egg": [1, 50, 0, 2],
                                                   "Flour": [1, 50, 0, 9],
                                                   "Meat": [2, 90, 0, 10],
                                                   "Oil": [0, 150, 0, 4],
                                                   "Onion": [4, 75, 0, 6],
                                                   "Pepper": [3, 40, 0, 1],
                                                   "Salt": [0, 30, 0, 3],
                                                   "Soy sauce": [0, 170, 0, 5],
                                                   "Sugar": [3, 120, 0, 7]
                                                   }
                                   }
    sc = ShoppingCart(shopping_cart_raw_data=test_shopping_cart_raw_data,
                      model=clf)
    sc.makePredictionForm().predict()
    print("The recipe type prediction is {} to the test input: \n===============\n {}".format(sc.pred, sc.DataFrame))
