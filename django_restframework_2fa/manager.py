from django.contrib.auth.models import BaseUserManager

from django.contrib.auth import get_user_model


class UserManager(BaseUserManager):
    
    def create_user(
        self, first_name, last_name, email, password, mobile_number, is_active, is_email_verified, is_mobile_number_verified
        ):

        user = get_user_model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name, 
            mobile_number = mobile_number, 
            password  = password, 
            is_email_verified = is_email_verified,
            is_mobile_number_verified = is_mobile_number_verified,
            is_active = is_active,
        )

        
        # Encrypt password before storing.
        user.set_password(password)

        
        # Save the object to the model.
        user.save(using = self._db)

        
        # Return newly created object's string representation.
        return user