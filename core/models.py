from django.db import models
from cloudinary.models import CloudinaryField

class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False)
    COUNTRY_CODE_CHOICES = [
        ('+1', '+1 (USA)'),
        ('+91', '+91 (India)'),
        ('+44', '+44 (UK)'),
        ('+61', '+61 (Australia)'),
        ('+81', '+81 (Japan)'),
        ('+86', '+86 (China)'),
        ('+49', '+49 (Germany)'),
        ('+33', '+33 (France)'),
        ('+39', '+39 (Italy)'),
        ('+7', '+7 (Russia)'),
        ('+27', '+27 (South Africa)'),
        ('+55', '+55 (Brazil)'),
        ('+34', '+34 (Spain)'),
        ('+62', '+62 (Indonesia)'),
        ('+63', '+63 (Philippines)'),
        ('+64', '+64 (New Zealand)'),
        ('+20', '+20 (Egypt)'),
        ('+971', '+971 (UAE)'),
        ('+92', '+92 (Pakistan)'),
        ('+972', '+972 (Israel)'),
        ('+94', '+94 (Sri Lanka)'),
        ('+880', '+880 (Bangladesh)'),
        ('+1', '+1 (Canada)'),
        ('+598', '+598 (Uruguay)'),
        ('+353', '+353 (Ireland)'),
        ('+47', '+47 (Norway)'),
        ('+46', '+46 (Sweden)'),
        ('+48', '+48 (Poland)'),
        ('+52', '+52 (Mexico)'),
        ('+351', '+351 (Portugal)'),
        ('+90', '+90 (Turkey)'),
        ('+82', '+82 (South Korea)'),
        ('+98', '+98 (Iran)'),
        ('+234', '+234 (Nigeria)'),
        ('+254', '+254 (Kenya)'),
        ('+255', '+255 (Tanzania)'),
        ('+260', '+260 (Zambia)'),
        ('+263', '+263 (Zimbabwe)'),
    ]
    
    country_code = models.CharField(
        max_length=5,
        choices=COUNTRY_CODE_CHOICES,
        default='',
        blank=False
    )
    
    phone_number = models.CharField(
        max_length=15,
        default="",
        blank=False
    )
    
    company_stage = models.CharField(
        max_length=50,
        choices=[
            ('idea', 'Idea Stage'),
            ('startup', 'A Startup'),
            ('smb', 'A SMB'),
            ('enterprise', 'An Enterprise'),
        ],
        blank=False
    )
    # help_with = models.CharField(max_length=255)  # Comma-separated options
    help_with = models.CharField(max_length=255, blank=False)
    message = models.TextField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    

class JoinUs(models.Model):

    COUNTRY_CODE_CHOICES = [
        ('+1', '+1 (USA)'),
        ('+91', '+91 (India)'),
        ('+44', '+44 (UK)'),
        ('+61', '+61 (Australia)'),
        ('+81', '+81 (Japan)'),
        ('+86', '+86 (China)'),
        ('+49', '+49 (Germany)'),
        ('+33', '+33 (France)'),
        ('+39', '+39 (Italy)'),
        ('+7', '+7 (Russia)'),
        ('+27', '+27 (South Africa)'),
        ('+55', '+55 (Brazil)'),
        ('+34', '+34 (Spain)'),
        ('+62', '+62 (Indonesia)'),
        ('+63', '+63 (Philippines)'),
        ('+64', '+64 (New Zealand)'),
        ('+20', '+20 (Egypt)'),
        ('+971', '+971 (UAE)'),
        ('+92', '+92 (Pakistan)'),
        ('+972', '+972 (Israel)'),
        ('+94', '+94 (Sri Lanka)'),
        ('+880', '+880 (Bangladesh)'),
        ('+1', '+1 (Canada)'),
        ('+598', '+598 (Uruguay)'),
        ('+353', '+353 (Ireland)'),
        ('+47', '+47 (Norway)'),
        ('+46', '+46 (Sweden)'),
        ('+48', '+48 (Poland)'),
        ('+52', '+52 (Mexico)'),
        ('+351', '+351 (Portugal)'),
        ('+90', '+90 (Turkey)'),
        ('+82', '+82 (South Korea)'),
        ('+98', '+98 (Iran)'),
        ('+234', '+234 (Nigeria)'),
        ('+254', '+254 (Kenya)'),
        ('+255', '+255 (Tanzania)'),
        ('+260', '+260 (Zambia)'),
        ('+263', '+263 (Zimbabwe)'),
    ]

    POSITION_CHOICES = [
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('manager', 'Manager'),
        ('sales-representative', 'Sales Representative'),
        ('marketing-specialist', 'Marketing Specialist'),
    ]

    join_us_name = models.CharField(max_length=100, verbose_name="Your Name",blank=False)
    join_us_email = models.EmailField(verbose_name="Email Address", blank=False)
    join_us_country_code = models.CharField(
        max_length=5,
        choices=COUNTRY_CODE_CHOICES,
        default='',
        blank=False
    )
    
    join_us_phone_number = models.CharField(
        max_length=15,
        default="",
        blank=False
    )

    position_applying_for = models.CharField(
        max_length=50, choices=POSITION_CHOICES, verbose_name="Position Applying For",
        blank=False
    )

    location = models.CharField(max_length=255, blank=False, verbose_name="Where are you based?")

    file_upload = CloudinaryField('image')

    join_us_message = models.TextField(blank=False, null=True)

    class Meta:
      verbose_name_plural = "Join Us"

