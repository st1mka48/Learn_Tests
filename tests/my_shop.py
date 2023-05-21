phone_disk = {}


def main():
    return my_shop(), product(phone_disk)


def discounted(price, discount, max_discount=20, phone_name=''):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Максимальная скидка не больше 100')
    if discount >= max_discount:
        return price
    elif 'iphone' in phone_name.lower():
        return price
    else:
        return price - (price * discount // 100)


def my_shop():
    count = 0
    exit_shop = 'y'
    while exit_shop == 'y':
        try:
            phone = input('Введите модель смартфона: ')
            phone = phone.lower().strip()
            our_price = int(input('Введите цену: '))
            our_discount = int(input('Введите скидку: '))
            price_phone = discounted(our_price, our_discount)
            phone_disk[phone] = price_phone
            count += 1
        except ValueError:
            print("Ошибка ввода данных. Попробуйте еще раз.")
        exit_shop = input('Хотите продолжить? (y/n) ')
    print(f'Добавлено товаров: {count}')
    product(phone_disk)
    with open('my_file.txt', 'w') as file:
        file.write(str(phone_disk))


def product(disk_shop):
    exit_shop = 'y'
    while exit_shop.lower() == 'y':
        try:
            your_phone = input('Укажите модель: ')
            your_phone = your_phone.lower().strip()
            print(f' Цена {your_phone}: {disk_shop[your_phone]}')
        except KeyError:
            print("Такой модели нет в нашем магазине.")
        exit_shop = input('Хотите продолжить? (y/n) ')


if __name__ == '__main__':
    main()