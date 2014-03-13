============================================================
navigation-top        id        top_navigation        
navigation-greenbar   css       #top_navigation .navbartop-green
navigation-header     id        top_navigation_header
navbar-user-icon      css       .user-icon #btn-menu
navbar-user-profile   id        user-profile
logo-hntext-icon      id        divTagline
community-team        id        communityTeam
inpatient-team        id        inpatientTeam
============================================================

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
     inside: navigation-header 12px top
     below: navigation-greenbar

navbar-user-profile
     width: 178px
     height: 41px
     below: navigation-greenbar

logo-hntext-icon
     visible
     inside: navigation-top 15px top
     width: 162px
     height: 32px
	 
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

logo-hntext-icon
     absent

community-team
     below: navigation-top -2px top

inpatient-team
     below: community-team 0px top