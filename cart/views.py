from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from bookstore_app.models import Books
from .cart import Cart
from .forms import CartAddBookForm
from discount.forms import *


@require_POST
def cart_add(request, book_id):
    # adding books to cart
    cart = Cart(request)
    book = get_object_or_404(Books, id=book_id)
    form = CartAddBookForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=book,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, book_id):
    # removing books from the trash
    cart = Cart(request)
    book = get_object_or_404(Books, id=book_id)
    cart.remove(book)
    return redirect('cart:cart_detail')


def cart_detail(request):
    # cart contents
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddBookForm(initial={'quantity': item['quantity'], 'update': True})
    
    coupon_apply_form = CouponApplyForm()

    return render(request,
                  'cart/detail.html',
                  {'cart': cart,
                   'coupon_apply_form': coupon_apply_form})
