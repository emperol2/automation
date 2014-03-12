==============================================================================
# objects definition
# Login Page
header-top        id       top_navugation
home-hero        css       .home-hero
first-line       css       .home-hero h2
second-line      css       .home-hero p
login-form       css       .login
username-box     css       input#txtUsername
password-box     css       input#txtPassword
buttons          css       .form-group.btnGroup
footer            id       footer
footer-text      css       #footer .row
==============================================================================
# specs definition
# ......

@ desktop

@ Section 1. Testing header | mobile
------------------------------------------------------------------------------
header-top
 inside: screen 0px top
 width: 100% of screen/width

@ Section 2. Testing hero text | mobile
------------------------------------------------------------------------------
first-line
 inside: home-hero < 10 px top
second-line
 below: first-line > 10 px top

@ Section 3. Testing log-in form | mobile
------------------------------------------------------------------------------
login-form
 below: home-hero < 10 px top

@ Section 4. Testing username and password field | mobile
------------------------------------------------------------------------------
username-box
 inside: login-form > 10 px top
password-box
 inside: login-form > 10 px top
 below: login-form < 10 px top

@ Section 5. Testing button and footer | mobile
------------------------------------------------------------------------------
buttons
 below: login-form > 10 px top
footer
 below: buttons > 10 px top

@ Section 6. Testing footer text align center | mobile
------------------------------------------------------------------------------
footer-text
 centered horizontally inside: footer


