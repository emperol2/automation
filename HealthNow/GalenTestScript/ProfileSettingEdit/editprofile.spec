============================================================
navigation-top        id        top_navigation        
navigation-greenbar   css       #top_navigation .navbartop-green
navigation-header     id        top_navigation_header
navbar-user-icon      css       .user-icon #btn-menu
navbar-user-profile   id        user-profile
name-user-profile     id        user-lblTopHeader
image-user-profile    css       #user-profile .user-img       
logo-hntext-icon      id        divTagline
editprofile-home-hero css       .home-hero
editprofile-form      css       .registration
editprofile-firstname id        txtFirstName
editprofile-accnum    id        txtAccountNumber
editprofile-vc        id        txtVC
editprofile-date-adm  id        txtDOA
editprofile-confirm   id        btnConfirm
editprofile-help      id        btnHelp
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

editprofile-home-hero
     below: navigation-top -2px top
     text is: Edit Profile

editprofile-form
     below: editprofile-home-hero 8px top

editprofile-date-adm
     aligned vertically left: editprofile-firstname

editprofile-accnum
     aligned horizontally top: editprofile-vc

editprofile-help
     aligned horizontally top: editprofile-confirm
@ tablet
------------------------------------------------------------
navigation-top
     width: 1169px
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

editprofile-home-hero
     below: navigation-top -7px top
     text is: Edit Profile

editprofile-form
     below: editprofile-home-hero 8px top

editprofile-date-adm
     aligned vertically left: editprofile-firstname

editprofile-accnum
     aligned horizontally top: editprofile-vc

editprofile-help
     aligned horizontally top: editprofile-confirm