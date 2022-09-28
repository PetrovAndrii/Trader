class RegisterConstants:
    CHECKOUT_TEXT_CSS_SELECTOR = '.checkout-step'
    LOGIN_LINK_XPATH = '//*[@class="auth-switch"]/p/a'
    FULL_NAME_FIELD_XPATH = '//input[@placeholder="Full Name"]'
    EMAIL_FIELD_XPATH = '//input[@placeholder="Email"]'
    PASSWORD_FIELD_XPATH = '//input[@placeholder="Password"]'
    PHONE_FIELD_XPATH = '//input[@placeholder="Phone"]'
    AGREE_TERMS_CHECKBOX_XPATH = '//input[@type="checkbox"]'
    # AGREE_TERMS_CHECKBOX_XPATH_2 = '//*[@class="form-block"]/form/label/input'
    CREATE_MY_ACCOUNT_BUTTON_XPATH = '//button[@type="submit"]'
    CREATE_AN_ACCOUNT_LINK_XPATH = '//*[@class="auth-switch"]/p/a'
    ACTIVE_CHARACTER_COUNT_ERROR_CSS_SELECTOR = 'div.validation-rules > p:nth-child(1) > i.ucpicon-close'
    ACTIVE_NUMBER_ERROR_CSS_SELECTOR = 'div.validation-rules > p:nth-child(2) > i.ucpicon-close'
    ACTIVE_SPECIAL_CHARACTER_ERROR_CSS_SELECTOR = 'div.validation-rules > p:nth-child(3) > i.ucpicon-close'
    ACTIVE_CAPITAL_LETTER_ERROR_CSS_SELECTOR = 'div.validation-rules > p:nth-child(4) > i.ucpicon-close'
    CHARACTER_COUNT_NO_ERROR_CSS_SELECTOR = 'div.validation-rules > p:nth-child(1) > i.ucpicon-content-menu-checkbox'
    NUMBER_NO_ERROR_CSS_SELECTOR = 'div.validation-rules > p:nth-child(2) > i.ucpicon-content-menu-checkbox'
    SPECIAL_CHARACTER_NO_ERROR_CSS_SELECTOR = 'div.validation-rules > p:nth-child(3) > i.ucpicon-content-menu-checkbox'
    CAPITAL_LETTER_NO_ERROR_CSS_SELECTOR = 'div.validation-rules > p:nth-child(4) > i.ucpicon-content-menu-checkbox'
    FIELD_IS_REQUIRED_ERROR_XPATH = '//*[@class="form-inputs"]/div[1]/span/div/p'
    FIELD_IS_REQUIRED_ERROR_TEXT = 'This field is required!'
    AGREE_TERMS_ERROR_TEXT = 'You must agree with terms and conditions'
    VALID_EMAIL_ERROR_TEXT = 'Please enter valid email address'
    VALID_EMAIL_ERROR_XPATH = '//*[@class="form-inputs"]/div[2]/span/div/p'
    TERMS_LINK_XPATH = '//*[@name="terms"]/span/a[1]'
    LICENSE_LINK_XPATH = '//*[@name="terms"]/span/a[2]'
    YOU_MUST_AGREE_ERROR_TEXT_XPATH = '//*[@class="form-block"]/form/p'
    COOKIES_AGREE_BUTTON_CSS_SELECTOR = '.banner_cookie_agreeBtn'
    CONFIRMATION_REGISTRATION_CSS_SELECTOR = '.offer-content'
    ERROR_CONTAINS_XPATH = '//*[contains(@class,"error")]'










