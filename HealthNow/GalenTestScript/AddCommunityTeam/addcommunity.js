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

// Health Team List Page with add community team
var addCommunity = $.page({
    healthTeamPage: ".btn-team-menu .img-responsive",
    addCommunityPage: "#communityTeam #btnAddTeam01"
});

addCommunity.healthTeamPage.click();
driver.navigate().to("http://qa.healthnow.com/Pages/List/HealthteamList.aspx");
Thread.sleep(3000);

addCommunity.addCommunityPage.click();
driver.navigate().to("http://qa.healthnow.com/Pages/ProviderDetail.aspx");
Thread.sleep(5000);