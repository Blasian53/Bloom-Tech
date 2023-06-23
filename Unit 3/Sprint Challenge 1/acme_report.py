from statistics import mean
from acme import Product
import random

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num=30):
    products = []

    for i in range(num):
        x = Product(name=random.choice(ADJECTIVES) + ' ' +
                    random.choice(NOUNS),
                    price=random.randint(5, 100),
                    weight=random.randint(5, 100),
                    flammability=random.uniform(0.0, 2.5))
        products.append(x)
    return products


def inventory_report(gen_list):
    unique_names = []
    avg_price = []
    avg_weight = []
    avg_flammability = []

    for i in gen_list:
        if i.name not in unique_names:
            unique_names.append(i.name)
        avg_price.append(i.price)
        avg_weight.append(i.weight)
        avg_flammability.append(i.flammability)

    return (len(unique_names), mean(avg_price),
            mean(avg_weight), sum(avg_flammability) / len(avg_flammability))


if __name__ == '__main__':
    product_list = generate_products()
    print(f"The product has been generated with {len(product_list)} items")
    for product in product_list:
        print(product.name)
    print(inventory_report(generate_products()))
    print('\n')
