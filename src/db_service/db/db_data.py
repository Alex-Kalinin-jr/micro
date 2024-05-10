from typing import TYPE_CHECKING


question_data = [
    [
        {
            "id" : 1,
            "type" : "text",
            "text" : "Имеем класс Hero. Hero.id, Hero.name = 'a'.\
                    Какой результат будет При выполнении команд: \
                    session.add(Hero) -> session.commit()->print(hero.name)",
            
        },
        [
            {
                "id" : 1,
                "question_id" : 1,
                "data" : "null",
                "is_right" : True
            },
            {
                "id" : 2,
                "question_id" : 1,
                "data" : "test_answer",
                "is_right" : False
            },
        ]

    ],
    [
        {
            "id" : 2,
            "type" : "text",
            "text" : "Чем отличается select.one() от select.first()?",
            
        },
        [
            {
                "id" : 3,
                "question_id" : 2,
                "data" : "one() выдаст рандомный row",
                "is_right" : False
            },
            {
                "id" : 4,
                "question_id" : 2,
                "data" : "в случае, если несколько, one() выдаст ошибку",
                "is_right" : True
            },
        ]

    ],
    [
        {
            "id" : 3,
            "type" : "text",
            "text" : "Определите главное назначение back_populates",
            
        },
        [
            {
                "id" : 5,
                "question_id" : 3,
                "data" : "Установление связей и отношений между таблицами",
                "is_right" : False
            },
            {
                "id" : 6,
                "question_id" : 3,
                "data" : "обновление связей до коммита изменений",
                "is_right" : True
            },
        ]

    ]
]
