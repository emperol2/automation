============================================================
navigation-top        id        top_navigation        
navigation-greenbar   css       #top_navigation .navbartop-green
navigation-header     id        top_navigation_header
navbar-user-icon      css       .user-icon #btn-menu
navbar-user-profile   id        user-profile
name-user-profile     id        user-lblTopHeader
image-user-profile    css       #user-profile .user-img       
logo-hntext-icon      id        divTagline
instruction-title     css       .header-title
instruction-text      css       .header-title .headtext
instruction-content   css       .content
instruction-back-btn  css       .content #btnBack
instruction-next-btn  css       .content #btnNext
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

instruction-title
     below: navigation-top -2px top

instruction-text
     text is: Instructions
     inside: instruction-title 8px bottom

instruction-content
     below: instruction-title 0px top
     text contains: We are conducting a study to answer this question. Thank you for accepting our invitation to participate
     above: instruction-back-btn -43px bottom

instruction-back-btn
     text is: Back
     inside: instruction-content 35px left
     aligned horizontally all: instruction-next-btn

instruction-next-btn
     text is: Next
     inside: instruction-content 35px right

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
     width: 200px
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

instruction-title
     below: navigation-top -7px top

instruction-text
     text is: Instructions
     inside: instruction-title 8px bottom

instruction-content
     below: instruction-title 0px top
     text contains: We are conducting a study to answer this question. Thank you for accepting our invitation to participate
     above: instruction-back-btn -43px bottom

instruction-back-btn
     text is: Back
     inside: instruction-content 130px left
     aligned horizontally all: instruction-next-btn

instruction-next-btn
     text is: Next
     inside: instruction-content 130px right