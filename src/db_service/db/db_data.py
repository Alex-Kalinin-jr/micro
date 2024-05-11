from typing import TYPE_CHECKING


question_data = [
    [
        {
            "type" : "text",
            "text" : "Имеем класс Hero. Hero.id, Hero.name = 'a'.\
                    Какой результат будет При выполнении команд: \
                    session.add(Hero) -> session.commit()->print(hero.name)",
            
        },
        [
            {
                "data" : "null",
                "is_right" : True
            },
            {
                "data" : "test_answer",
                "is_right" : False
            },
        ]

    ],
    [
        {
            "type" : "text",
            "text" : "Чем отличается select.one() от select.first()?",
            
        },
        [
            {
                "data" : "one() выдаст рандомный row",
                "is_right" : False
            },
            {
                "data" : "в случае, если несколько, one() выдаст ошибку",
                "is_right" : True
            },
        ]

    ],
    [
        {
            "type" : "text",
            "text" : "Определите главное назначение back_populates",
            
        },
        [
            {
                "data" : "Установление связей и отношений между таблицами",
                "is_right" : False
            },
            {
                "data" : "обновление связей до коммита изменений",
                "is_right" : True
            },
        ]

    ]
]
