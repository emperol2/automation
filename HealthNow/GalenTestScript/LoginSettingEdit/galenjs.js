/*******************************************************************************
 * Copyright 2013 Ivan Shubin http://galenframework.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ******************************************************************************/


String.prototype.trim=function(){return this.replace(/^\s+|\s+$/g, '');};

function parseLocator(locatorText) {
    var index = locatorText.indexOf(":");
    if (index > 0 ) {
        var typeText = locatorText.substr(0, index).trim();
        var value = locatorText.substr(index + 1, locatorText.length - 1 - index).trim();
        var type = "css";
        if (typeText == "id") {
            type = typeText;
        }
        else if (typeText == "xpath") {
            type = typeText;
        }
        else if (typeText == "css") {
            type = typeText;
        }
        else {
            throw "Unknown locator type: " + typeText;
        }

        return {
            type: type,
            value: value
        };
    }
    else return {
        type: "css",
        value: locatorText
    };
}

function _galenJs_component(mainFields, secondaryFields) {
    var result = {
        driver: this.driver,
        findChild: function (locator) {
            if (this.parent != undefined ) {
                return this.parent.findChild(locator);
            }
            else {
                try {
                    var element = this.driver.findElement(GalenJs.convertLocator(locator));
                    if (element == null) {
                        throw "No such element: " + locator.type + " " + locator.value; 
                    }
                    return element;
                }
                catch(error) {
                    throw "No such element: " + locator.type + " " + locator.value; 
                }
            }
        },
        findChildren: function (locator) {
            if (this.parent != undefined ) {
                return this.parent.findChildren(locator);
            }
            else {
                return this.driver.findElements(GalenJs.convertLocator(locator));
            }
        },
        waitTimeout: "10s",
        waitPeriod: "1s",
        set: function (props) {
            for (var property in props) {
                if (props.hasOwnProperty(property)) {
                    this[property] = props[property];
                }
            }
            return this;
        },
        waitForIt: function () {
            if (this.primaryFields.length > 0 ) {
                var conditions = {};
                var primaryFields = this.primaryFields;
                var page = this;

                for (var i = 0; i<this.primaryFields.length; i++) {
                    conditions[this.primaryFields[i] + " to be displayed"] = {
                        field: this[this.primaryFields[i]],
                        apply: function () {
                            return this.field.exists();
                        }
                    };
                }

                GalenJs.wait({time: this.waitTimeout, period: this.waitPeriod, message: "timeout waiting for page elements:"}).untilAll(conditions);
            }
            else throw "You can't wait for page as it does not have any fields defined";
            return this;
        }
    }

    var createElement = function (locatorText, parent) {
        return {
            cachedWebElement: null,
            locator: parseLocator(locatorText),
            parent: parent,
            isEnabled: function () {
                return this.getWebElement().isEnabled();
            },
            attribute: function(attrName) {
                return this.getWebElement().getAttribute(attrName);
            },
            cssValue: function (cssProperty) {
                return this.getWebElement().getCssValue(cssProperty);
            },
            click: function () {
                this.getWebElement().click();
            },
            typeText: function (text) {
                this.getWebElement().sendKeys(text);
            },
            clear: function () {
                this.getWebElement().clear();
            },
            getWebElement: function () {
                if (this.cachedWebElement == null) {
                    this.cachedWebElement = this.parent.findChild(this.locator);
                }
                return this.cachedWebElement;
            },
            isDisplayed: function () {
                return this.getWebElement().isDisplayed();
            },
            selectByValue: function (value) {
                var option = this.getWebElement().findElement(By.xpath(".//option[@value=\"" + value + "\"]"));
                if (option != null) {
                    option.click();
                }
                else throw "Cannot find option with value \"" + value + "\"";
            },
            selectByText: function (text) {
                var option = this.getWebElement().findElement(By.xpath(".//option[normalize-space(.)=\"" + text + "\"]"));
                if (option != null) {
                    option.click();
                }
                else throw "Cannot find option with text \"" + value + "\"";
            },
            waitFor: function(func, messageSuffix, time) {
                time = typeof time !== 'undefined' ? time : "10s";
                var name = typeof this.name !== 'undefined' ? this.name : "";
                var msg =  name + " " + messageSuffix;
                var thisElement = this;
                var conditions = {};
                conditions[msg] = function (){
                    return func(thisElement);
                };
                GalenJs.wait({time: time, period: 200}).untilAll(conditions);
            },
            waitToBeShown: function (time) {
                this.waitFor(function (thisElement){
                    return thisElement.exists() && thisElement.isDisplayed();
                }, "should be shown", time);
            },
            waitToBeHidden: function (time) {
                this.waitFor(function (thisElement){
                    return !thisElement.exists() || !thisElement.isDisplayed();
                }, "should be hidden", time);
            },
            waitUntilExists: function (time) {
                this.waitFor(function (thisElement){
                    return thisElement.exists();
                }, "should exist", time);
            },
            waitUntilGone: function (time) {
                this.waitFor(function (thisElement){
                    return !thisElement.exists();
                }, "should not exist", time);
            },
            exists: function () {
                try {
                    this.getWebElement();
                }
                catch(error) {
                    return false;
                }
                return true;
            }
        };
    };

    var iterateOverFields = function (fields, apply) {
        if (fields != undefined) {
            for (var property in fields) {
                if (fields.hasOwnProperty(property)) {
                    var value = fields[property];
                    if (typeof value == "string") {
                        result[property] = createElement(value, result);
                        result[property].name = property;
                        apply(property);
                    }
                    else {
                        result[property] = value;
                    }
                }
            }
        }
    }

    var primaryFields = [];

    iterateOverFields(mainFields, function (property) {
        primaryFields[primaryFields.length] = property;
    });

    result.primaryFields = primaryFields;

    iterateOverFields(secondaryFields, function (property) {});

    return result;
}

