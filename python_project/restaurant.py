import datetime


class Dish:

    def __init__(
        self,
        dish_id,
        name,
        price,
        image,
        category
    ):

        if price <= 0:
            raise ValueError("Price must be greater than 0")

        if price > 10000:
            print("Price is unusually high, please confirm input")

        if not image:
            raise ValueError("Dish must have an image")

        if not category:
            raise ValueError("Dish must have a category")

        self.__dish_id = dish_id
        self.__name = name
        self.__price = price
        self.__image = image
        self.__category = category

        self.__monthly_sales = 0

    def get_dish_id(self):
        return self.__dish_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_category(self):
        return self.__category

    def get_monthly_sales(self):
        return self.__monthly_sales

    def increase_sales(self, quantity):

        if quantity > 0:
            self.__monthly_sales += quantity


class StarRating:

    @staticmethod
    def select_star(star):

        allowed = [1, 2, 3, 4, 5]

        if star not in allowed:
            raise ValueError("Rating must be between 1 and 5 stars")

        return star



class Review:

    def __init__(
        self,
        user_id,
        food_rating,
        packaging_rating,
        taste_rating,
        service_rating,
        hygiene_rating,
        aftersale_rating,
        comment,
        images=None
    ):

        self.__food_rating = StarRating.select_star(food_rating)
        self.__packaging_rating = StarRating.select_star(packaging_rating)
        self.__taste_rating = StarRating.select_star(taste_rating)
        self.__service_rating = StarRating.select_star(service_rating)
        self.__hygiene_rating = StarRating.select_star(hygiene_rating)
        self.__aftersale_rating = StarRating.select_star(aftersale_rating)

        self.__user_id = user_id
        self.__comment = comment

        self.__images = images if images else []

        self.__time = datetime.datetime.now()

        self.__likes = 0
        self.__replies = []

        self.__merchant_reply = None

    def get_user_id(self):
        return self.__user_id

    def get_average_rating(self):

        return (

            self.__food_rating +
            self.__packaging_rating +
            self.__taste_rating +
            self.__service_rating +
            self.__hygiene_rating +
            self.__aftersale_rating

        ) / 6

    def add_like(self):
        self.__likes += 1

    def add_reply(self, reply_text):
        self.__replies.append(reply_text)

    def add_merchant_reply(self, reply_text):
        self.__merchant_reply = reply_text

    def display_review(self):

        print("Content:", self.__comment)
        print("Time:", self.__time)
        print("Likes:", self.__likes)

        if self.__merchant_reply:
            print("Merchant reply:", self.__merchant_reply)


