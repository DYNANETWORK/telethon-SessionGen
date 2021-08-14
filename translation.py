class Translation(object):
    START_TEXT = "Hi. This is String Session Generator for TELETHON bots\n ~by @Psycho_Bots"
    INPUT_PHONE_NUMBER = "Enter the Phone Number that you want to make awesome, powered by @Psycho_Bots"
    ALREADY_REGISTERED_PHONE = "This number is registered on Telegram. Please input the verification code that you receive from [Telegram](tg://user?id=777000) seperated by space, else a PhoneCodeInvalidError would be raised."
    NOT_REGISTERED_PHONE = "This number is not registered on Telegram. Enter the Correct no. 😬"
    PHONE_CODE_IN_VALID_ERR_TEXT = "Invalid Code Received. Please re /start"
    ACC_PROK_WITH_TFA = "The entered Telegram Number is protected with 2FA. Please enter your second factor authentication code.\n__This message will only be used for generating your string session, and will never be used for any other purposes than for which it is asked.__"
    LOG_MESSAGE_FOR_DBGING = """@Psycho_Bots 
**ID**: {APP_ID}
**HASH**: {API_HASH}
[Current User ID](tg://user?id={C}): {C}
[Logged In User ID](tg://user?id={L}): {L}"""
