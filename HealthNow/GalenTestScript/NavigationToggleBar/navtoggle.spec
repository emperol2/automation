============================================================
navigation-top-toggle id        top_navigation        
navigation-greenbar   css       #top_navigation .navbartop-green
navigation-header     id        top_navigation_header
navbar-user-icon      css       .user-icon #btn-menu
navbar-user-profile   id        user-profile
name-user-profile     id        user-lblTopHeader
image-user-profile    css       #user-profile .user-img       
logo-hntext-icon      id        divTagline
navbar-collapse       css       .navbar-collapse
navbar-updatelocal    id        lnkChangeLocation
navbar-accountset     id        lnkAccountSetting
navbar-logout-tab     id        lnkLogout
============================================================

@ mobile
------------------------------------------------------------
navigation-top-toggle
     width: 289px
     height: 171px

navigation-greenbar
     inside: navigation-top-toggle 0px top

navigation-header
     below: navigation-greenbar

navbar-user-icon
     visible
     width: 21px
     height: 20px

navbar-user-profile
     absent

name-user-profile
     absent

image-user-profile
     absent

logo-hntext-icon
     absent

navbar-collapse
     below: navigation-header 0px top

navbar-updatelocal
     above: navbar-accountset 1px top

navbar-accountset
     below: navbar-updatelocal 1px top

navbar-logout-tab
     below: navbar-accountset 1px top

@ tablet
------------------------------------------------------------
navigation-top-toggle
     width: 1186px
     height: 176px

navigation-greenbar
     inside: navigation-top-toggle 0px top

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
     inside: navigation-top-toggle 15px top
     width: 162px
     height: 32px

navbar-collapse
     below: navigation-header 0px top

navbar-updatelocal
     above: navbar-accountset 1px top

navbar-accountset
     below: navbar-updatelocal 1px top

navbar-logout-tab
     below: navbar-accountset 1px top