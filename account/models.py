from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from account.managers import MyUserManager


class User(AbstractBaseUser):   # namesh hatman bayad user bashe
    email = models.EmailField(max_length=100, unique=True)   # harchizi ke dakhele username fild mizarim hatman bayad unigq bashe
    full_name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)   # inam vajebe aya karbar admine
    is_active = models.BooleanField(default=True)   # in vajebe migim aya faal bashe
    objects = MyUserManager()  # ino bad az inke file manager.py ro neveshtim esme classesho ezafe mikonim inja
    USERNAME_FIELD = 'email'   # be soorate pishfarz ba username karbara shenasai ya hamun login mishodan hala kardim email
    REQUIRED_FIELDS = ['full_name']  # un createsuperuser khodesh username email va pass ro mikhad inja bekhatere khate bala faghat email dg usernami nadarim ma har fildi ke bekhaymo behesh ezafe mikonim

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):   # ino badan tozih midim dastresiaye karbare
        return True


    def has_module_perms(self, app_label):   # aya karbar emkane dastresi be modelharo dare bayad true bashe
        return True

    @property
    def is_staff(self):   # aya emkane dastresi be panele admin ro dare
        return self.is_admin   # faghat unai ke bala goftim adminan va inke hatman bayad property bashe


# agar ye modele dg dashte bashim bekhaym be in user forenkey bezanim ba settings.AUTHS_USER_MODEL