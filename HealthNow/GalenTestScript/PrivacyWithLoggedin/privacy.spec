============================================================
navigation-top        id        top_navigation        
navigation-greenbar   css       #top_navigation .navbartop-green
navigation-header     id        top_navigation_header
navbar-user-icon      css       .user-icon #btn-menu
navbar-user-profile   id        user-profile
name-user-profile     id        user-lblTopHeader
image-user-profile    css       #user-profile .user-img       
logo-hntext-icon      id        divTagline
privacy-head-title    css       .header-title
privacy-head-text     css       .header-title .headtext
privacy-content-form  css       .content
privacy-answer-text   css       .content .answer
privacy-back-btn      css       .content .buttons #btnBack
privacy-next-btn      css       .content .buttons #btnNext
============================================================

@ mobile
------------------------------------------------------------
navigation-top
     width: 306px
     height: 47px

navigation-greenbar
     inside: navigation-top 0px top

navigation-header
     below: navigation-greenbar

navbar-user-icon
     visible
     width: 21px
     height: 21px

navbar-user-profile
     absent

name-user-profile
     absent

image-user-profile
     absent

logo-hntext-icon
     absent

privacy-head-title
     below: navigation-top -2px top

privacy-head-text
     inside: privacy-head-title 25px top
     text is: Privacy and Security

privacy-content-form
     below: privacy-head-title 0px top

privacy-answer-text
     inside: privacy-content-form 82px top
     text contains: You are encouraged to share your completed exercises with your health care team. You can review your answers in person and/or ask for the carbon copies to be placed on your chart. 
     text contains:If you wish to share your answers only with the study team, place the carbon copies

privacy-back-btn
     text is: Back
     inside: privacy-content-form 5px bottom
     below: privacy-answer-text

privacy-next-btn
     text is: Next
     inside: privacy-content-form 5px bottom
     aligned horizontally all: privacy-back-btn

@ tablet
------------------------------------------------------------
navigation-top
     width: 1186px
     height: 52px

navigation-greenbar
     inside: navigation-top 0px top

navigation-header
     below: navigation-greenbar

navbar-user-icon
     visible
     inside: navigation-header 12px top
     below: navigation-greenbar

navbar-user-profile
     width: 211px
     height: 41px
     below: navigation-greenbar

name-user-profile
     visible

image-user-profile
     visible

logo-hntext-icon
     visible
     inside: navigation-top 15px top
     width: 162px
     height: 32px

privacy-head-title
     below: navigation-top -7px top

privacy-head-text
     inside: privacy-head-title 25px top
     text is: Privacy and Security

privacy-content-form
     below: privacy-head-title 0px top

privacy-answer-text
     inside: privacy-content-form 44px top
     text contains: You are encouraged to share your completed exercises with your health care team. You can review your answers in person and/or ask for the carbon copies to be placed on your chart.
     text contains: If you wish to share your answers only with the study team, place the carbon copies

privacy-back-btn
     text is: Back
     inside: privacy-content-form 5px bottom
     below: privacy-answer-text

privacy-next-btn
     text is: Next
     inside: privacy-content-form 5px bottom
     aligned horizontally all: privacy-back-btn