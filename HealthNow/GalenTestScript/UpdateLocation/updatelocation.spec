============================================================
navigation-top        id        top_navigation        
navigation-greenbar   css       #top_navigation .navbartop-green
navigation-header     id        top_navigation_header
navbar-user-icon      css       .user-icon #btn-menu
navbar-user-profile   id        user-profile
name-user-profile     id        user-lblTopHeader
image-user-profile    css       #user-profile .user-img       
logo-hntext-icon      id        divTagline
update-home-hero      css       .home-hero
update-location-form  css       .update-location
update-location-btn   id        btnUpdate
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

update-home-hero
     below: navigation-top -2px top

update-location-form
     below: update-home-hero 8px top
     text contains: Where are you now

update-location-btn
     inside: update-location-form 22px bottom

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

update-home-hero
     below: navigation-top -7px top

update-location-form
     below: update-home-hero 8px top
     text contains: Where are you now

update-location-btn
     inside: update-location-form 22px bottom