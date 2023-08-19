from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Заказ №. {}'.format(order.id)
    message = 'Уважаемый {},\n\nВы успешно разместили заказ.\
    Ваш идентификатор заказа {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_sent

