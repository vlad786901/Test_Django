from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm


def home(request):
    return render(request, 'orders/home.html')


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})


def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            # Собираем данные о блюдах
            dishes = []
            for key, value in request.POST.items():
                if key.startswith('dish_name_'):
                    index = key.split('_')[-1]
                    dish_name = value
                    dish_price = request.POST.get(f'dish_price_{index}')
                    if dish_name and dish_price:
                        dishes.append({'name': dish_name, 'price': float(dish_price)})
            order.items = dishes
            order.total_price = sum(dish['price'] for dish in dishes)
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})


def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = sum(item['price'] for item in order.items)
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})


def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('order_list')
