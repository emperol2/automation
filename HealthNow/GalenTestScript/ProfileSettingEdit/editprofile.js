// Include the GalenJs library
load("../galenjs.js");

// Create a GalenJs instance from driver
var $ = GalenJs.create(driver);

// Create a login page object
var homeLogin = $.page({
    username:      "#txtUsername",
    password:   "#txtPassword",
    login:     "#btnLogin"
});

// Perform login flow
homeLogin.username.typeText("papajohn_jr");
homeLogin.password.typeText("1981papajohn_jr");
homeLogin.login.click();

driver.navigate().to("http://qa.healthnow.com/pages/profile.aspx");
Thread.sleep(3000);

// Account Setting Page
var accountPage = $.page({
    navToggle: ".user-icon #btn-menu",
    accountSetting: "#lnkAccountSetting"
});

accountPage.navToggle.click();
accountPage.accountSetting.click();

driver.navigate().to("http://qa.healthnow.com/Pages/AccountSetting.aspx");
Thread.sleep(3000);

// Profile Setting Edit Page
var profileSettingEdit = $.page({
    editProfile: ".headereditinline #btnEditProfile"
});

profileSettingEdit.editProfile.click();

driver.navigate().to("http://qa.healthnow.com/Pages/PatientRegistration.aspx");
Thread.sleep(5000);