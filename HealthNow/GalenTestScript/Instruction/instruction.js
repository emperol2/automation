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

// Privacy Page
var instruction = $.page({
    introPage: "#lnkQuiz",
    privacyPage: "#btnNext",
    baseLinePage: "#btnNext",
    instructionPage: "#btnNext"
});

instruction.introPage.click();
driver.navigate().to("http://qa.healthnow.com/Pages/Introduction/Introduction.aspx");
Thread.sleep(3000);

instruction.privacyPage.click();
driver.navigate().to("http://qa.healthnow.com/Pages/Introduction/Privacy.aspx");
Thread.sleep(3000);

instruction.baseLinePage.click();
driver.navigate().to("http://qa.healthnow.com/Pages/Measurements/Baseline.aspx");
Thread.sleep(3000);

instruction.instructionPage.click();
driver.navigate().to("http://qa.healthnow.com/Pages/Introduction/Instructions.aspx");
Thread.sleep(7000);