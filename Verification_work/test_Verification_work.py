from Task1 import Form
from Task2 import Calculator
from Task3 import Sauce
import pytest


#--------------------------------------------------------------------------
#Автотест задания №1
form = Form()
red_color = 'rgba(248, 215, 218, 1)'
green_color = 'rgba(209, 231, 221, 1)'

@pytest.mark.vw
def test_red_and_green_color():
    assert Form.filling_form_uncompletely(green_color, red_color) == [True, True]



#--------------------------------------------------------------------------
#Автотест задания №2
calculator = Calculator
@pytest.mark.vw
@pytest.mark.parametrize('first_number, second_number, summ',
                          [(7, 8, '15'),
                           (3, 1, '4'),
                           (7, 2, '9')])
def test_calculate(first_number, second_number, summ):
    assert calculator.calculate(first_number, second_number) == summ



#--------------------------------------------------------------------------
#Автотест задания №3
sauce = Sauce
@pytest.mark.vw
def test_some_sauce():
    assert sauce.want_sauce() == " $58.29"
