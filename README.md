Query FitBit via [python-fitbit](https://github.com/orcasgit/python-fitbit), to retrieve steps from a certain date.

    # Install python-fitbit
    sudo pip install fitbit
   
    # Get API access for your app
    git@github.com:orcasgit/python-fitbit.git
    python python-fitbit/gather_keys_cli.py CONSUMER_KEY CONSUMER_SECRET_KEY
   
    # If done correctly output should look like this (tokens replaced with 0's)
    ** OAuth Python Library Example **
    
    * Obtain a request token ...
    
    RESPONSE
    {   u'oauth_callback_confirmed': u'true',
        u'oauth_token': u'00000000000000000000000',
        u'oauth_token_secret': u'00000000000000000000000'}
    
    * Authorize the request token in your browser
    
    Verifier: ACCESS_KEY_YOU_GET_AFTER_LOGGING_IN
    
    * Obtain an access token ...
    
    RESPONSE
    {   u'encoded_user_id': u'USER_ID_YOU_NEED_THIS',
        u'oauth_token': u'USER_KEY_YOU_NEED_THIS',
        u'oauth_token_secret': u'USER_SECRET_KEY_YOU_NEED_THIS'}
    
    Done.

    # Create a secret.py
    touch secret.py
  
    # secret.py should look like this
    CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
    CONSUMER_SECRET_KEY = 'YOUR_CONSUMER_SECRET_KEY'
  
    USER_KEY = {
        'ACCOUNT_NAME': 'USER_KEY_YOU_NEED_THIS'
    }
  
    USER_SECRET_KEY = {
        'ACCOUNT_NAME': 'USER_SECRET_KEY_YOU_NEED_THIS'
    }
  
    USER_ID = {
        'ACCOUNT_NAME': 'USER_ID_YOU_NEED_THIS'
    }
    
    # Example usage get steps
    python fitbit-steps.py --date 2014-10-12 --name robert

