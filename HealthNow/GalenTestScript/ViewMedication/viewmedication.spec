============================================================
navigation-top        id        top_navigation        
navigation-greenbar   css       #top_navigation .navbartop-green
navigation-header     id        top_navigation_header
navbar-user-icon      css       .user-icon #btn-menu
navbar-user-profile   id        user-profile
name-user-profile     id        user-lblTopHeader
image-user-profile    css       #user-profile .user-img       
logo-hntext-icon      id        divTagline
user-info-header      css       .top-user-info
user-info-image       css       .btn-team-menu .img-responsive
show-bar-filter       css       #filter .container
current-medication    css       #currentMedicationsPanel .header
current-mdc-add       css       #currentMedicationsPanel .pull-right .btn-new
current-mdc-notes     css       #currentMedicationsPanel .pull-right .btn-note
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

user-info-header
     text contains: Sam Johnston

user-info-image
     inside: user-info-header 12px top
     width: 38px
     height: 35px

show-bar-filter
     below: user-info-header 0px top

current-medication
     below: show-bar-filter 0px top
     contains: current-mdc-notes

current-mdc-add
     absent

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

user-info-header
     text contains: Sam Johnston

user-info-image
     inside: user-info-header 12px top
     width: 38px
     height: 35px

show-bar-filter
     below: user-info-header 0px top

current-medication
     below: show-bar-filter 0px top
     contains: current-mdc-notes

current-mdc-add
     absent
