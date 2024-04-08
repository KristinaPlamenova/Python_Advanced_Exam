def shop_from_grocery_list(budget, grocery_list, *args):
    result = []
    for name, price in args:
        if budget < price:
            break
        if name in grocery_list:
            grocery_list.remove(name)
            budget -= price



    if not grocery_list:
        result.append(f"Shopping is successful. Remaining budget: {budget:.2f}.")
    else:
        result.append(f"You did not buy all the products. Missing products: {', '.join(map(str, grocery_list))}.")

    return "".join(result)





print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))




