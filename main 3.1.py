def linear_search_product(product_list, target_product):
    for index, product in enumerate(product_list):
        if product == target_product:
            return f"{target_product} found at index {index}"
    return f"{target_product} not found in the list"

# Example usage:
products = ["apple", "banana", "cherry", "date", "grape"]
target = "cherry"
result = linear_search_product(products, target)
print(result)