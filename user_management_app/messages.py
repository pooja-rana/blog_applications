from core.messages import CommonMessages

class UserDetailsMessages(CommonMessages):
    INVALID_PASSWORD = "Password must be min 8 characters, and have 1 Special Character, 1 Uppercase, 1 Number, " \
                       "and 1 Lowercase. "
    INVALID_EMAIL = "Please enter valid email address."
    EMAIL_ALREADY_EXISTS = "This email already exists."
    ENTITY_WITH_PHONE_NUMBER = "Please enter valid phone number."
    USER_REGISTER_SUCCESSFULLY = "User register successfully."
    USERNAME_PASSWORD_NOT_MATCH = "Your Username & Password do not match. Please try again."
    USER_LOGIN_SUCCESSFULLY = "User login successfully."
    PROFILE_UPDATE_SUCCESSFULLY= "Profile updated successfully."
    USER_UPDATE_ONLY_OWN_PROFILE = "User update only own profile."
