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
homeLogin.username.typeText("sam2014");
homeLogin.password.typeText("papajohn");
homeLogin.login.click();

driver.navigate().to("https://my.healthnow.net/Pages/profile.aspx");
Thread.sleep(3000);

// Health Team List Page
var healthTeamList = $.page({
    healthTeamImg: ".btn-team-menu .img-responsive"
});

healthTeamList.healthTeamImg.click();

driver.navigate().to("https://my.healthnow.net/Pages/List/HealthteamList.aspx");
Thread.sleep(5000);