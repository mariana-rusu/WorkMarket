import os
class SignUpSettings:
    qa_env = os.environ["qa_env"]
    url = "https://{}.workmarket.com/register/campaign/10081C503B209A0C8E7F05FDCC1AA98D4C904DEEF5F73265CAE38C744E7EAD3E"\
        .format(qa_env)
