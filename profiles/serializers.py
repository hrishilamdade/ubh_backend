import json
from rest_framework import serializers,exceptions
from rest_framework.validators import UniqueValidator
from django.utils.translation import ugettext_lazy as _

from .models import *



class UserRegistrationSerializer(serializers.ModelSerializer):
    
    # sub= SubSerializer(required=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = ('email','username','first_name','last_name','password' )
        extra_kwargs = {'password': {'write_only': True}}


    def validate(self, data):
        if User.objects.filter(email = data['email']).exists():
            raise serializers.ValidationError("Email already registered")
        elif User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError("Username already registered")
        # elif form.clean_password()==False:
        #     messages.error(request, form.errors)
        #     return HttpResponseRedirect(reverse('show_company_dash'))
        return data
    
    def create(self, validated_data):
        print(validated_data)
        data = {}
        data['email'] = validated_data['email']
        data['username'] = validated_data['username']
        data['first_name'] = validated_data['first_name']
        data['last_name'] = validated_data['last_name']
        data['password'] = validated_data['password']

        user = User.objects.create_user(**data)
        user.save()
        return user


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','username' )


class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('style', {})

        kwargs['style']['input_type'] = 'password'
        kwargs['write_only'] = True

        super().__init__(*args, **kwargs)


class TokenObtainPairSerializer(serializers.Serializer):

    default_error_messages = {
        'no_active_account': _('No active account found with the given credentials'),
        'user_not_active': _('Please check your email box to activate your account.'),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'] = serializers.CharField()
        self.fields['password'] = PasswordField()

    def validate(self, attrs):
        # authenticate_kwargs = {
        #     self.username_field: attrs[self.username_field],
        #     'password': attrs['password'],
        # }
        # try:
        #     authenticate_kwargs['request'] = self.context['request']
        # except KeyError:
        #     pass
        # print(authenticate_kwargs)
        # self.user = authenticate(**authenticate_kwargs)
        # print(self.user)
        # Prior to Django 1.10, inactive users could be authenticated with the
        # default `ModelBackend`.  As of Django 1.10, the `ModelBackend`
        # prevents inactive users from authenticating.  App designers can still
        # allow inactive users to authenticate by opting for the new
        # `AllowAllUsersModelBackend`.  However, we explicitly prevent inactive
        # users from authenticating to enforce a reasonable policy and provide
        # sensible backwards compatibility with older Django versions.
        username = attrs['username']
        password = attrs['password']
        try:
            self.user = User.objects.get(username=username)
            if self.user.check_password(password):
                if self.user is None :
                    raise exceptions.AuthenticationFailed(
                        self.error_messages['no_active_account'],
                        'no_active_account',
                    )
                elif not self.user.is_active:
                    raise exceptions.AuthenticationFailed(
                        self.error_messages['user_not_active'],
                        'user_not_active',
                    )
            else:
                raise serializers.ValidationError("Incorrect username or Password")
                
        except User.DoesNotExist:
            raise serializers.ValidationError("Incorrect username or Password")
        
        return {}

    @classmethod
    def get_token(cls, user):
        raise NotImplementedError('Must implement `get_token` method for `TokenObtainSerializer` subclasses')

class CustomTokenSerializer(serializers.Serializer):
    token = serializers.CharField()

