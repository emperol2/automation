============================================================
navigation-container     id     top_navugation_container
navigation-header     css     #top_navugation_header .navbar-header
logo     id     lnkHNLogo
header     id     lblTopHeader
content-wrapper     id     content-wrapper
text-content-wrapper     id     Resources_PatientRegistration_Hero1
registration     css     #content-wrapper .registration
firstname-field     css     .container #txtFirstName
email-field     css     .container #txtEmail
confirm-button     css     .container #btnConfirm
help-button     css     .container #btnHelp
account-field     id     txtAccountNumber
vc-field     id     txtVC
============================================================
@ all
------------------------------------------------------------
navigation-container
     absent

navigation-header
     absent

logo
     visible
     width: 30px
     height: 30px

header
     text is: Patient Registration
     width: 530px
     height: 41px

content-wrapper
     height: 846px

text-content-wrapper
     centered horizontally inside: content-wrapper 10px
     text is: Review and Confirm Your Registration Data

@ mobile
------------------------------------------------------------
logo
     width: 30px
     height: 30px

registration
     inside: content-wrapper 6px left right, 66px top, 0px bottom
     color scheme: 58% #F5F5F5, 1% #9CB959

firstname-field
     inside: registration 20px left right, 37px top, 719px bottom
     width: 237px
     height: 34px

email-field
     aligned vertically left: firstname-field

confirm-button
     aligned vertically left: firstname-field
     text is: Confirm

help-button
     text is: Help
     aligned horizontally: confirm-button

account-field
     aligned vertically left: firstname-field
     aligned horizontally: vc-field

vc-field
     aligned horizontally: account-field

@ desktop
-----------------------------------------------------------
logo
     width: 30px
     height: 30px

registration
     inside: content-wrapper 6px left right, 50px top, 0px bottom
     color scheme: 56% #F5F5F5, 2% #9CB959

firstname-field
     inside: registration 20px left right, 37px top, 719px bottom
     width: 237px
     height: 34px

email-field
     aligned vertically left: firstname-field

confirm-button
     aligned vertically left: firstname-field
     text is: Confirm

help-button
     text is: Help
     aligned horizontally: confirm-button

account-field
     aligned vertically left: firstname-field
     aligned horizontally: vc-field

vc-field
     aligned horizontally: account-field