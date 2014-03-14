============================================================
navigation-top        id        top_navugation       
navigation-greenbar   css       #top_navigation .navbartop-green
navigation-header     id        top_navigation_header
navbar-user-icon      css       .user-icon #btn-menu
navbar-user-profile   id        user-profile
logo-hntext-icon      id        divTagline
account-setting-tab   css       .home-hero
account-setting-form  css       .accountsetting
login-head-inline     css       .headerinline
login-edit-icon       css       .headereditinline #btnEditLogin
============================================================

@ mobile
------------------------------------------------------------

account-setting-tab
     below: navigation-top -2px top

account-setting-form
     below: account-setting-tab 8px top

login-head-inline
     inside: account-setting-form 9px top
     near: login-edit-icon 119px left

@ tablet
------------------------------------------------------------

account-setting-tab
     below: navigation-top -12px top

account-setting-form
     below: account-setting-tab 8px top

login-edit-icon
     near: login-head-inline 852px right