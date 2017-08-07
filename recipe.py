#!/usr/bin/python

dict= {'green beans': '2 pounds', 'olive oil': '1 tablespoon', 'butter': '3 tablespoons', 'garlic clover': '2 large ones',
'red pepper flakes': '1 tablespoon', 'lemon zest': '1 tablespoon', 'salt and ground pepper': 'a pinch'};

ing=["Blanch green beans in a large stock pot of well salted boiling water",
"do this for two minutes until it's bright green and crispy",
"then drain and shock in a bowl of ice water to stop from cooking",
 "heat a large heavy skillet over medium heat", "Add the oil and the butter",
  "add the garlic and red pepper flakes and saute until fragrant, about 30 seconds",
  "add the beans and continue to saute until coated in the butter and heated through, about 5 minutes",
  "add lemon zest and season with salt and pepper"];

print(ing[0])
for item in range(len(ing)):
    print(ing[item])

for  item in ing:
    print(item)

for item in dict:
    print (item, ":" , dict[item])
