try:
    import telegram
except ImportError:
    raise AssertionError('Модуль telegram не установлен. Посмотрите в README, что нужно для этого сделать.')

try:
    import main
except telegram.error.InvalidToken:
    raise AssertionError('Убедитесь, что токен для класса Bot передан валидный.')


def test_import():
    try:
        main.Bot
    except ImportError:
        raise AssertionError('Импортируйте класс Bot из модуля telegram.')


def test_bot():
    try:
        assert isinstance(main.bot, telegram.Bot), "Переменная bot должна быть экземпляром класса Bot."
    except AttributeError:
        raise AssertionError('Убедитесь, что экземпляр класса Bot назван bot.')


def test_chat_id():
    try:
        isinstance(main.chat_id, str), "Переменная chat_id должна быть строкой."
    except AttributeError:
        raise AssertionError('Убедитесь, что id получателя назван, как chat_id')


def test_text():
    try:
        isinstance(main.text, str), "Переменная text должна быть строкой."
    except AttributeError:
        raise AssertionError('Убедитесь, что текст сообщения назван, как text')


if __name__ == '__main__':
    test_import()
    test_bot()
    test_chat_id()
    test_text()
    print("Все тесты прошли успешно.")
