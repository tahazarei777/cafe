from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re

class CustomPasswordValidator:
    def validate(self, password, user=None):
        errors = []
        
        if len(password) < 8:
            errors.append(_("رمز عبور باید حداقل ۸ کاراکتر باشد."))
        
        if not re.search(r'[A-Z]', password):
            errors.append(_("رمز عبور باید حداقل یک حرف بزرگ (A-Z) داشته باشد."))
        
        if not re.search(r'[0-9]', password):
            errors.append(_("رمز عبور باید حداقل یک عدد (0-9) داشته باشد."))
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append(_("رمز عبور باید حداقل یک نماد خاص (!@#...) داشته باشد."))
        
        if errors:
            raise ValidationError(errors)

    def get_help_text(self):
        return _(
            "رمز عبور باید شامل:\n"
            "- حداقل ۸ کاراکتر\n"
            "- حداقل یک حرف بزرگ\n"
            "- حداقل یک عدد\n"
            "- حداقل یک نماد خاص"
        )