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
var accountSetting = $.page({
    accountPatient: ".select-patient-lnk .img-responsive"
});

accountSetting.accountPatient.click();

driver.navigate().to("http://qa.healthnow.com/pages/AccountSetting.aspx");
Thread.sleep(5000);