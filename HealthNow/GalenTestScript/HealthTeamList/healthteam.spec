============================================================
navigation-top        id        top_navigation        
navigation-greenbar   css       #top_navigation .navbartop-green
navigation-header     id        top_navigation_header
navbar-user-icon      css       .user-icon #btn-menu
navbar-user-profile   id        user-profile
name-user-profile     id        user-lblTopHeader
image-user-profile    css       #user-profile .user-img       
logo-hntext-icon      id        divTagline
community-team-form   id        communityTeam
inpatient-team-form   id        inpatientTeam
add-community-team    id        btnAddTeam01
add-inpatient-team    id        btnAddTeam02
community-header      css       #communityTeam .header #header
inpatient-header      css       #inpatientTeam .header #header
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

community-team-form
     below: navigation-top -2px top

inpatient-team-form
     below: community-team-form 0px top

add-community-team
     near: community-header 104px right

add-inpatient-team
     near: inpatient-header 122px right

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

community-team-form
     below: navigation-top -7px top

inpatient-team-form
     below: community-team-form 0px top

add-community-team
     near: community-header 785px right

add-inpatient-team
     near: inpatient-header 803px right