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

driver.navigate().to("http://qa.healthnow.com/Pages/Profile.aspx");
Thread.sleep(3000);

// View Medication Page
var viewMedication = $.page({
    viewallIssue: "#medicationsPanel .header .pull-right .btn-viewall"
});

viewMedication.viewallIssue.click();

driver.navigate().to("http://qa.healthnow.com/Pages/List/MedicationList.aspx");
Thread.sleep(5000);