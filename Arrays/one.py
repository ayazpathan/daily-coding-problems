# This is the first problem I'm testing

test_prefix = []
def products(nums): 
    # Generate prefix products. 
    prefix_products = [] 
    
    for num in nums: 
        if prefix_products: 
            prefix_products.append(prefix_products[-1] * num) 
        else: 
            prefix_products.append(num)
    print(prefix_products);

    print(prefix_products);

    
products([1, 2, 3, 4, 5])
    
