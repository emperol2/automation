============================================================
navigation-top        id        top_navigation        
navigation-greenbar   css       #top_navigation .navbartop-green
navigation-header     id        top_navigation_header
navbar-user-icon      css       .user-icon #btn-menu
navbar-user-profile   id        user-profile
logo-hntext-icon      id        divTagline
============================================================

@ tablet
------------------------------------------------------------
navigation-top
     width: 1039px
     height: 51px

navigation-greenbar
     inside: navigation-top 0px top

navigation-header
     below: navigation-greenbar

navbar-user-icon
     inside: navigation-header 11px top
     below: navigation-greenbar

navbar-user-profile
     width: 176px
     height: 41px
     below: navigation-greenbar

logo-hntext-icon
     visible
     inside: navigation-top 10px top
	 
@ mobile
------------------------------------------------------------
navigation-top
     width: 1039px
     height: 51px

navigation-greenbar
     inside: navigation-top 0px top

navigation-header
     below: navigation-greenbar

navbar-user-icon
     absent

navbar-user-profile
     visible
     width: 176px
     height: 41px
     below: navigation-greenbar

logo-hntext-icon
     absent