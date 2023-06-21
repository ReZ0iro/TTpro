from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager #its for Customizeing Users

# Create your models here.

class UserAccountsManager(BaseUserManager):
    def create_superuser(self,username , password = None) : 
        if not username : 
            raise ValueError("Please Enter Username !")
        user = self.model(
            username = username ,
        )

        user.is_superuser = True
        user.is_staff     = True
        user.role = 1
        user.set_password(password)
        user.save(using = self._db)
        return user


    def create_admin(self, username, email, first_name, last_name, phone_number,password =None) : 

        if not username :
            raise ValueError("Please Enter Username !")
        if not email    : 
            raise ValueError("Please Enter email !")
        
        user = self.model(
            username    = username , 
            email       = self.normalize_email(email) , 
            first_name  = first_name , 
            last_name   = last_name ,
            phone_number = phone_number , 
            
        )
        
        user.role       = 2 
        
        user.is_admin   = True

        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_user(self ,username, email, first_name, last_name, password = None) : 
        
        if not username : 
            raise ValueError("Please Enter Username !")
        if not email : 
            raise ValueError("please Enter Email !")
        
        user = self.model(
            username    = username      ,
            email       = self.normalize_email(email) ,
            first_name  = first_name , 
            last_name   = last_name  ,
        )
        
        user.role   = 4
        
        user.set_password(password)
        
        user.save(using = self._db)
        
        return user

class UserAccounts(AbstractBaseUser) : 
    """

    
    """
    first_name  = models.CharField(max_length=50)

    last_name   = models.CharField(max_length=50)   

    username   = models.CharField(max_length=50, unique=True, null=False, blank=False)

    phone_number = models.CharField(max_length=14 ,unique=True, null=True, blank=True)

    email   = models.EmailField(max_length=75 , unique=True, blank=True, null=True)

    bio     = models.CharField(max_length=100, null=True, blank=True)

    # profile_image =  
    
    # music => dar inja bayad ye jori ye link musici chizi bezaram k ye chizi to maye haye masalan status to 

    # estefadeh mishe !!!

    following   = models.ManyToManyField("self" , blank=True) 

    SUPERADMIN  = 1
    ADMIN       = 2
    PRO_USER    = 3
    USER        = 4

    ROLE_CHOICES = (
        (SUPERADMIN , "SUPERADMIN") , 
        (ADMIN      , "ADMIN") , 
        (PRO_USER   , "PRO_USER") , 
        (USER       , "USER") ,
    )
    user_role   = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=False, null=False, default=4)

    is_verified     = models.BooleanField(default=False)

    is_admin        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    
    is_active       = models.BooleanField(default=True)

    objects         = UserAccountsManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):

        return self.username


    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True  


