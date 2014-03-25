============================================================
navigation-top        id        top_navigation        
navigation-greenbar   css       #top_navigation .navbartop-green
navigation-header     id        top_navigation_header
navbar-user-icon      css       .user-icon #btn-menu
navbar-user-profile   id        user-profile
name-user-profile     id        user-lblTopHeader
image-user-profile    css       #user-profile .user-img       
logo-hntext-icon      id        divTagline
add-new-contact-head  css       #content-wrapper .provider-detail .lato
provider-contact-card css       .container .form-group
image-link-icon       css       #A7 .img-responsive
name-detail-contact   css       .detail .container .form-group
how-can-reach-them    css       .lato .container
detail-reach-them     css       .detail #data_contact_list
associated-role       xpath     /html/body/form/div[2]/div[2]/div/div[7]/div
associated-detail-1   css       .detail .tabs #tab-1
associated-detail-2   css       .detail .tabs #tab-2
associated-trust-sub  css       .detail .tabs-content
asso-another-btn      id        btnAddAnother       
============================================================

@ mobile
------------------------------------------------------------
navigation-greenbar
     inside: navigation-top 0px top
	 
navigation-top
     visible
	 
navigation-header
     absent

navbar-user-icon
     absent

navbar-user-profile
     absent
	 
name-user-profile
     absent

image-user-profile
     absent
	 
logo-hntext-icon
     absent

add-new-contact-head
     below: navigation-greenbar 0px top

provider-contact-card
     below: add-new-contact-head 7px top
     text is: Provider Contact Card
     near: image-link-icon -269px right

name-detail-contact
     below: provider-contact-card 10px top
     text is: Name

detail-reach-them
     below: how-can-reach-them 167px top

associated-role 
     below: detail-reach-them 3px top
     text is: Associated Role(s)

associated-detail-1
    text is: Family and Friends
    near: associated-detail-2 -270px right

associated-detail-2
    text is: Health Professionals
    near: associated-detail-1 -270px left

associated-trust-sub
    below: associated-role 35px top

asso-another-btn
    below: associated-trust-sub 0px top
    text is: Add Another Contact

@ tablet
------------------------------------------------------------
navigation-greenbar
     inside: navigation-top 0px top

navigation-top
     visible
	 
navigation-header
     absent

navbar-user-icon
     absent

navbar-user-profile
     absent
	 
name-user-profile
     absent

image-user-profile
     absent
	 
logo-hntext-icon
     absent

add-new-contact-head
     below: navigation-greenbar 0px top

provider-contact-card
     below: add-new-contact-head 7px top
     text is: Provider Contact Card
     near: image-link-icon -970px right

name-detail-contact
     below: provider-contact-card 10px top
     text is: Name

detail-reach-them
     below: how-can-reach-them 147px top

associated-role 
     below: detail-reach-them 3px top
     text is: Associated Role(s)

associated-detail-1
    text is: Family and Friends
    near: associated-detail-2 -950px right

associated-detail-2
    text is: Health Professionals
    near: associated-detail-1 -950px left

associated-trust-sub
    below: associated-role 35px top

asso-another-btn
    below: associated-trust-sub 0px top
    text is: Add Another Contact
