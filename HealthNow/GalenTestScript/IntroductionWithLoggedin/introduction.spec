============================================================
navigation-top        id        top_navigation        
navigation-greenbar   css       #top_navigation .navbartop-green
navigation-header     id        top_navigation_header
navbar-user-icon      css       .user-icon #btn-menu
navbar-user-profile   id        user-profile
name-user-profile     id        user-lblTopHeader
image-user-profile    css       #user-profile .user-img       
logo-hntext-icon      id        divTagline
intro-header-title    css       .header-title
introduction-text     css       .header-title .container .headtext
intro-content-form    css       .content
intro-back-btn        css       .content .buttons #btnBack
intro-next-btn        css       .content .buttons #btnNext
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

intro-header-title
     below: navigation-top -2px top

introduction-text
     inside: intro-header-title 8px bottom
     text is: Introduction

intro-content-form
     below: intro-header-title
     text contains: What happens when patients and families are given the opportunity to chart their progress along side the medical team?

intro-back-btn
     inside: intro-content-form 5px bottom
     text is: Back

intro-next-btn
     inside: intro-content-form 5px bottom
     text is: Next
     aligned horizontally all: intro-back-btn
     
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

intro-header-title
     below: navigation-top -7px top

introduction-text
     inside: intro-header-title 8px bottom
     text is: Introduction

intro-content-form
     below: intro-header-title
     text contains: What happens when patients and families are given the opportunity to chart their progress along side the medical team?

intro-back-btn
     inside: intro-content-form 5px bottom
     text is: Back

intro-next-btn
     inside: intro-content-form 5px bottom
     text is: Next
     aligned horizontally all: intro-back-btn