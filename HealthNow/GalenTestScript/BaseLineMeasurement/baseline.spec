============================================================
navigation-top        id        top_navigation        
navigation-greenbar   css       #top_navigation .navbartop-green
navigation-header     id        top_navigation_header
navbar-user-icon      css       .user-icon #btn-menu
navbar-user-profile   id        user-profile
name-user-profile     id        user-lblTopHeader
image-user-profile    css       #user-profile .user-img       
logo-hntext-icon      id        divTagline
baseline-head-title   css       .header-title
baseline-head-text    css       .header-title .headtext
baseline-content-form css       .content
baseline-questions    css       .content .questions
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

baseline-head-title
     below: navigation-top -2px top

baseline-head-text
     text is: Baseline Measurement
     inside: baseline-head-title 8px bottom

baseline-content-form
     below: baseline-head-title 0px top

baseline-questions
     inside: baseline-content-form 223px top
     width: 219px
     height: 242px

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

baseline-head-title
     below: navigation-top -7px top

baseline-head-text
     text is: Baseline Measurement
     inside: baseline-head-title 8px bottom

baseline-content-form
     below: baseline-head-title 0px top

baseline-questions
     inside: baseline-content-form 90px top
     width: 940px
     height: 182px