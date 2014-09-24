require 'test/unit'
require 'rubygems'
require 'selenium-webdriver'

class NzHomeTest < Test::Unit::TestCase

  # Called before every test method runs. Can be used
  # to set up fixture information.
  def setup
    # Do nothing
    @driver = Selenium::WebDriver.for :firefox
    @driver.manage.window.maximize
    @wait = Selenium::WebDriver::Wait.new(timeout: 10)
    @bk_nz_url = 'http://qa.burgerking.co.nz:3333/'
    @driver.get @bk_nz_url
  end

  # Called after every test method runs. Can be used to tear
  # down fixture information.
  def test_home_header
    p @driver.title
    assert @wait.until {@driver.find_element(:css, 'header.container-fluid').displayed?}
    @driver.find_element(:xpath, '//header/div/nav/ul/li').click
    assert @wait.until {@driver.find_element(:css, 'header.container-fluid div.logoNavHolder').displayed?}
    assert element_present?(:css, 'a.logo i.icon')  # Check BK NZ Logo
    @driver.find_element(:css, 'a.logo i.icon').click
  end

  def test_home_banner
    assert_not_nil(@driver.find_element(:css, 'div.carouselItem'), 'Home banner carousel')
    assert_not_nil(@driver.find_element(:css, 'div.content a.bk-btn'), 'Check It Out')
  end

  def test_home_timeout
    assert_not_nil(@driver.find_element(:css, 'section.container-fluid'), 'Time Out Entertainment Zone')
    assert @driver.find_element(:xpath, '//section[2]/div/div/div/span').text.include?'Time Out Entertainment Zone'
    assert element_present?(:xpath, '//section[2]/div/div/div[2]/div/a[2]') # Check Available Here
    assert element_present?(:xpath, '//section[2]/div/div/div[2]/div[2]/a[2]') # Check Fing Out Where

    assert @driver.find_element(:xpath, '//section[2]/div/div[2]/div/span').text.include?'follow your taste buds'
    assert element_present?(:xpath, '//section[2]/div/div[2]/div[2]/div/div/a/i') # Check facebook
    assert element_present?(:xpath, '//section[2]/div/div[2]/div[2]/div/div[2]/a/i') # Check instagram
  end

  def test_home_take_a_break
    @take_a_break = @driver.find_element(:xpath, '/html/body/section[3]')
    @take_a_break.location_once_scrolled_into_view
    assert @wait.until {@driver.find_element(:css, 'ul#flick-inflickity-clone').displayed?}
    assert element_present?(:css, 'ul#flick-inflickity-clone') # Check image on Flick
    assert @driver.find_element(:css, 'h4.subtitle').text.include?'swipe it, flip it, share it'
    @driver.find_element(:css, 'li.item div.flipContainer div.front').click
  end

  def test_home_find_restaurant
    @find_restaurant = @driver.find_element(:css, 'div#homeMap')
    @find_restaurant.location_once_scrolled_into_view
    assert @driver.find_element(:css, 'div.swatch h4.title').text.include?'find a restaurant'
    @driver.find_element(:css, 'input.mapInput').send_key('Montreal')
    @driver.find_element(:css, 'button.submit').click
  end

  def test_home_our_story
    @our_story = @driver.find_element(:xpath, '/html/body/section[5]')
    @our_story.location_once_scrolled_into_view
    assert @driver.find_element(:xpath, '//section[5]/div/h3/span').text.include?'OUR STORY'
    @driver.find_element(:xpath, '//section[5]/div/a').click
  end

  def test_home_bk_callouts
    @bk_callouts = @driver.find_element(:xpath, '/html/body/section[6]')
    @bk_callouts.location_once_scrolled_into_view
    assert element_present?(:xpath, '//section[6]/div/div/div')
    assert element_present?(:xpath, '//section[6]/div/div[2]/div')
    assert element_present?(:xpath, '//section[6]/div/div[3]/div')
    @driver.find_element(:xpath, '//section[6]/div/div[3]/a').click
  end

  def test_home_bk_footer
    @bk_footer = @driver.find_element(:css, 'footer.container-fluid')
    @bk_footer.location_once_scrolled_into_view
    assert element_present?(:css, 'div.footerBg div.row')
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