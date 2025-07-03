from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models





class MyAccountMananger(BaseUserManager):
    '''
    when you use a custom user model with AbstractBaseUser, Django no longer knows how to create users or superusers by default so,
    You have to define that logic yourself using a custom manager.
    and create_user() and create_superuser() method names constant. Django expects your model manager to define:
     create_user(self, ...) and   create_superuser(self, ...)
    '''

    def create_user(self, first_name, last_name, username, email, password ):
        if not email:
            raise ValueError("User must have email")
        if not username:
            raise ValueError("User must have username")

        # Create an instance of the model (Account) attached to this manager
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)

        # ensures the object is saved in the correct database i.e. the db manager
        # is currently using (useful when your project has more than one DB)
        user.save(using=self.db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password ):

        #creating superuser using create_user method / reusing creat_user method
        user=self.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
        )
        user.is_admin=True
        user.is_staff=True
        user.is_active=True
        user.is_superadmin=True

        user.save(using=self.db)
        return user



'''Django’s built-in authentication system expects a user model — by default, it uses django.contrib.auth.models.User and
   if using your own model (like Account), you must tell Django by adding In settings.py -> AUTH_USER_MODEL = 'accounts.Account',
   before you run makemigrations.
   and to prevent passwords from being editable in the Django admin panel and to make it read only we will use UserAdmin in admin.py'''

class Account(AbstractBaseUser):
    first_name  = models.CharField(max_length=20)
    last_name   = models.CharField(max_length=20)
    username    = models.CharField(max_length=20, unique=True)
    email       = models.EmailField(max_length=50, unique=True)
    phn_no      = models.CharField(max_length=20)

    #Required
    date_joined     = models.DateTimeField(auto_now=True)
    last_login      = models.DateTimeField(auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models. BooleanField(default=False)
    is_active       = models. BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)

    # telling Account model that we are using MyAccountManager for managing the creation of user
    objects = MyAccountMananger()


    # USERNAME_FIELD is a built-in Django constant used when you define a custom user model, tells Django which field should be used as the unique identifier for login.
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username','last_name','first_name']
    # REQUIRED_FIELDS is not a built-in constant, it's a special class attribute that Django looks for when you're using a custom user model with AbstractBaseUser

    def __str__(self):
        return f"{self.email} : {self.username}"

    # if you're creating a custom user model using AbstractBaseUser,then you must implement both:- has_perm(self, perm, obj=None) , has_module_perms(self, app_label)
    # Django's permission system expects these methods to exist on the user model and Permission checks like user.has_perm() will break

    def has_perm(self, perm, obj=None):         #Used to check if a user has a specific permission
        return self.is_admin
    def has_module_perms(self, add_label):      #Used to check if a user has any permission in a specific app.
        return True



