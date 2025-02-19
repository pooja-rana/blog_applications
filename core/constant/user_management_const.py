from enum import Enum


class UserConst(Enum):
    PASSWORD_REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&^()_+|}" \
                     r"{\]\[:><.,\/\\;'=~`\"-])[A-Za-z\d@$!#%*?&^()_+|}{\]\[:><.,\/\\;'=~`\"-]{8,64}$"
    PHONE_NUMBER = "^[+]?[0-9]{6,15}$"
