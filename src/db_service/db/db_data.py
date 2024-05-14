from typing import TYPE_CHECKING


question_data = [
    [
        {
            "type" : "text",
            "text" : "Имеем класс Hero. Hero.id, Hero.name = 'a'.\
                    Какой результат будет При выполнении команд: \
                    session.add(Hero) -> session.commit()->print(hero.name)",
            "category" : "SQLModel"
            
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
            "category" : "SQLModel"
            
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
            "category" : "SQLModel"
            
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

    ],
    [
        {
            "type" : "text",
            "text" : "Какого типа SSL сертификатов не существует",
            "category" : "security"
            
        },
        [
            {
                "data" : "Extended Validation certificates",
                "is_right" : False
            },
            {
                "data" : "Organization Validated certificates ",
                "is_right" : False
            },
            {
                "data" : "Domain Validated certificates",
                "is_right" : False
            },
            {
                "data" : "Wildcard SSL certificates",
                "is_right" : False
            },
            {
                "data" : "Multi-Domain SSL certificates",
                "is_right" : False
            },
            {
                "data" : "Unified Communications Certificates",
                "is_right" : False
            },
            {
                "data" : "Transport Layer certificates",
                "is_right" : True
            },

        ]

    ],
    
]

links_data = [
    {
        "data" : "https://testdriven.io/blog/fastapi-sqlmodel/",
        "explanation" : "Good article for integration async Alembic (initial aquantance with alembic is needed)."
    }
]
