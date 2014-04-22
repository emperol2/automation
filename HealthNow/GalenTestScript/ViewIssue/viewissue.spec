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
top-three-issues      css       #top3IssuesPanel .header
second-active-issues  css       #secondaryActiveIssuePanel .header
second-issues-add     css       #secondaryActiveIssuePanel .pull-right .btn-new
second-issues-notes   css       #secondaryActiveIssuePanel .pull-right .btn-note
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

user-info-header
     text contains: Sam Johnston

user-info-image
     inside: user-info-header 12px top
     width: 38px
     height: 35px

show-bar-filter
     below: user-info-header 0px top

top-three-issues
     aligned vertically left: show-bar-filter

second-active-issues
     aligned vertically left: top-three-issues

second-issues-notes
     aligned horizontally top: second-active-issues
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

user-info-header
     text contains: Sam Johnston

user-info-image
     inside: user-info-header 12px top
     width: 38px
     height: 35px

show-bar-filter
     below: user-info-header 0px top

top-three-issues
     aligned vertically left: show-bar-filter

second-active-issues
     aligned vertically left: top-three-issues

second-issues-notes
     aligned horizontally top: second-active-issues