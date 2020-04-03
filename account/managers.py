from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):  # har namem ishe behesh dad
    def create_user(self, email, full_name,
                    password):  # miad ye usere mamuli ijad mikone, harchi dakhele username_field va required_filde modele user neveshtim ba password bayad dakhele in bashe, fieldhaye dh ham mitune bashe amma ina be dalayeli ke goftim vajebe
        if not email:  # mikhaym hatman vared kone
            raise ValueError('email is ejbari')

        if not full_name:  # mamulan harchi too username_field va required fild mizarim migim hatman bayad karbar vared kone
            raise ValueError('full_name is ejbari')

        # hala bayad user ra ijad konim faghat badan be modele user mifahmunimesh
        user = self.model(email=self.normalize_email(email),
                          full_name=full_name)  # emailesh barabar bashe ba normalize shodeye emailemun amma full namesh hamun bashe
        user.set_password(password)  # inam asswordo hash va code gozari mikone
        user.save(using=self.db)  # dakhele parantez be khatere inke tooye database doros zakhire she
        return user

    def create_superuser(self, email, full_name, password):  # miad ye superuser ijad mikone
        user = self.create_user(email, full_name, password)  # hamun metode balaro seda mizanim ke besaze
        user.is_admin = True  # faghat bayad inja begim adminesho bezar true
        user.save(using=self.db)
        return user

    # hal bayad berim tooye model va user va object ra ezafe konim
