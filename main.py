__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
from setupdb import *
from datetime import datetime
from rich import print


def search(term: str):
    term = term.lower()
    query = Products.select().where(Products.name.contains(term) | Products.description.contains(term))
    if query:
        print( 
            f"[green]We have found your search term - {term} - in the following hit(s): \n")
        for product in query:
            print(f"Products name: {product.name}")
            print(f"Description: {product.description}")
            print(f"Price: {product.price_per_unit}")
            print(f"Quantity in stock: {product.amount_in_stock} \n")
    else:
        print(
            f"[red]Sorry, no matching products have been found for: {term} \nPlease try another search term")


def list_user_products(user_id: int):
    query = Products.select().where(Products.owner == user_id)

    if query:
        user = Users.get_by_id(user_id)
        print(
            f"[green]We have found the following product(s) for {user.name}:\n")
        for product in query:
            print(f"Products name: {product.name}")
            print(f"Price: {product.price_per_unit}")
            print(f"Quantity in stock: {product.amount_in_stock} \n")
    else:
        print(
            f"[red]Sorry, no product(s) have been found for user id: {user_id}")


def list_products_per_tag(tag_id: int):
    query = Products.select().join(ProductTag).join(
        Tags).where(Tags.tag_id == tag_id)

    if query:
        tag = Tags.get_by_id(tag_id)
        print(
            f"[green]We have found the following product(s) for tag name {tag.name}:\n")
        for product in query:
            print(f"Products name: {product.name}")
            print(f"Price: {product.price_per_unit}")
            print(f"Owner: {product.owner.name} \n")
    else:
        print(
            f"[red]sorry, no product(s) have been found for tag id: {tag_id}")


def add_product_to_catalog(user_id: int, product_id: int):
    user = Users.get_by_id(user_id)
    product = Products.get_by_id(product_id)

    product.owner = user
    product.save()

    print(f"[green]Product {product.name} is added for {user.name}")


def update_stock(product_id, new_quantity):
    query = Products.get_by_id(product_id)

    old_stock = query.amount_in_stock
    query.amount_in_stock = new_quantity
    query.save()
    print(
        f"[green]Old amount in stock of {query.name} was {old_stock}, new amount of stock is: {new_quantity}")


def purchase_product(product_id: int, buyer_id: int, quantity: int):
    product = Products.get_by_id(product_id)
    buyer = Users.get_by_id(buyer_id)

    if buyer_id == product.owner:
        print(
            f"[red]Sorry {buyer.name}, you can't buy your own products.")

    if quantity >= product.amount_in_stock:
        print(
            f"[red]Sorry, the requested amount ({quantity}) of {product.name} is currently not in stock.\nAt this moment we have {product.amount_in_stock} of {product.name} in stock.")

    else:
        price_per_unit = product.price_per_unit
        purchased_price = round(product.price_per_unit * quantity, 2)

        transaction = Transactions.create(
            buyer=buyer_id,
            purchased_product=product_id,
            purchased_quantity=quantity,
            purchased_price=purchased_price,
            date=datetime.now().date()
        )
        print(
            f"[green]On {transaction.date} {buyer.name} bought {quantity} of {product.name} for a total amount of: €{transaction.purchased_price}.\nThe price per {product.name} is €{price_per_unit}")

        new_quantity = product.amount_in_stock - quantity

        update_stock(product_id, new_quantity)


def remove_product(product_id):
    try:
        query = Products.get_by_id(product_id)
        print(f"[green]Product {query.name} has been removed from inventory!")
        query.delete_instance()

    except DoesNotExist:
        print(
            f"[red]Product {product_id} was not found in inventory.\nCheck entered product id or product has already been removed from inventory.")


def main():

    print("If a database exists it will be deleted first to start with a clean database")
    print("")

    if os.path.exists("betsy_webshop.db") == True:
        delete_database()

    print("Creating database")

    create_test_data()
    print("")

    # Search function:
    print(
        "Starting test: search function (with term red)")
    search("red")
    print("")

    # List User Products function:
    print(
        "Starting test: List User Products function (with user_id: 1 which is Flip Fluitketel)")
    list_user_products(1)
    print("")

    # List Products Per Tag function:
    print(
        "Starting test: List Products Per Tag function (with tag_id: 2 which is cake)")
    list_products_per_tag(2)
    print("")

    # Add Product To Catalog function:
    print(
        "Starting test: Add Product To Catalog function (with user_id: 2 which is Joep Meloen and product id: 3 which is pecan pie)")
    add_product_to_catalog(2, 3)
    print("")

    # Update Stock function:
    print(
        "Starting test: Update Stock function (with product_id: 5 which is velvet cake and adjust the stock to 20)")
    update_stock(5, 20)
    print("")

    # Purchase Product function:
    print(
        "Starting test: Purchase Product function (with product_id: 4 which is carrot cake, buyer_id: 5 which is Willie Wezel and quantity of 2)")
    purchase_product(4, 5, 2)
    print("")

    # Remove Product function:
    print(
        "Starting test: Remove Product function (with product_id: 2 which is strawberry cake)")
    remove_product(2)
    print("")

    # Invalid Search:
    print(
        "Starting test: Invalid Search (with term cookie)")
    search("cookie")
    print("")

    # Invalid List User Products:
    print(
        "Starting test: Invalid List User Products (with user_id: 8)")
    list_user_products(8)
    print("")

    # Invalid List Products Per Tag:
    print(
        "Starting test: Invalid List Products Per Tag (with tag_id: 9)")
    list_products_per_tag(9)
    print("")

    # Insufficient stock:
    print(
        "Starting test: Insufficient stock (with product_id: 1 which is chocolate cake, buyer_id: 3 which is Ome Willem and quantity of 8)")
    purchase_product(1, 3, 8)
    print("")

    # Invalid id for Remove Product:
    print(
        "Starting test: Invalid id for Remove Product (with product_id: 7)")
    remove_product(7)
    print("")
    print(
        f"End of tests")


if __name__ == '__main__':
    main()
