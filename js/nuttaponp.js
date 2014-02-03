Selenium.prototype.doGetRandomLink = function(variableName) {
	var resultX = new Array();
	//var source = "";
	var source = this.browserbot.getDocument().getElementsByTagName("html")[0].innerHTML;
	//alert(source);
	//var source = "sdfsdfsdfsdfsd sdfsdfdf dfdsfdsfsdf border-radius:";
	//alert(source);
	resultX[0] = source.match(/ctl[0-9]*_ctl[0-9]*_phContent_ctl[0-9]*_ctlRegistrationMainRegistrant_lnkToEdit/g);
	alert(resultX[0]);
	
	//value = resultX[0];
	//ctl00_ctl00_phContent_ctl13_ctlRegistrationMainRegistrant_lnkToEdit
}

Selenium.prototype.doCheckMatch = function(input, variableName) {
	

	var result = new Array();
	var str = new Array();
	//var stringX = "ctl00_ctl00_phContent_ctl"
	//var stringY = "_ctlRegistrationMainRegistrant_lnkToEdit"
	var id = input
	str = id.match("ctl00_ctl00_phContent_ctl");
	var stringX = str[0];

	var str2_lenght = id.length;

	var id_at = id.charAt(26);
	//alert (id_at);
	var check_position_number = id_at.match(/[0-9]*/g);

	if (check_position_number){
		str2 = id.substr(27, str2_lenght);
		//alert ("27 = number: " + str2);
	}else{
		str2 = id.substr(28, str2_lenght);
		//alert ("27 != number: " + str2);
	}

	var stringY = str2;

	var source = this.browserbot.getDocument().getElementsByTagName("html")[0].innerHTML;
	
	for (var i = 0; i < 100; i++){
		var x = i.toString();
		var stringX_X = stringX.concat(x);
		var stringZ = stringX_X.concat(stringY);

		result[0] = source.match(stringZ);

		if (result[0])
		{
			storedVars[variableName] = result[0];
		}

	}
	
}

Selenium.prototype.assertTableRows = function(locator, value) {
  var table = this.browserbot.findElement(locator);
  Assert.matches(value, table.rows.length.toString());
}
