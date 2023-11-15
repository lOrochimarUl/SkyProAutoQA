from string_utils import StringUtils
import pytest

stringUtilits = StringUtils()


#-------------------------------------------------------------------------------------------------------------------------------
# Первый символ их нижнего регистра в верхний
@pytest.mark.parametrize('utilite, string, result', 
    [(stringUtilits, "hello, my friend", "Hello, my friend"), 
    (stringUtilits, "привет, мой друг", "Привет, мой друг"), 
    (stringUtilits, "1hello, my friend", "1hello, my friend"), 
    (stringUtilits, " hello, my friend", " hello, my friend"), 
    (stringUtilits, "", "")])
def test_first_low_char_into_high(utilite, string, result):
    assert StringUtils.capitilize(utilite, string) == result

@pytest.mark.xfail
def test_n_first_low_char_into_high_without_string():
    with(TypeError):
        StringUtils.capitilize(stringUtilits, None)

#-------------------------------------------------------------------------------------------------------------------------------
# Удаление пробелов в начале строки
@pytest.mark.parametrize('utilite, string, result', 
    [(stringUtilits, "      hello, my friend ", "hello, my friend "), 
    (stringUtilits, "      ", ""), 
    (stringUtilits, "", "")])
def test_whitespace_deleting(utilite, string, result):
    assert StringUtils.trim(utilite, string) == result

@pytest.mark.xfail
def test_n_whitespace_deleting_without_string():
    with(TypeError):
        StringUtils.trim(stringUtilits, None)


#-------------------------------------------------------------------------------------------------------------------------------
# Разделение строк символом
@pytest.mark.parametrize('utilite, string, delimeter, result', 
    [(stringUtilits, "Hello\\ my friend\\ how are you doing?", "\\", ["Hello", " my friend", " how are you doing?"]), 
    (stringUtilits, "Hello, my friend, how are you doing?", " ", ["Hello,", "my", "friend,", "how", "are", "you", "doing?"]), 
    (stringUtilits, "Hello, my friend, how are you doing?", ":", ["Hello, my friend, how are you doing?"]),
    (stringUtilits, "", ",", [])])
def test_string_partition(utilite, string, delimeter, result):
    assert StringUtils.to_list(utilite, string, delimeter) == result

# Разделение строк символом без указания разделителя (по-умолчанию ',')
def test_string_partition_without_specifying_delimeter():
    assert ["Hello", " my friend", " how are you doing?"] == StringUtils.to_list(stringUtilits, "Hello, my friend, how are you doing?")

# Разделение строк символом с указанием разделителя в виде пустой строки
def test_n_string_partition_with_empty_delimeter():
    with pytest.raises(ValueError):
        StringUtils.to_list(stringUtilits, "Hello, my friend, how are you doing?", "")


#-------------------------------------------------------------------------------------------------------------------------------
# Поиск символа в строке
@pytest.mark.parametrize('utilite, string, symbol, result', 
    [(stringUtilits, "Hello", "o", True),
     (stringUtilits, "Привет", "П", True),
     (stringUtilits, "Hello, my friend", " ", True),
     (stringUtilits, "Hello", "F", False),
     (stringUtilits, "Hello", "Hell", True),
     (stringUtilits, "", "F", False)])
def test_symbol_containing(utilite, string, symbol, result):
    assert StringUtils.contains(utilite, string, symbol) == result

@pytest.mark.xfail
def test_n_symbol_containing_without_symbol():
    with(TypeError):
        StringUtils.contains(stringUtilits, "Hello", None, True)

#-------------------------------------------------------------------------------------------------------------------
# Удаление подстроки из строки
@pytest.mark.parametrize('utilite, string, symbols_for_deleting, result', 
    [(stringUtilits, "Hello, my friend", "my", "Hello,  friend"),
     (stringUtilits, "Hello, my friend! Are you okay?", "e", "Hllo, my frind! Ar you okay?"),
     (stringUtilits, "Hello, my friend! Are you okay?", " ", "Hello,myfriend!Areyouokay?"),
     (stringUtilits, "Hello", "Hello", "")])
def test_symbols_deleting(utilite, string, symbols_for_deleting, result):
    assert StringUtils.delete_symbol(utilite, string, symbols_for_deleting) == result

@pytest.mark.xfail
def test_n_symbols_deleting_without_string():
    with(TypeError):
        StringUtils.delete_symbol(stringUtilits, None, "o")

#-------------------------------------------------------------------------------------------------------------------
# Соответствие первых символов строки с заданным значением
@pytest.mark.parametrize('utilite, string, symbol, result',
    [(stringUtilits, "Hello", "H", True),
     (stringUtilits, "Hello", "Hell", True),
     (stringUtilits, "Hello", "llo", False),
     (stringUtilits, "   Hello", "H", False),
     (stringUtilits, "   Hello", " ", True)])
def test_starting_with(utilite, string, symbol, result):
    assert StringUtils.starts_with(utilite, string, symbol) == result

@pytest.mark.xfail
def test_n_symbol_containing_without_string():
    with(TypeError):
        StringUtils.starts_with(stringUtilits, None, "o", True)

#-------------------------------------------------------------------------------------------------------------------
# Соответствие последних символов строки с заданным значением
@pytest.mark.parametrize('utilite, string, symbol, result',
    [(stringUtilits, "Hello", "o", True),
     (stringUtilits, "Hello", "lo", True),
     (stringUtilits, "Hello", "ll", False),
     (stringUtilits, "Hello   ", "o", False),
     (stringUtilits, "Hello   ", " ", True)])
def test_ending_with(utilite, string, symbol, result):
    assert StringUtils.end_with(utilite, string, symbol) == result

@pytest.mark.xfail
def test_n_ending_with_without_string():
    with(TypeError):
        StringUtils.end_with(stringUtilits, None, "o", True)

#-------------------------------------------------------------------------------------------------------------------
# Пустая строка или нет
@pytest.mark.parametrize('utilite, string, result', 
    [(stringUtilits, "      ", True), 
    (stringUtilits, "", True), 
    (stringUtilits, " , ", False)])
def test_is_empty(utilite, string, result):
    assert StringUtils.is_empty(utilite, string) == result

@pytest.mark.xfail
def test_n_is_empty_without_string():
    with(TypeError):
        StringUtils.is_empty(stringUtilits, None, True)

#-------------------------------------------------------------------------------------------------------------------
# Список строк в одну строку с разделителем
@pytest.mark.parametrize('utilite, list, delimeter, result', 
    [(stringUtilits, [1, 2, 3, 4, 5], ", ", "1, 2, 3, 4, 5"), 
    (stringUtilits, ["Aunt", "Baby", "Center"], "\\ ", "Aunt\\ Baby\\ Center"),
    (stringUtilits, [1], ", ", "1"),
    (stringUtilits, ["",""], " " , " "),
    (stringUtilits, [], " ", ""),
    (stringUtilits, [1, 2, 3, 4, 5], "", "12345" )])
def test_list_to_string(utilite, list, delimeter, result):
    assert StringUtils.list_to_string(utilite, list, delimeter) == result

@pytest.mark.xfail
def test_n_list_to_string_int_instead_of_list():
    with(TypeError):
        StringUtils.list_to_string(stringUtilits, 123, True)