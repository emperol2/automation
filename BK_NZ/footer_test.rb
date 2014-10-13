require 'test/unit'
require 'rubygems'
require 'selenium-webdriver'

class NzMenuTest < Test::Unit::TestCase

  # Called before every test method runs. Can be used
  # to set up fixture information.
  def setup
    # Do nothing
    @driver = Selenium::WebDriver.for :firefox
    @driver.manage.window.maximize
    @wait = Selenium::WebDriver::Wait.new(timeout: 10)
    @bk_nz_url = 'http://ec2-54-85-128-13.compute-1.amazonaws.com'
    @driver.get @bk_nz_url
  end

  # Called after every test method runs. Can be used to tear
  # down fixture information.

  def test_footer
    @bk_footer = @driver.find_element(:css, 'footer.container-fluid')
    @bk_footer.location_once_scrolled_into_view
    assert element_present?(:css, 'div.footerBg') # Verify Footer Blog
    assert @driver.find_element(:css, 'div.footerBg div.row').text.include?'BK INFO'
    assert @driver.find_element(:css, 'div.col-xs-12 p').text.include?'SHARE THIS WEBSITE'
    assert element_present?(:css, 'div.row div.col-xs-12 div.socialLinks')
    assert @driver.find_element(:xpath, '//footer/div/div[3]/div/p').text.include?'TM & Copyright 2014 Burger King Corporation. All Rights Reserved.'
    @driver.find_element(:id, 'toTop').click  # Back To The Top button
  end

  def element_present?(how, what)
    found = @driver.find_element(how => what)
    if found
      true # return true if this element is found
    else
      false # return false if this element is not found
    end
  rescue Selenium::WebDriver::Error::NoSuchElementError # catch if NoSuchElementError appears
    false
  end

  def teardown
    # Do nothing
    @driver.quit
  end

  # Fake test
  #def test_fail
  #
  #  # To change this template use File | Settings | File Templates.
  #  fail('Not implemented')
  #end
end