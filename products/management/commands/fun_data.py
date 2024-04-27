from django.core.management import BaseCommand
import json

from products.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories_list = []
        products_list = []

        categories_list_for_create = []

        with open('data.json', 'r', encoding='utf-8') as file:
            items_from_file = json.load(file)

        for item in items_from_file:
            if item['model'] == 'products.category':
                categories_list.append(Category(**item['fields']))
            if item['model'] == 'products.product':
                products_list.append(Product(**item['fields']))

        # print(products_list)
        # print('_'*30)
        # print(categories_list)

        Category.objects.bulk_create(categories_list)
        Product.objects.bulk_create(products_list)
