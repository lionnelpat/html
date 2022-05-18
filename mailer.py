import re
import yagmail

YAGMAIL_USERNAME = "dplionnel@gmail.com"
YAGMAIL_PASSWORD = "shmkgmyvvuocpgan"




def is_email_valid(email):
    """
        Check if email is valid
    :param email:
    :return: boolean
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(regex, email):
        return True
    else:
        return False


def send_email(user_email, body):
    """
        send email to user with her bill
    :return: None
    """
    yagmail.register(YAGMAIL_USERNAME, YAGMAIL_PASSWORD)

    try:
        yag = yagmail.SMTP(YAGMAIL_USERNAME)

        yag.send(
            to=user_email,
            subject="Cesag Website ",
            contents=body
        )
    except Exception as e:
        print(e)
    finally:
        print("\nMerci pour votre confiance \n A bientot")
