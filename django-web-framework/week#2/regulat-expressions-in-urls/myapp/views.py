from django.http import HttpResponse

def display_menu_item(request, item_id=None):
    if item_id:
        return HttpResponse(f"Displaying menu item with ID: {item_id}")
    return HttpResponse("Displaying menu item with ID: 10")