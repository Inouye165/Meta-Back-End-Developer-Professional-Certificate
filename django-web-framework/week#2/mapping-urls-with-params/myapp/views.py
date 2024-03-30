from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.


def menuitems(request, dish):
    items = {
        'pastas': 'Pasta is a type of food typically made from an unleavened dough of wheat flour mixed with water or eggs, and formed into sheets or other shapes, then cooked by boiling or baking.',
        "burger": "Burger",
        'falafal': 'Falafal is a deep-fried ball or patty made from ground chickpeas, fava beans, or both. Falafel is a traditional Middle Eastern food, commonly served in a pita, which acts as a pocket, or wrapped in a flatbread known as taboon; "falafel" also frequently refers to a wrapped sandwich that is prepared in this way. The falafel balls are topped with salads, pickled vegetables, hot sauce, and drizzled with tahini-based sauces. Falafel balls may also be eaten alone as a snack or served as part of a meze tray (assortment of appetizers).', 
        'cheesecake': 'Cheesecake is a sweet dessert consisting of one or more layers. The main, and thickest layer, consists of a mixture of soft, fresh cheese (typically cream cheese or ricotta), eggs, and sugar. If there is a bottom layer, it often consists of a crust or base made from crushed cookies (or digestive biscuits), graham crackers, pastry, or sometimes sponge cake. It may be baked or unbaked (usually refrigerated). Cheesecake is usually sweetened with sugar and may be flavored in many different ways. It may be flavored by adding vanilla, spices, lemon, chocolate, pumpkin, or other flavors to the cheese layer.',
        "fries": "Fries",
        "soda": "Soda",
    }
    description = items[dish]
    return HttpResponse(f"<h2>{dish}</h2>" + description)