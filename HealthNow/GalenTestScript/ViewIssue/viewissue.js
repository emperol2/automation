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

// View Issue Page
var viewIssue = $.page({
    viewallIssue: ".btn-viewall"
});

viewIssue.viewallIssue.click();

driver.navigate().to("http://qa.healthnow.com/Pages/List/Issuelist.aspx");
Thread.sleep(5000);