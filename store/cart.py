from decimal import Decimal
from .models import Parfum

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, perfum, perfum_qty):
        perfum_id = str(perfum.id)
        if perfum_id in self.cart:
            self.cart[perfum_id]['qty'] = perfum_qty
        else:
            self.cart[perfum_id] = {'price': str(perfum.price), 'qty': perfum_qty}
        self.session.modified = True

    def delete(self, perfum):
        perfum_id = str(perfum)
        if perfum_id in self.cart:
            del self.cart[perfum_id]
        self.session.modified = True

    def update(self, perfum, qty):
        perfum_id = str(perfum)
        perfum_quantity = qty
        if perfum_id in self.cart:
            self.cart[perfum_id]['qty'] = perfum_quantity
        self.session.modified = True

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())

    def __iter__(self):
        all_perfum_ids = self.cart.keys()
        perfum = Parfum.objects.filter(id__in=all_perfum_ids)
        cart = self.cart.copy()
        for perfum in perfum:
            cart[str(perfum.id)]['perfum'] = perfum
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty']
            yield item

    def get_total(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
