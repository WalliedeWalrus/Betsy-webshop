from models import *
from rich import print
import os


# Delete database:
def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "betsy_webshop.db")
    if os.path.exists(database_path):
        os.remove(database_path)


# Create clean database:
def create_test_data():
    db.connect()
    cwd = os.getcwd()
    print(
        f"Betsy's webshop database is created in folder [yellow] {cwd}")

    db.create_tables(
        [
            Users,
            Products,
            Tags,
            ProductTag,
            Transactions
        ]
    )
    # User 1
    flipfluitketel = Users.create(
        name="Flip Fluitketel",
        address="Ketelstraat 10",
        zip_code="1234 FF",
        city="Rotterdam",
        billing_information="Ideal ABN Amro"
    )
    # User 2
    joepmeloen = Users.create(
        name="Joep Meloen",
        address="Meloenstraat 10",
        zip_code="1234 MM",
        city="Amsterdam",
        billing_information="Visacard 9876543210"
    )
    # User 3
    omewillem = Users.create(
        name="Ome Willem",
        address="Studio 6",
        zip_code="1234 WW",
        city="Deventer",
        billing_information="Paypal"
    )
    # User 4
    linkeloetje = Users.create(
        name="Linke Loetje",
        address="Gevangenis 13",
        zip_code="1234 LL",
        city="Den Haag",
        billing_information="Zwart geld"
    )
    # User 5
    williewezel = Users.create(
        name="Willie Wezel",
        address="Bosstraat 1",
        zip_code="1234 BB",
        city="Veluwe",
        billing_information="Natura"
    )

    # Products
    chocolatecake = Products.create(
        owner=flipfluitketel,
        name="Chocolate cake",
        description="Death by chocolate: if you like chocolate, you like this cake",
        price_per_unit=29.99,
        amount_in_stock=5,
    )
    strawberrycake = Products.create(
        owner=joepmeloen,
        name="Strawberry cake",
        description="Delicious cake with loads of strawberry cream",
        price_per_unit=24.99,
        amount_in_stock=3,
    )
    pecanpie = Products.create(
        owner=omewillem,
        name="Pecan pie",
        description="Delicious cake with lots of pecan and nuts",
        price_per_unit=39.95,
        amount_in_stock=10,
    )
    carrotcake = Products.create(
        owner=linkeloetje,
        name="Carrot cake",
        description="Healthy carrot cake",
        price_per_unit=14.95,
        amount_in_stock=3,
    )
    redvelvetcake = Products.create(
        owner=williewezel,
        name="Red velvet cake",
        description="Delicious red velvet cake with chocolate and strawberries",
        price_per_unit=19.95,
        amount_in_stock=15,
    )

    # Tags
    chocolate = Tags.create(
        name="chocolate"
    )
    cake = Tags.create(
        name="cake"
    )
    nodiet = Tags.create(
        name="nodiet"
    )
    strawberry = Tags.create(
        name="strawberry"
    )
    pecan = Tags.create(
        name="pecan"
    )
    nuts = Tags.create(
        name="nuts"
    )
    carrot = Tags.create(
        name="carrot"
    )
    healthy = Tags.create(
        name="healthy"
    )

    # Product tags chocolatecake:
    ProductTag.create(
        product=chocolatecake,
        tag=chocolate
    )
    ProductTag.create(
        product=chocolatecake,
        tag=cake
    )
    ProductTag.create(
        product=chocolatecake,
        tag=nodiet
    )

    # Product tags strawberrycake:
    ProductTag.create(
        product=strawberrycake,
        tag=strawberry
    )
    ProductTag.create(
        product=strawberrycake,
        tag=cake
    )

    # Product tags pecanpie:
    ProductTag.create(
        product=pecanpie,
        tag=pecan
    )
    ProductTag.create(
        product=pecanpie,
        tag=nuts
    )

    # Product tags carrotcake
    ProductTag.create(
        product=carrotcake,
        tag=carrot
    )
    ProductTag.create(
        product=carrotcake,
        tag=cake
    )
    ProductTag.create(
        product=carrotcake,
        tag=healthy
    )

    # Product tags redvelvetcake:
    ProductTag.create(
        product=redvelvetcake,
        tag=cake
    )
    ProductTag.create(
        product=redvelvetcake,
        tag=chocolate
    )
    ProductTag.create(
        product=redvelvetcake,
        tag=strawberry
    )