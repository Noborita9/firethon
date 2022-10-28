auth_endpoints = {
    "refresh_with_custom_token": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key=",
        "method": "POST",
        "headers": {"content-type": "application/x-www-form-urlencoded"}
    },
    "refresh_token": {
        "url": "https://securetoken.googleapis.com/v1/token?key=",
        "method": "POST",
        "headers": {"content-type": "application/x-www-form-urlencoded"}
    },
    "sign_up_with_email_and_password": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "sign_in_with_email_and_password": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "sign_in_anonymously": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "sign_in_with_oauth_credential": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "fetch_email_providers": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:createAuthUri?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "reset_password_with_email": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "verify_password_reset_with_email": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:createAuthUri?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "confirm_password_reset": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:resetPassword?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "change_email": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:update?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "change_password": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:update?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "update_profile": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:update?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "get_user_data": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "link_with_email_and_password": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:update?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "link_with_oauth_credential": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "unlink_provider": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:update?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "send_email_verification": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "confirm_email_verification": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:update?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
    "delete_account": {
        "url": "https://identitytoolkit.googleapis.com/v1/accounts:delete?key=",
        "method": "POST",
        "headers": {"content-type": "application/json"}
    },
}
