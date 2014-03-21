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

// Declare URL for each page
var profileLink = "https://my.healthnow.net/Pages/Profile.aspx"
var introductionLink = "https://my.healthnow.net/Pages/Introduction/Introduction.aspx"
var accountSettingLink = "https://my.healthnow.net/pages/AccountSetting.aspx"


if (driver.getCurrentUrl() == "https://my.healthnow.net/Pages/Introduction/Introduction.aspx")
{
	driver.navigate().to("https://my.healthnow.net/Pages/Login.aspx");
	homeLogin.username.typeText("sam2014");
	homeLogin.password.typeText("papajohn");
	homeLogin.login.click();
	driver.navigate().to("https://my.healthnow.net/Pages/Introduction/Introduction.aspx");
}

if (driver.getCurrentUrl() != "https://my.healthnow.net/Pages/Introduction/Introduction.aspx"){
	// Perform login flow
	homeLogin.username.typeText("sam2014");
	homeLogin.password.typeText("papajohn");
	homeLogin.login.click();
}

//driver.navigate().to(profileLink);
Thread.sleep(3000);

// Include homelogin
//load("../homelogin.spec");

//var location = profileLink;

var currentURL = driver.getCurrentUrl();

//var currentLocation = window.location;

if(currentURL == "https://my.healthnow.net/Pages/Profile.aspx"){
	var number = 1;
}else if (currentURL == "https://my.healthnow.net/Pages/Introduction/Introduction.aspx"){
	var number = 2;
}else if (currentURL == "https://my.healthnow.net/pages/AccountSetting.aspx"){
	var number = 3;
}else{
	var number = 4;
}

switch(number)
{
case 1:
	break;
	
case 2:
	// Introduction Page
	//var introduction = $.page({
		//introPage: "#lnkQuiz"
	//});

	//introduction.introPage.click();

	//driver.navigate().to(introductionLink);
	Thread.sleep(5000);
	
	break;
	
case 3:
	//var accountSetting = $.page({
	//accountPatient: ".select-patient-lnk .img-responsive"
	//});

	//accountSetting.accountPatient.click();

	driver.navigate().to("https://my.healthnow.net/pages/AccountSetting.aspx");
	Thread.sleep(5000);

	break;
	
default:
	break;

}