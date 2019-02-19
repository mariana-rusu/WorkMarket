Environment and framework configuration

Browser and driver configuration
    1. Installed version of browser:   Google Chrome Version 72.0.3626.109
    2. Install chrome driver by following instructions http://jonathansoma.com/lede/foundations-2017/classes/more-scraping/selenium/
Testing environment
    1. Install python http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/
    2. Install pip https://pip.pypa.io/en/stable/installing/
    3. Required packages in requirements.txt run:
        pip install -r requirements.txt

How to run tests:
    1. export environment variables:
        export email=service_account@email.com password=service_account_password qa_env=dev
    2. execute:
        python run.py

Results:
    As a result in current directory you should find a file with name: yyyy-mm-dd-report.html