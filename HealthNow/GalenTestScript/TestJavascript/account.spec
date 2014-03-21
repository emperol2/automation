============================================================
navigation-top        id        top_navigation       
navigation-greenbar   css       #top_navigation .navbartop-green
navigation-header     id        top_navigation_header
navbar-user-icon      css       .user-icon #btn-menu
name-user-profile     id        user-lblTopHeader
image-user-profile    css       #user-profile .user-img
logo-hntext-icon      id        divTagline
hnlogo-icon-header    id        lnkHNLogo
user-profile-mobile   id        lblTopHeader
account-setting-tab   css       .home-hero
account-setting-form  css       .accountsetting
login-head-inline     css       .headerinline
login-edit-icon       css       .headereditinline #btnEditLogin
profile-image-set     css       .labelinline #profileimg
profile-info-set      css       .valueinline #profile
============================================================

@ mobile
------------------------------------------------------------

navbar-user-icon
     visible

name-user-profile
     absent

image-user-profile
     absent

logo-hntext-icon
     absent

hnlogo-icon-header
     visible
     inside: navigation-header 6px top, 9px left

user-profile-mobile
     visible
     centered all inside: navigation-header

account-setting-tab
     below: navigation-top -2px top

account-setting-form
     below: account-setting-tab 8px top

login-head-inline
     inside: account-setting-form 9px top
     near: login-edit-icon 119px left

profile-image-set
     inside: account-setting-form 206px top
     width: 65px
     height: 65px

profile-info-set
     inside: account-setting-form 273px top
     near: profile-image-set 0px right

@ tablet
------------------------------------------------------------

navbar-user-icon
     visible

name-user-profile
     visible

image-user-profile
     visible

logo-hntext-icon
     visible
     near: hnlogo-icon-header 7px right

hnlogo-icon-header
     visible
     inside: navigation-header 6px top, 9px left

user-profile-mobile
     absent

account-setting-tab
     below: navigation-top -7px top

account-setting-form
     below: account-setting-tab 8px top

login-edit-icon
     near: login-head-inline 852px right

profile-image-set
     inside: account-setting-form 186px top
     width: 65px
     height: 65px

profile-info-set
     inside: account-setting-form 210px top
     near: profile-image-set 14px right