function _galenJs_use() {
}

var GalenJs = {
    create: function (driver) {
        return {
            driver: driver,
            page: _galenJs_component,
            component: _galenJs_component,
            use: _galenJs_use,

            //basic functions
            get: function (url){this.driver.get(url);},
            refresh: function () {this.driver.navigate().reload();},
            back: function (){this.driver.navigate().back();},
            currentUrl: function (){return this.driver.getCurrentUrl();},
            pageSource: function () {return this.driver.getPageSource();},
            title: function () {return this.driver.getTitle();}


        };
    },

    convertLocator: function(galenLocator) {
        if (galenLocator.type == "id") {
            return By.id(galenLocator.value);
        }
        else if (galenLocator.type == "css") {
            return By.cssSelector(galenLocator.value);
        }
        else if (galenLocator.type == "xpath") {
            return By.xpath(galenLocator.value);
        }
    },

    convertTimeToMillis: function (userTime) {
        if (typeof userTime == "string") {
            var number = parseInt(userTime);
            var type = userTime.replace(new RegExp("([0-9]| )", "g"), "");
            if (type == "") {
                return number;
            }
            else {
                if (type == "m") {
                    return number * 60000;
                }
                else if(type == "s") {
                    return number * 1000;
                }
                else throw "Cannot convert time. Uknown metric: " + type;
            }
        }
        else return userTime;
    },

    wait: function (settings) {
        if (settings.time == undefined) {
            throw "time was not defined";
        }

        var period = settings.period;
        if (period == undefined) {
            period = 1000;
        }

        var message = null;


        if (typeof settings.message == "string") {
            message = settings.message;
        }
        else message = "timeout error waiting for:"

        return {
            time: GalenJs.convertTimeToMillis(settings.time),
            period:  GalenJs.convertTimeToMillis(period),
            message: message,

            //conditions is a map of functions which should return boolean
            untilAll: function (conditions) {
                var waitFuncs = [];
                for (var property in conditions) {
                    if (conditions.hasOwnProperty(property)) {
                        var value = conditions[property];

                        waitFuncs[waitFuncs.length] = {
                            message: property,
                            func: value
                        };
                    }
                }

                if (waitFuncs.length > 0) {
                    var t = 0;
                    while (t < this.time) {
                        t = t + this.period;
                        if (this._checkAll(waitFuncs)) {
                            return;
                        }
                        Thread.sleep(this.period);
                    }

                    var errors = "";
                    for (var i = 0; i<waitFuncs.length; i++) {
                        if (!this._apply(waitFuncs[i].func)) {
                            errors = errors + "\n  - " + waitFuncs[i].message;
                        }
                    }

                    if (errors.length > 0) {
                        throw this.message + errors;
                    }
                }
                else throw "You are waiting for nothing";
            },

            _checkAll: function (waitFuncs) {
                for (var i = 0; i<waitFuncs.length; i++) {
                    if (!this._apply(waitFuncs[i].func)) {
                        return false;
                    }
                }
                return true;
            },

            //Need this hack since sometimes it could be function and sometimes it could be an object with apply function inside
            _apply: function (conditionFunc) {
                if (typeof conditionFunc == "function") {
                    return conditionFunc();
                }
                else {
                    return conditionFunc.apply();
                }
            }
        }
    }
};


(function (exports) {
    exports.GalenJs = GalenJs;
})(this);