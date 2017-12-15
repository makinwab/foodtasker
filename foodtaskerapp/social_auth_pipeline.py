from foodtaskerapp.models import Customer, Driver

def create_user_by_type(backend, user, response, *args, **kwargs):
    request = backend.strategy.request_data()
    print request
    if backend.name == 'facebook':
        fb_pic_url = 'https://graph.facebook.com/%s/picture?type=large'
        avatar = fb_pic_url % response['id']
    else:
        avatar = ''

    if request['user_type'] == "driver" and not Driver.objects.filter(
        user_id=user.id
    ):
        Driver.objects.create(user_id=user.id, avatar=avatar)
    elif not Customer.objects.filter(user_id=user.id):
        Customer.objects.create(user_id=user.id, avatar=avatar)
