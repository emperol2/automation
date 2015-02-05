require 'test/unit'
require 'rubygems'
require 'selenium-webdriver'

class NzFreshOfferTest < Test::Unit::TestCase

  # Called before every test method runs. Can be used
  # to set up fixture information.
  def setup
    # Do nothing
    client = Selenium::WebDriver::Remote::Http::Default.new
    client.timeout = 400
    @driver = Selenium::WebDriver.for :ff, :http_client => client
    #@driver = Selenium::WebDriver.for :firefox
    @driver.manage.window.maximize
    @driver.manage.timeouts.implicit_wait = 300
    @wait = Selenium::WebDriver::Wait.new(timeout: 20)
    @driver.navigate.to 'http://burgerking.co.nz/offers'
  end

  # Called after every test method runs. Can be used to tear
  # down fixture information.

  def test_offers
    assert @driver.title.include?'Offers'
    # Fresh Offer banner
    assert element_present?(:tag_name, 'img')
    assert_true @driver.page_source.include? "http://burgerking.co.nz/sites/default/files/FreshOffer_Coupon.jpg"
  end

  def test_right_left_image
    assert @driver.title.include?'Offers'
    # Verify right image
    assert element_present?(:css, 'div.right-image')
    assert_true @driver.page_source.include? "background-image:url('http://burgerking.co.nz/sites/default/files/Panel_Fries_L.jpg')"
    # Verify left image
    assert element_present?(:css, 'div.left-image')
    assert_true @driver.page_source.include? "background-image:url('http://burgerking.co.nz/sites/default/files/Panel_Fries_L.jpg')"
  end

  def test_crm_block
    assert @driver.title.include?'Offers'
    assert @driver.find_element(:css, 'section.container-fluid.crm')
    #@crm_block = @driver.find_element(:css, 'section.container-fluid.crm')
    #@crm_block.location_once_scrolled_into_view
    assert element_present?(:css, 'section.container-fluid.crm')
    assert element_present?(:css, 'div.col-sm-6.special-stores')
    assert @driver.find_element(:css, 'div.col-sm-6.special-stores div.crmTitle span').text.include? 'Time Out Entertainment Zone'
    assert element_present?(:css, 'div.col-sm-6')
    assert @driver.find_element(:css, 'div.col-sm-6 div.crmText').text.include? 'JOIN THE BK'
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