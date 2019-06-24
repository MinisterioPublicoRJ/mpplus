import base64
import json
import requests

from django.conf import settings
from django.contrib.auth.models import User, Group


class Authenticator():

    def authenticate(self, request, username, password):
        del request
        password = bytes(password, 'utf-8')
        session = requests.session()

        response = session.post(
            url=settings.AUTH_MPRJ,
            data={
                'username': username,
                'password': base64.b64encode(password).decode('utf-8') 
            }
        )

        if response.status_code == 200:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                response = session.get(url=settings.AITJ_MPRJ_USERINFO)
                corpo = json.loads(response.content.decode('utf-8'))
                permissions = corpo['permissions']
                if 'ROLE_mp_plus_admin' in permissions and permissions['ROLE_mp_plus_admin']:
                    user = User(username=username)
                    user.is_staff = True
                    user.is_superuser = False
                    user.email = username + '@mprj.mp.br'
                    user.first_name = corpo['userDetails']['nome'].split()[0]
                    user.last_name = corpo['userDetails']['nome'].split()[-1]
                    user.save()

                    mpplus = Group.objects.get(name='MP_PLUS')
                    mpplus.user_set.add(user)
                else:
                    return None
            return user



        return None
