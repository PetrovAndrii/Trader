import time


class MarketingPagesHelper:

    def __init__(self, app):
        self.app = app

# partnership pages
    def open_partnership_pages(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # scroll page down
        wd.find_element_by_xpath('//*[@class="footer"]/div/div[2]/div/div[1]/ul/li[5]/a').click()

    def link_become_an_affiliate(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@class="item"]/a').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def button_become_an_affiliate(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="Partnership"]/div[2]/a[1]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def button_become_a_partner(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="Partnership"]/div[2]/a[2]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

# Terms & Condition
    def open_terms_pages(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # scroll page down
        new_window_url = wd.find_element_by_xpath('//*[@class="footer"]/div/div[5]/ul/li[4]/a').get_attribute("href")
        wd.get(new_window_url)

    def check_subparagraphs_terms_text(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[contains(text(), 'Website Terms of Use')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Acceptance of the Terms of Use')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Changes to the Terms of Use')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Accessing the Website and Account Security')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Intellectual Property Rights')]")
        wd.find_element_by_xpath('//*[@id="LandingPageContainer"]/div[2]/div/div/div/div/strong[5]')
        wd.find_element_by_xpath('//*[@id="LandingPageContainer"]/div[2]/div/div/div/div/strong[6]')
        wd.find_element_by_xpath("//*[contains(text(), 'SmartTrader’s Refer-a-Friend Program Terms & Conditions')]")
        wd.find_element_by_xpath('//*[@id="LandingPageContainer"]/div[2]/div/div/div/div/strong[9]')
        wd.find_element_by_xpath("//*[contains(text(), 'Transactions are only complete if they are confirmed')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Trademarks')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Prohibited Uses')]")
        wd.find_element_by_xpath('//*[@id="LandingPageContainer"]/div[2]/div/div/div/div/strong[12]')
        wd.find_element_by_xpath("//*[contains(text(), 'Monitoring and Enforcement; Termination')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Electronic Delivery of Communications')]")
        wd.find_element_by_xpath("//*[contains(text(), 'HOW TO WITHDRAW YOUR CONSENT')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Reliance on Information Posted')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Changes to the Website')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Information About You and Your Visits to the Website')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Online Purchases and Other Terms and Conditions')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Linking to the Website and Social Media Features')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Links from the Website')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Geographic Restrictions')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Disclaimer of Warranties')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Limitation on Liability')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Indemnification')]")
        wd.find_element_by_xpath("//*[contains(text(), 'General Legal Provisions')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Contact Us!')]")

    def privacy_policy_link(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[3]/b/a[1]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def community_guidelines_link(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[3]/b/a[2]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def risk_disclaime_link(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[3]/a').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def privacy_policy_link2(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[9]/a').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def terms_use_link(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[34]/a[1]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def community_guidelines_link2(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[34]/a[2]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def terms_use_link2(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[35]/a[1]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def community_guidelines_link3(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[35]/a[2]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def privacy_policy_link3(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[61]/a[1]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def privacy_policy_link4(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[61]/a[2]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def community_guidelines_link4(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[65]/a').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

# Risk and General Disclaimer
    def open_risk_disclainer(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # scroll page down
        new_window_url = wd.find_element_by_xpath('//*[@class="footer"]/div/div[5]/ul/li[1]/a').get_attribute("href")
        wd.get(new_window_url)

    def check_subparagraphs_risk_text(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[contains(text(), 'GENERAL RISK DISCLAIMER')]")
        wd.find_element_by_xpath("//*[contains(text(), 'RISKS ASSOCIATED WITH FOREX TRADING')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Hypothetical Results Disclaimer')]")
        wd.find_element_by_xpath("//*[contains(text(), 'RISKS ASSOCIATED WITH OPTIONS TRADING')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Options Disclosure Document')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Electronic Trading Risks')]")
        wd.find_element_by_xpath("//*[contains(text(), 'RISKS ASSOCIATED WITH CRYPTOCURRENCY')]")
        wd.find_element_by_xpath('//*[@id="LandingPageContainer"]/div[2]/div/div/div/div/strong[7]')
        wd.find_element_by_xpath("//*[contains(text(), 'RISKS ASSOCIATED WITH TRADING THE STOCK MARKET')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Education Services')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Acknowledgement and Agreement')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Accuracy of Information')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Telephone Call Monitoring and Recording')]")
        wd.find_element_by_xpath('//*[@id="LandingPageContainer"]/div[2]/div/div/div/div/strong[13]')
        wd.find_element_by_xpath("//*[contains(text(), 'Third Party')]")
        wd.find_element_by_xpath('//*[@id="LandingPageContainer"]/div[2]/div/div/div/div/strong[15]')
        wd.find_element_by_xpath("//*[contains(text(), 'Celebrity Endorsement')]")

# Privacy Policy
    def open_privacy_policy(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # scroll page down
        new_window_url = wd.find_element_by_xpath('//*[@class="footer"]/div/div[5]/ul/li[2]/a').get_attribute("href")
        wd.get(new_window_url)

    def check_subparagraphs_privacy_policy_text(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[contains(text(), 'SmartTrader Privacy Policy')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Introduction')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Please read this policy carefully to understand "
                                 "how we will treat your information')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Children Under the Age of 13')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Information We Collect About You and How We Collect It')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Information You Provide to Us')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Information We Collect Through "
                                 "Automatic Data Collection Technologies')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Third-Party Use of Cookies and Other Tracking Technologies')]")
        wd.find_element_by_xpath("//*[contains(text(), 'How We Use Your Information')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Disclosure of Your Information')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Choices About How We Use and Disclose Your Information')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Accessing and Correcting Your Information')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Your California Privacy Rights')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Data Security')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Changes to Our Privacy Policy')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Contact Information')]")

    def nai_link(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[25]/a').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        time.sleep(1)
        return url

    def terms_of_use_link(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[27]/a').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

# Community Guidelines
    def open_community_guidelines(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # scroll page down
        new_window_url = wd.find_element_by_xpath('//*[@class="footer"]/div/div[5]/ul/li[3]/a').get_attribute("href")
        wd.get(new_window_url)

    def check_subparagraphs_community_guidelines_text(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[contains(text(), 'SmartTrader User Guidelines and Community Rules')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Overview')]")
        wd.find_element_by_xpath("//*[contains(text(), 'User Guidelines - Account Names and Avatars')]")
        wd.find_element_by_xpath("//*[contains(text(), 'User Guidelines - General')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Community Rules - Posting Comments')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Account Suspension and Banning')]")
        wd.find_element_by_xpath("//*[contains(text(), 'Community Rules - Publishing Ideas and Trading Scripts')]")

    def ideas_link(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[7]/a[1]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def scripting_link(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[7]/a[2]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

# About
    def open_about(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # scroll page down
        wd.find_element_by_xpath('//*[@class="footer"]/div/div[2]/div/div[1]/ul/li[4]/a').click()

    def check_about_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[contains(text(), 'About SmartTrader')]")
        wd.find_element_by_xpath('//*[@id="LandingPageContainer"]/section/section[1]/img')
        wd.find_element_by_xpath('//*[@id="LandingPageContainer"]/section/section[3]/div/div/div[1]/img')
        wd.find_element_by_xpath('//*[@id="LandingPageContainer"]/section/section[3]/div/div/div[2]/img')
        wd.find_element_by_xpath('//*[@id="LandingPageContainer"]/section/section[3]/div/img')
        wd.find_element_by_xpath('//*[@id="LandingPageContainer"]/section/section[4]/div/div/img')
        wd.find_element_by_xpath("//*[contains(text(), 'Building a Supportive')]")

    def learn_more_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="LandingPageContainer"]/section/section[6]/div/a/button').click()
        url = wd.current_url
        return url

# License Agreement
    def open_license_agreement(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # scroll page down
        new_window_url = wd.find_element_by_xpath('//*[@class="footer"]/div/div[5]/ul/li[5]/a').get_attribute("href")
        wd.get(new_window_url)

    def check_license_agreement_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[contains(text(), 'End-User License Agreement')]")
        wd.find_element_by_xpath("//*[contains(text(), 'DEFINITIONS:')]")
        wd.find_element_by_xpath("//*[contains(text(), 'SOFTWARE:')]")
        wd.find_element_by_xpath("//*[contains(text(), 'SERVICE:')]")
        wd.find_element_by_xpath("//*[contains(text(), 'TERM:')]")
        wd.find_element_by_xpath("//*[contains(text(), 'OWNERSHIP:')]")
        wd.find_element_by_xpath("//*[contains(text(), 'NON-ST SERVICES:')]")
        wd.find_element_by_xpath("//*[contains(text(), 'GENERAL:')]")
        wd.find_element_by_xpath("//*[contains(text(), 'INFORMATION WE COLLECT, TERMS OF USE, AND PRIVACY POLICY:')]")
        wd.find_element_by_xpath("//*[contains(text(), 'NO WARRANTIES, LIMITATIONS ON LIABILITY:')]")
        wd.find_element_by_xpath("//*[contains(text(), 'TERMINATION:')]")
        wd.find_element_by_xpath("//*[contains(text(), 'EQUITABLE REMEDIES:')]")
        wd.find_element_by_xpath("//*[contains(text(), 'GENERAL LEGAL TERMS:')]")

    def eula_terms_of_use_link(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[2]/a[1]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def eula_privacy_policy_link(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[2]/a[2]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def eula_privacy_policy_link2(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                                  '/div[2]/div/div/div/div/p[19]/a').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url