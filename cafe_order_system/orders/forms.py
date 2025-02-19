from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_number', 'status']

    dish_name = forms.CharField(max_length=100, required=False,
                                label="Название блюда")
    dish_price = forms.DecimalField(max_digits=10, decimal_places=2,
                                    required=False, label="Цена блюда")

    def clean_items(self):
        items = self.cleaned_data['items']
        if not isinstance(items, list):
            raise forms.ValidationError("Должен быть список блюд.")
        return items