class Restaurant:

    def __init__(
        self,
        restaurant_id,
        name,
        address,
        store_image,
        dining_image,
        kitchen_image,
        license_image,
        business_hours
    ):

        self.__restaurant_id = restaurant_id
        self.__name = name
        self.__address = address

        if not store_image:
            raise ValueError("Store image is required")

        if not dining_image:
            raise ValueError("Dining area image is required")

        if not kitchen_image:
            raise ValueError("Kitchen image is required")

        if not license_image:
            raise ValueError("Business license image is required")

        self.__store_image = store_image
        self.__dining_image = dining_image
        self.__kitchen_image = kitchen_image
        self.__license_image = license_image

        self.__business_hours = business_hours

        self.__menu_by_category = {}

        self.__dishes = []

        self.__received_orders = []

        self.__reviews = []

        self.__customers_who_ordered = set()

        self.__rating = 0.0

        self.__delivery_radius = 2.0



    def add_category(self, category_name):

        if not category_name.strip():
            print("Category name cannot be empty")
            return

        if category_name not in self.__menu_by_category:

            self.__menu_by_category[category_name] = []

            print(f"Category {category_name} created successfully")

        else:

            print("Category already exists")


    def display_categories(self):

        print("\nCurrent Categories:")

        for c in sorted(self.__menu_by_category):
            print("-", c)


    def add_dish(self, dish):

        for d in self.__dishes:

            if d.get_dish_id() == dish.get_dish_id():

                print("Dish ID already exists")

                return

        category = dish.get_category()

        if category not in self.__menu_by_category:

            print(f"Category {category} does not exist")

            return

        self.__dishes.append(dish)

        self.__menu_by_category[category].append(dish)

        print(f"Dish {dish.get_name()} added successfully")


    def remove_dish(self, dish_id):

        for dish in self.__dishes:

            if dish.get_dish_id() == dish_id:

                self.__dishes.remove(dish)

                category = dish.get_category()

                self.__menu_by_category[category].remove(dish)

                print("Dish removed successfully")

                return

        print("Dish not found")


    def get_dish_by_id(self, dish_id):

        for dish in self.__dishes:

            if dish.get_dish_id() == dish_id:

                return dish

        return None


    def display_menu(self):

        print(f"\n{self.__name} Menu:")

        for category in sorted(self.__menu_by_category):

            print(f"\n{category}")

            dishes = sorted(
                self.__menu_by_category[category],
                key=lambda d: d.get_name()
            )

            for dish in dishes:

                print(

                    dish.get_name(),
                    "HK$",
                    dish.get_price(),
                    "| Monthly sales:",
                    dish.get_monthly_sales()

                )


    def update_dish_sales(self, dish_id, quantity):

        if quantity <= 0:
            print("Quantity must be greater than 0")
            return

        dish = self.get_dish_by_id(dish_id)

        if dish:

            dish.increase_sales(quantity)

            print(f"{dish.get_name()} sales +{quantity}")

        else:

            print("Dish not found")



    def receive_order(self, order):

        self.__received_orders.append(order)

        user_id = order.get_user_id()

        self.__customers_who_ordered.add(user_id)

        order.update_status("Order received by restaurant")


    def add_review(self, review):

        user_id = review.get_user_id()

        if user_id not in self.__customers_who_ordered:

            print("Only customers who placed orders can leave reviews")

            return

        self.__reviews.append(review)

        self.__update_rating()

        print("Review added successfully")


    def __update_rating(self):

        if len(self.__reviews) == 0:

            self.__rating = 0

            return

        total = 0

        for review in self.__reviews:

            total += review.get_average_rating()

        self.__rating = round(total / len(self.__reviews), 1)


    def get_rating(self):

        return self.__rating
    
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__restaurant_id
    @staticmethod
    def load_menu(file_name, restaurant_objects):

        try:
            with open("restaurant_data/" + file_name, "r") as f:

                for line in f:

                    data = line.strip().split(";")

                    if len(data) != 5:
                        print("Invalid menu data:", line)
                        continue

                    restaurant_id = int(data[0])

                    dish = Dish(
                      int(data[1]),
                        data[2],
                        float(data[3]),
                        "default.jpg",
                        data[4]
                    )
   
                    for r in restaurant_objects:

                        if r.get_id() == restaurant_id:

                            if data[4] not in r._Restaurant__menu_by_category:
                                r.add_category(data[4])

                            r.add_dish(dish)

                            break

        except FileNotFoundError:
            print("Menu file not found")

    @staticmethod
    def load_restaurants(file_name):

        restaurant_objects = []

        try:
            with open(file_name, "r") as f:

                for line in f:

                    data = line.strip().split(";")

                    if len(data) != 8:
                        print("Invalid restaurant data:", line)
                        continue

                    r = Restaurant(
                        int(data[0]),
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                        data[6],
                        data[7]
                    ) 

                    restaurant_objects.append(r)

        except FileNotFoundError:
            print("Restaurant file not found")

        return restaurant_objects

    @staticmethod
    def save_restaurants(file_name, restaurant_objects):

        with open(file_name, "w") as f:

            for r in restaurant_objects:

                line = ";".join([
                    str(r.get_id()),
                    r.get_name(),
                    r._Restaurant__address,
                    r._Restaurant__store_image,
                    r._Restaurant__dining_image,
                    r._Restaurant__kitchen_image,
                    r._Restaurant__license_image,
                    r._Restaurant__business_hours
                ])

                f.write(line + "\n")
