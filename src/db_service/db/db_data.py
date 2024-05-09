from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import QuestionType

question_data = [
    {
        {
            "type" : QuestionType.TEXT,
            "text" : "Имеем класс Hero. Hero.id, Hero.name = 'a'.\
                    Какой результат будет При выполнении команд: \
                    session.add(Hero) -> session.commit()->print(hero.name)",
            
        },
        [
            {
                "text" : "null",
                "is_right" : True
            },
            {
                "text" : "test_answer",
                "is_right" : False
            },
        ]

    },
    {
        {
            "type" : QuestionType.TEXT,
            "text" : "Чем отличается select.one() от select.first()?",
            
        },
        [
            {
                "text" : "one() выдаст рандомный row",
                "is_right" : False
            },
            {
                "text" : "в случае, если несколько, one() выдаст ошибку",
                "is_right" : True
            },
        ]

    },
    {
        {
            "type" : QuestionType.TEXT,
            "text" : "Определите главное назначение back_populates",
            
        },
        [
            {
                "text" : "Установление связей и отношений между таблицами",
                "is_right" : False
            },
            {
                "text" : "обновление связей до коммита изменений",
                "is_right" : True
            },
        ]

    }
]
