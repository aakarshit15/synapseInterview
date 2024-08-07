gadgets = [
    ("Explosive Batarangs", 3, True),
    ("Batarangs", 5, True),
    ("Smoke Pellets", 0, False),
    ("Tear Gas Grenades", 2, True),
    ("Night Vision Goggles", 1, True),
    ("Batclaw", 0, False),
    ("Grapple Gun", 3, True),
    ("Batsignal", 0, False),
    ("Utility Belt", 1, True),
    ("Batmobile Tires", 4, True)
]

sortedGadgets = sorted(gadgets, key=(lambda gadget: (-gadget[2], -gadget[1], gadget[0])))

for gadget in sortedGadgets:
    print(gadget)
    

"""
stockSorted = sorted(gadgets, key=(lambda product: product[2]), reverse=True)
quantitySorted = sorted(stockSorted, key=(lambda product: product[1]), reverse=True)

quantities = {product[1] for product in gadgets}
print(quantities)

quantityBasedProducts = []

for quantity in quantities:
    quantityProducts = list(filter((lambda product: product[1] == quantity), quantitySorted))
    quantityBasedProducts.append(quantityProducts)

productNameSorted = []

for quantityProducts in quantityBasedProducts:
    quantityProducts.sort(key=(lambda product: product[0]), reverse=True)
    productNameSorted += quantityProducts

quantityBasedProducts.sort(key=(lambda qunatityProducts : quantityProducts[0][1]))

productNameSorted.reverse()

for product in productNameSorted:
    print(product)
"""

# ('Batarangs', 5, True)
# ('Batmobile Tires', 4, True)
# ('Explosive Batarangs', 3, True)
# ('Grapple Gun', 3, True)
# ('Tear Gas Grenades', 2, True)
# ('Night Vision Goggles', 1, True)
# ('Utility Belt', 1, True)
# ('Batclaw', 0, False)
# ('Batsignal', 0, False)
# ('Smoke Pellets', 0, False)