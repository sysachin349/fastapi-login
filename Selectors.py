class Yahoo_selector():
    def __init__(self):
        self.subject="snbajsnasasasklaska"
        self.url='https://mail.yahoo.com/'
        self.userName='//*[@id="login-username"]'
        self.password='//*[@id="login-passwd"]'
        self.inbox='//span[contains(@title,"Inbox") and @class="D_F W_6D6F ab_C i_6FIA p_R o_h G_e J_x Q_689y" ]//span'
        self.spam='//span[contains(@title,"Spam")]//span'
        self.InboxMail='''//span[@data-test-id="message-subject" and @title="%s"]''' %self.subject
        self.SpamMail='''//span[@data-test-id="message-subject" and @title="%s"]''' %self.subject
        self.notSpam='''//span[contains(text(),"Not Spam")]'''
        