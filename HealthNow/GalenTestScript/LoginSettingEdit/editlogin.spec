============================================================
navigation-top        id        top_navigation        
navigation-greenbar   css       #top_navigation .navbartop-green
navigation-header     id        top_navigation_header
navbar-user-icon      css       .user-icon #btn-menu
navbar-user-profile   id        user-profile
name-user-profile     id        user-lblTopHeader
image-user-profile    css       #user-profile .user-img       
logo-hntext-icon      id        divTagline
editlogin-home-hero   css       .home-hero
editlogin-form        css       .accountsetting
editlogin-username    id        txtUsername
editlogin-currentpw   id        txtCurrentPassword
editlogin-cancelbtn   id        btnCancel
editlogin-savebtn     id        btnSave
============================================================

@ mobile
------------------------------------------------------------
navigation-top
     width: 289px
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

editlogin-home-hero
     below: navigation-header -1px top

editlogin-form
     below: editlogin-home-hero 8px top

editlogin-username
     inside: editlogin-form 34px top

editlogin-currentpw
     aligned vertically left: editlogin-username

editlogin-cancelbtn
     aligned vertically left: editlogin-username
     near: editlogin-savebtn -236px right

editlogin-savebtn
     aligned horizontally top: editlogin-cancelbtn
     near: editlogin-cancelbtn -236px left

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
     width: 175px
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

editlogin-home-hero
     below: navigation-header -6px top

editlogin-form
     below: editlogin-home-hero 8px top

editlogin-username
     inside: editlogin-form 34px top

editlogin-currentpw
     aligned vertically left: editlogin-username

editlogin-cancelbtn
     aligned vertically left: editlogin-username
     near: editlogin-savebtn -954px right

editlogin-savebtn
     aligned horizontally top: editlogin-cancelbtn
     near: editlogin-cancelbtn -954px left